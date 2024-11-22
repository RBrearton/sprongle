"""Define the left drawer component."""

from nicegui import ui

from ._menu import Menu


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

        with self:
            Menu()
