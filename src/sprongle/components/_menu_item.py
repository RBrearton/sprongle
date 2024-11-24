"""Define a simple menu item that links to a page."""

from nicegui import ui

from sprongle import style


class MenuItem(ui.item):
    """A menu item that links to a page."""

    def __init__(self, text: str, link: str) -> None:
        super().__init__(text=text, on_click=lambda: ui.navigate.to(link))

        self.props("flat")
        self.classes(style.menu_item)
