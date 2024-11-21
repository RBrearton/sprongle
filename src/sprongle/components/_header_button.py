"""Define the buttons that are used in the site's header."""

from nicegui import ui


class HeaderButton(ui.button):
    def __init__(self, text: str, link: str) -> None:
        super().__init__(text=text, on_click=lambda: ui.navigate.to(link))

        self.classes("text-white py-2 px-4 text-lg")
        self.props("rounded flat no-caps")
