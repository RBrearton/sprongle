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
    """A simple text component."""

    def __init__(self, text: str, *, is_span: bool = False) -> None:
        super().__init__(content=text, tag="span" if is_span else "p")
        self.classes("w-full")
