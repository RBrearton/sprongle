"""Define the site's header component."""

from nicegui import ui

from sprongle.style import bg_primary

from ._dark_mode_toggle import DarkModeToggle
from ._github_link import GithubLink
from ._header_button import HeaderButton


class Header(ui.header):
    """Define the header component."""

    def __init__(self, *, title: str) -> None:
        # Set up the header the way we like it.
        super().__init__(
            value=True,
            fixed=True,
            bordered=True,
            elevated=False,
            add_scroll_padding=True,
        )
        self.classes(bg_primary)

        # Add the contents of the header.
        with self:
            # Make three equally spaced sections.
            with ui.element().classes(
                "flex flex-row justify-between items-center w-full"
            ):
                # Everything here lives on the left.
                with ui.element().classes(
                    "flex flex-row items-center justify-start flex-1"
                ):
                    # Add the title.
                    ui.markdown(f"#### {title}").classes("py-2")

                # Add the central buttons.
                with ui.element().classes(
                    "flex flex-row items-center justify-center flex-1"
                ):
                    HeaderButton("Home", "/")
                    HeaderButton("Physics", "/physics")

                # Add the right section.
                with ui.element().classes(
                    "max-md:hidden flex flex-row items-center justify-end "
                    "flex-1"
                ):
                    DarkModeToggle()
                    GithubLink()
