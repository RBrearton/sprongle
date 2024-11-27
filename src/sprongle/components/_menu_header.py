"""Define the MenuHeader component."""

from nicegui import ui


class MenuHeader(ui.html):
    """The MenuHeader component is used to make headers for the menus."""

    def __init__(self, text: str) -> None:
        super().__init__(content=text, tag="q-item-label")
        self.props("header")
        self.classes("font-bold")
