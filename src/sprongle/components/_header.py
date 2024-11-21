"""Define the site's header component."""

from nicegui import ui


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
            # Add the title.
            ui.markdown(f"#### {title}")
