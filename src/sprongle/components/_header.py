"""Define the site's header component."""

from nicegui import ui

from sprongle.style import bg_primary, header_clickable

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
        self._drawer_ref: ui.drawer | None = None

        # Add the contents of the header.
        with self:
            # Make three equally spaced sections.
            with ui.element().classes(
                "flex flex-row justify-between items-center w-full"
            ):
                # Everything here lives on the left.
                with ui.element().classes(
                    "flex flex-row items-end justify-start flex-1"
                ):
                    # Toggle the drawer if we've been given a reference to it.
                    self.drawer_toggle = (
                        ui.button(icon="menu")
                        .classes("text-lg mb-[2px]")
                        .classes(header_clickable)
                        .classes("text-white p-2")
                        .classes("xl:hidden")
                        .props("flat round")
                        .on(
                            "click",
                            lambda: self._drawer_ref.toggle()
                            if self._drawer_ref
                            else None,
                        )
                    )

                    # Add the title.
                    ui.markdown(f"#### {title}").classes("p-2")

                # Add the central buttons.
                with ui.element().classes(
                    "flex flex-row items-center justify-center flex-1"
                ):
                    HeaderButton("Home", "/")
                    HeaderButton("Physics", "/physics")
                    HeaderButton("Research", "/research")

                # Add the right section.
                with ui.element().classes(
                    "max-md:hidden flex flex-row items-center justify-end "
                    "flex-1"
                ):
                    DarkModeToggle()
                    GithubLink()

    def set_drawer_ref(self, drawer_ref: ui.drawer) -> None:
        """Set the reference to the drawer."""
        self._drawer_ref = drawer_ref
