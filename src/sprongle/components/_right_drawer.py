"""Define the right drawer component."""

from nicegui import ui


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

        with self:
            ui.markdown("Placeholder right menu.")
