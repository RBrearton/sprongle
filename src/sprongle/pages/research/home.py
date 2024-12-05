"""Define the research home page."""

from nicegui import ui

from sprongle import components as c
from sprongle._sprongle_page import SpronglePage


class ResearchHome(SpronglePage):
    """The research home page."""

    def __init__(self) -> None:
        """Create the research home page."""
        super().__init__("research")

    def make_content(self) -> ui.element:  # noqa: D102
        with ui.element() as div:
            c.Title("Research", level=1)
            c.Text(R"""
I'm very interested in computational physics.

For generations, physicists have trained to become expert mathematicians, as mathematics has always been the best language to use to describe physical systems.
This is no longer the case.
The perfection provided by mathematics is incredible, but maths is hard, and there's no way to get around that.
Progress on problems that *might* be solvable is extremely slow, and the overwhelming majority of interesting problems are unsolvable.

Nowadays, almost all research papers contain some form of numerical simulation.
Most numerical work done by physicists is, unfortunately, completely amateurish.
This is because physicists are expert mathematicians with very little training in numerical methods.

I would like to improve this situation.
""")

        return div
