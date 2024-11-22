"""Define the site's header component."""

from nicegui import ui

from ._github_link import GithubLink
from ._header_button import HeaderButton


class Header(ui.header):
    """Define the header component."""

    def __init__(self, *, title: str) -> None:
        # Set up the header the way we like it.
        super().__init__(
            value=True,
            fixed=False,
            bordered=True,
            elevated=False,
            add_scroll_padding=True,
        )

        # Add the contents of the header.
        with self:
            # Make three equally spaced sections.
            with ui.row().classes("flex justify-between items-center w-full"):
                # Add the title.
                ui.markdown(f"#### {title}")

                # Add the central buttons.
                with ui.row():
                    HeaderButton("Home", "/")
                    HeaderButton("Physics", "/physics")

                # Add the right section.
                with ui.row():
                    GithubLink()
