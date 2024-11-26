"""Define the left drawer component."""

from nicegui import ui

from sprongle.style import bg_100


class LeftDrawer(ui.left_drawer):
    """The sprongle app's left drawer component."""

    def __init__(self) -> None:
        super().__init__(
            value=True,
            fixed=False,
            bordered=False,
            elevated=False,
            top_corner=False,
            bottom_corner=False,
        )

        self.classes(bg_100)
