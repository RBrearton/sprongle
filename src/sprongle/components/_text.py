"""Define a simple Text component."""

from functools import lru_cache

from markdown2 import markdown  # type: ignore  # noqa: PGH003
from nicegui import ui

# These are all of the extras that we opt into by default. To see all the
# available options, read the wiki:
# https://github.com/trentm/python-markdown2/wiki
default_extras = [
    "latex",
    "admonitions",
    "fenced-code-blocks",
    "tables",
    "footnotes",
    "code-friendly",
    "cuddled-lists",
    "metadata",
    "task_list",
    "strike",
    "header-ids",
]


@lru_cache
def render_markdown(markdown_text: str) -> str:
    """Render markdown text to HTML."""
    return markdown(markdown_text, extras=default_extras)


class Text(ui.html):
    """A simple text component.

    The text can be any markdown text, and it will be rendered for you by this
    component. If you don't want the text to be a paragraph, you can set the
    is_paragraph parameter to False.
    """

    def __init__(self, text: str, *, is_paragraph: bool = True) -> None:
        super().__init__(content=text, tag="p" if is_paragraph else "span")
        self.classes("w-full")
