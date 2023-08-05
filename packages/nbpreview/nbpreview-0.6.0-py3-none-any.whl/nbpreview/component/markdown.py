"""Override rich's markdown renderer with custom components."""
import dataclasses
import enum
import io
import os
import pathlib
import textwrap
from io import BytesIO
from pathlib import Path
from typing import Iterable, Iterator, Optional, Union
from urllib import parse

import httpx
import PIL
import validators
import yarl
from PIL import Image
from rich import _loop, markdown, measure, rule, segment, style, syntax, text
from rich.console import (
    Console,
    ConsoleOptions,
    JustifyMethod,
    RenderableType,
    RenderResult,
)
from rich.measure import Measurement
from rich.style import Style
from rich.text import Text

from nbpreview.component.content.output.result import drawing, link, markdown_extensions
from nbpreview.component.content.output.result.drawing import ImageDrawing
from nbpreview.component.content.output.result.markdown_extensions import (
    MarkdownExtensionSection,
)


class CustomCodeBlock(markdown.CodeBlock):
    """A custom code block with syntax highlighting."""

    style_name = "none"

    def __init__(self, lexer_name: str, theme: str) -> None:
        """Constructor."""
        super().__init__(lexer_name=lexer_name, theme=theme)

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult:
        """Render the custom code block."""
        code = textwrap.indent(str(self.text).rstrip(), prefix=" " * 4)
        rendered_syntax = syntax.Syntax(
            code, self.lexer_name, theme=self.theme, background_color="default"
        )
        yield rendered_syntax


@enum.unique
class HeadingColorEnum(enum.Enum):
    """The heading color."""

    PURPLE = enum.auto()
    TEAL = enum.auto()


class CustomHeading(markdown.Heading):
    """A custom rendered markdown heading."""

    def __init__(self, level: int) -> None:
        """Constructor."""
        self.level = level

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult:
        """Render the custom markdown heading."""
        source_text = self.text
        source_text.justify = "left"
        if self.level == 1:
            header_color = (
                "color(57)"
                if console.color_system in ["truecolor", "256"]
                else "color(5)"
            )
            header_style = style.Style(
                color="color(231)", bgcolor=header_color, bold=True
            )
            source_text.stylize(header_style)
            if source_text.cell_len < console.width:
                source_text = text.Text(" ", style=header_style) + source_text
            if source_text.cell_len < console.width:
                source_text = source_text + text.Text(" ", style=header_style)

            yield source_text
        else:
            header_color = (
                "color(37)"
                if console.color_system in ["truecolor", "256"]
                else "color(6)"
            )
            header_style = style.Style(color=header_color, bold=True)
            source_text.stylize(header_style)
            source_text = (
                text.Text(self.level * "#" + " ", style=header_style) + source_text
            )
            if self.level <= 3:
                yield text.Text("")
            yield source_text

        if self.level < 3:
            yield rule.Rule(style=style.Style(color=header_color, dim=True, bold=False))


class CustomBlockQuote(markdown.BlockQuote):
    """A custom block quote."""

    style_name = style.Style(dim=True)  # type: ignore[assignment]


class CustomHorizontalRule(markdown.HorizontalRule):
    """A customized horizontal rule to divide sections."""

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult:
        """Render the horizontal rule."""
        yield rule.Rule(style="none")


class CustomListItem(markdown.ListItem):
    """A custom list element."""

    def render_bullet(self, console: Console, options: ConsoleOptions) -> RenderResult:
        """Render a markdown bullet."""
        render_options = options.update(width=options.max_width - 3)
        lines = console.render_lines(self.elements, render_options, style=self.style)
        bullet_style = console.get_style("none")

        bullet = segment.Segment(" • ", bullet_style)
        padding = segment.Segment(" " * 3, bullet_style)
        new_line = segment.Segment("\n")
        for first, line in _loop.loop_first(lines):
            yield bullet if first else padding
            yield from line
            yield new_line

    def render_number(
        self, console: Console, options: ConsoleOptions, number: int, last_number: int
    ) -> RenderResult:
        """Render a markdown number."""
        number_width = len(str(last_number)) + 2
        render_options = options.update(width=options.max_width - number_width)
        lines = console.render_lines(self.elements, render_options, style=self.style)
        number_style = console.get_style("none")

        new_line = segment.Segment("\n")
        padding = segment.Segment(" " * number_width, number_style)
        numeral = segment.Segment(
            f"{number}.".rjust(number_width - 1) + " ", number_style
        )
        for first, line in _loop.loop_first(lines):
            yield numeral if first else padding
            yield from line
            yield new_line


def _get_url_content(url: str) -> Union[BytesIO, None]:
    """Return content from URL."""
    try:
        response = httpx.get(url)
    except httpx.RequestError:
        content = None
    else:
        try:
            content = io.BytesIO(response.content)
        except TypeError:
            content = None
    return content


class CustomImageItem(markdown.ImageItem):
    """Renders a placeholder for an image."""

    nerd_font: bool = False
    unicode: bool = True
    images: bool = True
    image_drawing: ImageDrawing = "block"
    color: bool = True
    characters: Optional[str] = None
    files: bool = True
    hide_hyperlink_hints: bool = False
    negative_space: bool = True
    relative_dir: Path = dataclasses.field(default_factory=pathlib.Path)

    def __init__(self, destination: str, hyperlinks: bool) -> None:
        """Constructor."""
        content: Union[None, Path, BytesIO]
        self.image_data: Union[None, bytes]
        self.destination = destination
        if not validators.url(self.destination):
            # destination comes in a url quoted format, which will turn
            # Windows-like paths into %5c, unquote here to that pathlib
            # understands correctly
            if (
                destination_path := pathlib.Path(parse.unquote(self.destination))
            ).is_absolute():
                self.path = destination_path
            else:
                self.path = self.relative_dir / destination_path
            self.path = self.path.resolve()
            self.destination = os.fsdecode(self.path)
            content = self.path
            self.is_url = False
        else:
            self.is_url = True
            self.path = pathlib.Path(yarl.URL(self.destination).path)
            content = _get_url_content(self.destination)
        self.extension = self.path.suffix.lstrip(".")
        if content is not None and (self.images or (self.is_url and self.files)):
            try:
                with Image.open(content) as image:
                    with io.BytesIO() as output:
                        try:
                            format = Image.EXTENSION[f".{self.extension}"]
                        except KeyError:
                            self.image_data = None
                        else:
                            image.save(output, format=format)
                            self.image_data = output.getvalue()
            except (FileNotFoundError, PIL.UnidentifiedImageError):
                self.image_data = None

        else:
            self.image_data = None

        super().__init__(destination=self.destination, hyperlinks=hyperlinks)

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult:
        """Render the image."""
        title = self.text.plain or self.destination
        if self.is_url:
            rendered_link = link.Link(
                path=self.destination,
                nerd_font=self.nerd_font,
                unicode=self.unicode,
                subject=title,
                emoji_name="globe_with_meridians",
                nerd_font_icon="爵",
                hyperlinks=self.hyperlinks,
                hide_hyperlink_hints=self.hide_hyperlink_hints,
            )

        else:
            rendered_link = link.Link(
                path=f"file://{self.destination}",
                nerd_font=self.nerd_font,
                unicode=self.unicode,
                subject=title,
                emoji_name="framed_picture",
                nerd_font_icon="",
                hyperlinks=self.hyperlinks,
                hide_hyperlink_hints=self.hide_hyperlink_hints,
            )

        yield rendered_link

        if self.images:
            fallback_title = self.destination.strip("/").rsplit("/", 1)[-1]
            rendered_drawing = drawing.choose_drawing(
                image=self.image_data,
                fallback_text=self.text.plain or fallback_title,
                image_type=f"image/{self.extension}",
                image_drawing=self.image_drawing,
                color=self.color,
                negative_space=self.negative_space,
                characters=self.characters,
            )
            if rendered_drawing is not None:
                yield text.Text("")
                yield rendered_drawing


class MarkdownOverwrite(markdown.Markdown):
    """A custom markdown renderer."""

    def __init__(
        self,
        markup: str,
        code_theme: str = "monokai",
        justify: Optional[JustifyMethod] = None,
        style: Union[str, Style] = "none",
        hyperlinks: bool = True,
        inline_code_lexer: Optional[str] = None,
        inline_code_theme: str = "dark",
        nerd_font: bool = False,
        unicode: bool = True,
        images: bool = True,
        image_drawing: ImageDrawing = "block",
        color: bool = True,
        negative_space: bool = True,
        characters: Optional[str] = None,
        files: bool = True,
        hide_hyperlink_hints: bool = False,
        relative_dir: Optional[Path] = None,
    ) -> None:
        """Constructor."""
        relative_dir = relative_dir if relative_dir is not None else pathlib.Path()
        self.elements["code_block"] = CustomCodeBlock
        self.elements["heading"] = CustomHeading
        self.elements["block_quote"] = CustomBlockQuote
        self.elements["thematic_break"] = CustomHorizontalRule
        self.elements["item"] = CustomListItem
        self.elements["image"] = CustomImageItem

        CustomImageItem.nerd_font = nerd_font
        CustomImageItem.images = images
        CustomImageItem.unicode = unicode
        CustomImageItem.image_drawing = image_drawing
        CustomImageItem.color = color
        CustomImageItem.negative_space = negative_space
        CustomImageItem.characters = characters
        CustomImageItem.files = files
        CustomImageItem.hide_hyperlink_hints = hide_hyperlink_hints
        CustomImageItem.relative_dir = relative_dir
        super().__init__(
            markup=markup,
            code_theme=code_theme,
            justify=justify,
            style=style,
            hyperlinks=hyperlinks,
            inline_code_lexer=inline_code_lexer,
            inline_code_theme=inline_code_theme,
        )


@dataclasses.dataclass
class CustomMarkdown:
    """A custom markdown renderer with table support."""

    source: str
    theme: str
    relative_dir: Path
    hyperlinks: bool = True
    nerd_font: bool = False
    unicode: bool = True
    images: bool = True
    image_drawing: ImageDrawing = "block"
    color: bool = True
    negative_space: bool = True
    characters: Optional[str] = None
    files: bool = True
    hide_hyperlink_hints: bool = False

    def __post_init__(self) -> None:
        """Constructor."""
        table_sections = markdown_extensions.parse_markdown_extensions(
            self.source, unicode=self.unicode
        )
        self.renderables = [
            renderable
            for renderable in _splice_tables(
                self.source,
                table_sections=table_sections,
                theme=self.theme,
                hyperlinks=self.hyperlinks,
                nerd_font=self.nerd_font,
                unicode=self.unicode,
                images=self.images,
                image_drawing=self.image_drawing,
                color=self.color,
                negative_space=self.negative_space,
                characters=self.characters,
                files=self.files,
                hide_hyperlink_hints=self.hide_hyperlink_hints,
                relative_dir=self.relative_dir,
            )
        ]

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult:
        """Render the markdown."""
        yield from self.renderables

    def __rich_measure__(
        self, console: Console, options: ConsoleOptions
    ) -> Measurement:
        """Define the dimensions of the rendered markdown."""
        measurement = measure.measure_renderables(
            console=console, options=options, renderables=self.renderables
        )
        return measurement


def _splice_tables(
    markup: str,
    table_sections: Iterable[MarkdownExtensionSection],
    theme: str,
    hyperlinks: bool,
    nerd_font: bool,
    unicode: bool,
    images: bool,
    image_drawing: ImageDrawing,
    color: bool,
    negative_space: bool,
    files: bool,
    hide_hyperlink_hints: bool,
    relative_dir: Path,
    characters: Optional[str] = None,
) -> Iterator[Union[MarkdownOverwrite, RenderableType, Text]]:
    """Mix in tables with traditional markdown parser."""
    markup_lines = markup.splitlines()
    last_end_point = 0
    for table_section in table_sections:
        non_table_section = "\n".join(
            markup_lines[last_end_point : table_section.start_line]
        )
        yield MarkdownOverwrite(
            non_table_section,
            code_theme=theme,
            hyperlinks=hyperlinks,
            nerd_font=nerd_font,
            unicode=unicode,
            images=images,
            image_drawing=image_drawing,
            color=color,
            negative_space=negative_space,
            characters=characters,
            files=files,
            hide_hyperlink_hints=hide_hyperlink_hints,
            relative_dir=relative_dir,
        )
        yield text.Text()
        yield table_section.renderable

        yield text.Text()
        last_end_point = table_section.end_line + 1
    end_section = "\n".join(markup_lines[last_end_point:])
    yield MarkdownOverwrite(
        end_section,
        code_theme=theme,
        hyperlinks=hyperlinks,
        nerd_font=nerd_font,
        unicode=unicode,
        images=images,
        image_drawing=image_drawing,
        color=color,
        negative_space=negative_space,
        characters=characters,
        files=files,
        hide_hyperlink_hints=hide_hyperlink_hints,
        relative_dir=relative_dir,
    )
