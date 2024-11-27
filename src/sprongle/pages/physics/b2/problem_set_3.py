"""Define the problem set 2 page's main content."""

from nicegui import ui

from sprongle import components as c
from sprongle._sprongle_page import SpronglePage


class B2ProblemSet3(SpronglePage):
    """Define the B2 problem set 3 page."""

    def __init__(self) -> None:  # noqa: D107
        super().__init__("physics")

    def make_content(self) -> ui.element:  # noqa: D102, PLR0915:
        with ui.element() as div:
            c.Title("B2 problem set 3", level=1)
            q1_title = c.Title.menu_title(
                "Q1: Evaluation of derivatives for a four-vector field",
                level=2,
                parent=self,
            )
            c.Text(r"""
This question is all about practicing taking derivatives of a four-vector.
We're told that $F^\mu$ is given by
""")
            q1_field = c.Text(r"""
$$
F^\mu = 2X^\mu + K^\mu (X^\nu X_\nu)
$$
""")
            c.Text(r"""
where $K^\mu$ is a constant four-vector, and

$$
X^\mu = \left( ct,\, x,\, y,\, z\right)
$$

is the spacetime position four-vector.
Evaluate the following:
""")
            c.Title.menu_title("Part a", level=3, parent=q1_title)
            c.Text(r"""

<blockquote>
$$
\partial_\lambda X^\lambda
$$
</blockquote>

This is the divergence of the position four-vector.
""")
            with c.Admonition.show_answer():
                c.Text(r"""
$$
\partial_\lambda X^\lambda = 4
$$
""")

        return div
