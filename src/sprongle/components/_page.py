"""Define the core page template."""

from nicegui import ui

from ._header import Header
from ._header_button import HeaderButton


class Page(ui.element):
    """Define the core page template."""

    def __init__(self, content: ui.element) -> None:
        """Set up a standard page.

        The content of the page, to be displayed in the central area, should be
        passed in as an argument.
        """
        super().__init__()

        # Set up the page with the usual content.
        with self:
            Header("sprongle")
