"""Define the buttons that are used in the site's header."""

from nicegui import ui

from sprongle import style


class HeaderButton(ui.html):
    def __init__(self, text: str, link: str) -> None:
        super().__init__(content=text, tag="q-btn")

        # When the button is clicked, navigate to the link.
        self.on("click", lambda: ui.navigate.to(link))

        # This is a clickable in the header, so...
        self.classes(style.header_clickable)

        # These are specific to the fact that this is a button.
        self.props("rounded flat no-caps")
        self.classes("py-2 px-4 text-lg")
