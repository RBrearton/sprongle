"""Define the right drawer component."""

from nicegui import ui

from sprongle.style import bg_100, bg_content


class RightDrawer(ui.right_drawer):
    """The sprongle app's right drawer component."""

    def __init__(self) -> None:
        super().__init__(
            value=True,
            fixed=True,
            bordered=False,
            elevated=False,
            top_corner=False,
            bottom_corner=False,
        )
        self.props("breakpoint=1250")
        self.classes(f"{bg_100} {bg_content}")
