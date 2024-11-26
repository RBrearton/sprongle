"""Define the right drawer component."""

from nicegui import ui

from sprongle.style import bg_100


class RightDrawer(ui.right_drawer):
    """The sprongle app's right drawer component."""

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

        with self:
            ui.markdown("Placeholder right menu.")
