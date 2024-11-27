"""Define the problem set 2 page's main content."""

from nicegui import ui

from sprongle import components as c
from sprongle._sprongle_page import SpronglePage


class B2ProblemSet2(SpronglePage):
    """Define the B2 problem set 2 solutions page."""

    def __init__(self) -> None:  # noqa: D107
        super().__init__("physics")

    def make_content(self) -> ui.element:  # noqa: D102:
        with ui.element() as div:
            ui.markdown("# B2 problem set 2")
            q1_title = c.Title.menu_title(
                "Q1: The rotation formula", level=2, parent=self
            )
            c.Title.menu_title("Part a", level=3, parent=q1_title)
            c.Title.menu_title("Part b", level=4, parent=q1_title)
            c.Title.menu_title("Part c", level=5, parent=q1_title)
            c.Title.menu_title("Part d", level=6, parent=q1_title)
            q2_title = c.Title.menu_title(
                "Q2: The moment of inertia of a hoop", level=2, parent=self
            )
            c.Title.menu_title("Part a", level=3, parent=q2_title)
            c.Title.menu_title("Part b", level=3, parent=q2_title)
            c.Title.menu_title("Part c", level=3, parent=q2_title)
            c.Title.menu_title("Part d", level=3, parent=q2_title)
        return div
