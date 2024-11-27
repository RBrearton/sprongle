"""Define the MarkdownPage class."""

from nicegui import ui

from sprongle import utils

from ._sprongle_page import SpronglePage


class MarkdownPage(SpronglePage):
    """A SpronglePage that's generated from the path to a markdown file."""

    def __init__(
        self,
        subdomain_name: str,
        page_path: str,
    ) -> None:
        super().__init__(subdomain_name)

        self._page_path = page_path
        self._parsed_markdown = utils.get_markdown(self._page_path)

    def make_right_drawer_content(self) -> None:
        return None

    def make_content(self) -> ui.element:
        return ui.markdown(
            self._parsed_markdown,
            extras=["tables", "fenced-code-blocks", "latex"],
        )
