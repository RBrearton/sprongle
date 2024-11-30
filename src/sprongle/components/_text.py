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

    def __init__(self, text: str, *, is_paragraph: bool = False) -> None:
        rendered_text = render_markdown(text)

        # This always renders as a paragraph, which we never want, because this
        # is going to be put as an input into either a <p> or a <span> tag. If
        # we didn't do this and we asked for a paragraph, our html would look
        # like <p><p>...</p></p>, which is never what we want.
        if rendered_text.startswith("<p>"):
            # We still check for the <p>, just in case!
            rendered_text = rendered_text[3:-5]

        super().__init__(
            content=rendered_text, tag="p" if is_paragraph else "span"
        )
        self.classes("w-full")
