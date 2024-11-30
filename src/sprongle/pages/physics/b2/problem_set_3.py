"""Define the problem set 2 page's main content."""

from nicegui import ui

from sprongle import components as c
from sprongle._sprongle_page import SpronglePage


class B2ProblemSet3(SpronglePage):
    """Define the B2 problem set 3 page."""

    def __init__(self) -> None:  # noqa: D107
        super().__init__("physics")

    def make_content(self) -> ui.element:  # noqa: D102:
        with ui.element() as div:
            c.Title("B2 problem set 3", level=1)
            q1_title = c.Title.menu_title(
                "Q1: Evaluation of derivatives for a four-vector field",
                level=2,
                parent=self,
            )

            c.Text(R"""
This question is all about practicing taking derivatives of a four-vector.
We're told that $F^\mu$ is given by
""")
            q1_field = c.Text(R"""
$$
F^\mu = 2X^\mu + K^\mu (X^\nu X_\nu)
$$
""")
            c.Text(R"""
where $K^\mu$ is a constant four-vector, and

$$
X^\mu = \left( ct,\, x,\, y,\, z\right)
$$

is the spacetime position four-vector.
Evaluate the following:
""")
            c.Title.menu_title("Part a", level=3, parent=q1_title)
            c.Text(R"""

<blockquote>
$$
\partial_\lambda X^\lambda
$$
</blockquote>

This is the divergence of the position four-vector.
""")
            with c.Admonition.show_answer():
                c.Text(R"""
$$
\partial_\lambda X^\lambda = 4
$$
""")
            c.Title.menu_title("Part b", level=3, parent=q1_title)
            c.Text(R"""
<blockquote>
$$
\partial^\mu (X_\lambda X^\lambda)
$$
</blockquote>

This one requires a bit more working.
""")
            with c.Admonition.show_working():
                c.Text(R"""
We can start by applying the product rule.

$$
\partial^\mu (X_\lambda X^\lambda) = X_\lambda \partial^\mu X^\lambda + X^\lambda \partial^\mu X_\lambda
$$

The term $X^\lambda \partial^\mu X_\lambda$ just gives us

$$
X^\lambda \partial^\mu X_\lambda =  X^\lambda \delta^\mu_\lambda = X^\mu \, ,
$$

which is easy enough.
We can reuse this trick by inserting the metric tensor into the other term and using the product rule, as follows:

$$
X_\lambda \partial^\mu X^\lambda
=
X_\lambda \left( \partial^\mu g^{\lambda \nu} X_\nu \right)
=
X_\lambda g^{\lambda \mu}
=
X^\mu \, .
$$

This means that, overall, we have
""")
                gradient_of_the_dot_product = c.Text(R"""
$$
\partial^\mu (X_\lambda X^\lambda) = 2X^\mu \, .
$$
""")
            c.Title.menu_title("Part c", level=3, parent=q1_title)
            c.Text(R"""
<blockquote>
$$
\partial^\mu \partial_\mu X^\nu X_\nu
$$
</blockquote>
""")
            c.Text("We can use the ")
            c.DropdownReference(
                ref=gradient_of_the_dot_product,
                text="gradient of the dot product",
            )
            c.Text(
                R"""
that we just derived to make this quite trivial.
"""
            )
            with c.Admonition.show_answer():
                c.Text(R"""
$$
\partial^\mu \partial_\mu X^\nu X_\nu
=
\partial_\mu \left[
    \partial^\mu \left(
        X^\nu X_\nu
    \right)
\right]
=
\partial_\mu \left(
    2X^\mu
\right)
=
8
$$
""")

            c.Title.menu_title("Part d", level=3, parent=q1_title)
            c.Text(R"""
<blockquote>
$$
\partial^\mu X^\nu
$$
</blockquote>

Once again, we're going to insert the metric tensor to get this one quite easily.
""")
            with c.Admonition.show_working():
                c.Text(R"""
$$
\partial^\mu X^\nu = g^{\mu \lambda} \partial_\lambda X^\nu = g^{\mu \nu}
$$
""")
            c.Title.menu_title("Part e", level=3, parent=q1_title)
            c.Text(
                R"""
<blockquote>
$$
\partial_\lambda F^\lambda
$$
</blockquote>
"""
            )
            c.Text("Subbing in the expression for the ")
            c.DropdownReference(
                ref=q1_field,
                text="four-vector field",
            )
            c.Text(" given in the problem, and once again using the ")
            c.DropdownReference(
                ref=gradient_of_the_dot_product,
                text="gradient of the dot product",
            )
            c.Text(", we get ")
            with c.Admonition.show_answer():
                c.Text(R"""
$$
\partial_\lambda F^\lambda
=
2 \partial_\lambda X^\lambda + K^\lambda \partial_\lambda (X^\nu X_\nu)
=
8 + 2K^\lambda X_\lambda
$$
""")
            c.Title.menu_title("Part f", level=3, parent=q1_title)
            c.Text(
                R"""
<blockquote>
$$
\partial^\mu \partial_\lambda F^\lambda
$$
</blockquote>

This is quite easy, because we did most of the work in the previous problem.
"""
            )
            with c.Admonition.show_answer():
                c.Text(R"""
$$
\partial^\mu \partial_\lambda F^\lambda
=
2 k^\lambda \partial^\mu X_\lambda
=
2 K^\mu
$$
""")
            c.Title.menu_title("Part g", level=3, parent=q1_title)
            c.Text(
                R"""
<blockquote>
$$
\partial^\mu \partial_\mu \sin \left( K_\lambda X^\lambda \right)
$$
</blockquote>

This one is a bit more tricky, but we've built up the tools we need to tackle it.
"""
            )
            with c.Admonition.show_working():
                c.Text(R"""
Let's start by applying the chain rule to the sine function, using only the first derivative.

$$
\partial^\mu \partial_\mu \sin \left( K_\lambda X^\lambda \right)
=
\partial^\mu \left[ \partial_\mu \left( K_\lambda X^\lambda \right) \cos \left( K_\lambda X^\lambda \right) \right]
$$

Now we finish taking the chain rule using the fact that $\partial_\mu X^\lambda = \delta^\lambda_\mu$.

$$
\partial^\mu \left[ \partial_\mu \left( K_\lambda X^\lambda \right) \cos \left( K_\lambda X^\lambda \right) \right]
=
\partial^\mu \left[ K_\mu \cos \left( K_\lambda X^\lambda \right) \right]
$$

That's the first derivative applied!
Now let's do it again.

$$
\partial^\mu \left[ K_\mu \cos \left( K_\lambda X^\lambda \right) \right]
=
-K_\mu \partial^\mu \left( K_\lambda X^\lambda \right) \sin \left( K_\lambda X^\lambda \right)
$$

Now we need to be a bit careful, because both indices are raised, so we need another metric tensor to lower coordinate $X$.

$$
-K_\mu \partial^\mu \left( K_\lambda X^\lambda \right) \sin \left( K_\lambda X^\lambda \right)
=
-K_\mu \partial^\mu \left( K_\lambda g^{\lambda \nu} X_\nu \right) \sin \left( K_\lambda X^\lambda \right)
=
-K_\mu K_\lambda g^{\lambda \mu} \sin \left( K_\lambda X^\lambda \right)
$$

And we made it!
Now we just apply the metric tensor to one of the $K$ vectors to get the final answer.

$$
\partial^\mu \partial_\mu \sin \left( K_\lambda X^\lambda \right)
=
-K_\mu K^\mu \sin \left( K_\lambda X^\lambda \right).
$$
""")
        return div
