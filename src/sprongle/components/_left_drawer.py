"""Define the left drawer component."""

from nicegui import ui

from sprongle.style import bg_100, bg_content, large_screen_px


class LeftDrawer(ui.left_drawer):
    """The sprongle app's left drawer component."""

    def __init__(self) -> None:
        super().__init__(
            fixed=True,
            bordered=False,
            elevated=False,
            top_corner=False,
            bottom_corner=False,
        )
        self.props(f"breakpoint={large_screen_px}")
        self.classes(f"{bg_100} {bg_content}")
