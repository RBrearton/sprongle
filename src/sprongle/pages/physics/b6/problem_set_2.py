"""Define the problem set 2 page's main content."""

import numpy as np
import plotly.graph_objects as go
from nicegui import ui

from sprongle import components as c
from sprongle._sprongle_page import SpronglePage


def diatomic_dispersion(
    wavevector: np.ndarray,
    spring_const: float,
    mass_1: float,
    mass_2: float,
    interatomic_distance: float,
    *,
    is_optical: bool = False,
) -> np.ndarray:
    """Return the dispersion relation for a 1d diatomic chain."""
    # The prefactor of the whole expression.
    prefactor = spring_const / mass_1 / mass_2

    # We use plus for the optical branch and minus for the acoustic branch.
    plus_minus = 1 if is_optical else -1

    # Now produce the expression for the square of the dispersion relation.
    dispersion_sq = prefactor * (
        mass_1
        + mass_2
        + plus_minus
        * np.sqrt(
            (mass_1 + mass_2) ** 2
            - 4
            * mass_1
            * mass_2
            * np.sin(wavevector * interatomic_distance / 2) ** 2
        )
    )
    return np.sqrt(dispersion_sq)


def get_diatomic_dispersion_plot(mass_1: float, mass_2: float) -> go.Figure:
    """Return the diatomic dispersion plot."""
    # Prepare the parameters for the plot.
    interatomic_distance = 1
    spring_const = 1
    num_points = 10_000
    wavevectors = np.linspace(
        -np.pi / interatomic_distance, np.pi / interatomic_distance, num_points
    )

    # Calculate the dispersion relations.
    dispersion_acoustic = diatomic_dispersion(
        wavevectors,
        spring_const,
        mass_1,
        mass_2,
        interatomic_distance,
        is_optical=False,
    )

    # Also calculate the optical branch for the extended zone scheme.
    extended_wavevectors_1 = np.linspace(
        -2 * np.pi / interatomic_distance,
        -np.pi / interatomic_distance,
        num_points,
    )
    extended_wavevectors_2 = np.linspace(
        np.pi / interatomic_distance,
        2 * np.pi / interatomic_distance,
        num_points,
    )
    dispersion_optical_extended_1 = diatomic_dispersion(
        extended_wavevectors_1,
        spring_const,
        mass_1,
        mass_2,
        interatomic_distance,
        is_optical=True,
    )
    dispersion_optical_extended_2 = diatomic_dispersion(
        extended_wavevectors_2,
        spring_const,
        mass_1,
        mass_2,
        interatomic_distance,
        is_optical=True,
    )

    # Create the figure
    fig = go.Figure()

    # Add acoustic branch
    fig.add_trace(
        go.Scatter(
            x=wavevectors,
            y=dispersion_acoustic,
            mode="lines",
            name="acoustic",
            line={"color": "lightblue"},
        )
    )

    # Add the optical branch, if the masses are different.
    if mass_1 != mass_2:
        dispersion_optical = diatomic_dispersion(
            wavevectors,
            spring_const,
            mass_1,
            mass_2,
            interatomic_distance,
            is_optical=True,
        )
        fig.add_trace(
            go.Scatter(
                x=wavevectors,
                y=dispersion_optical,
                mode="lines",
                name="optical",
                line={"color": "orange"},  # Use a consistent color scheme
            )
        )

    # Add optical-extended-1 branch. Note that this is actually acoustic if the masses
    # are the same.
    legend_name = "optical-extended" if mass_1 != mass_2 else "also-acoustic"
    fig.add_trace(
        go.Scatter(
            x=extended_wavevectors_1,
            y=dispersion_optical_extended_1,
            mode="lines",
            name=legend_name,
            legendgroup=legend_name,
            line={"color": "powderblue", "dash": "dot"},
        )
    )

    # Add optical-extended-2 branch
    fig.add_trace(
        go.Scatter(
            x=extended_wavevectors_2,
            y=dispersion_optical_extended_2,
            mode="lines",
            name=legend_name,
            legendgroup=legend_name,
            showlegend=False,  # Hide the second legend entry
            line={"color": "powderblue", "dash": "dot"},
        )
    )

    # Update layout
    fig.update_layout(
        title="Diatomic Dispersion Relation",
        xaxis_title="Wavevector",
        yaxis_title="Frequency ω",
        template="plotly_dark",
    )

    # Make the figure always have a height of 1000 pixels.
    fig.update_layout(height=1000)
    return fig


class B6ProblemSet2(SpronglePage):
    """Define the B2 problem set 2 solutions page."""

    def __init__(self) -> None:  # noqa: D107
        super().__init__("physics")

    def make_content(self) -> ui.element:  # noqa: D102, PLR0915:
        with ui.element() as div:
            c.Title("B6 problem set 2", level=1)
            q1_title = c.Title.menu_title(
                "Q1: Chemical bonding", level=2, parent=self
            )
            c.Title.menu_title("Part a", level=3, parent=q1_title)
            c.Text(R"""
<blockquote>
Qualitatively describe the five different types of chemical bonds and why they occur.
</blockquote>

Just copy the table out of Steve Simon's "The Oxford Solid State Basics" book.
To avoid *direct* plagiarism, I won't copy the table here.
""")
            c.Title.menu_title("Part b", level=3, parent=q1_title)
            c.Text(R"""
<blockquote>
Describe qualitatively the phenomenon of Van der Waals forces.
Explain why the force is attractive and proportional to $1/R^7$.
</blockquote>

Van der Waals forces are the attractive forces between molecules.
They are caused by the fluctuating electric fields of the molecules.
We can get the $1/R^7$ dependence without thinking too hard - it's clear from dimensional analysis, so we don't need to remember exact forms of results from electrostatics.
""")
            with c.Admonition.show_working():
                c.Text(R"""
In the absence of external forces and fields, we don't expect atoms to be polarized.
If an electric field is applied, they will develop a polarization

$$
\vec{p} = \chi \vec{E},
$$

where $\chi$ is the polarizability.
Now imagine that we have two atoms separated by a distance $R$.
If the first atom develops, for whatever reason, a spontaneous polarization $\vec{p}_1=p_1 \hat{z}$, it will produce a field

$$
E \propto \frac{p_1}{R^3}
$$

at the location of the second atom.
The second atom will then develop a polarization $p_2 = \chi E$.
Just thinking about dimensions, the potential energy of this interaction has to be proportional to $p_1 p_2 / R^3$, so that

$$
V \propto \frac{1}{R^6}.
$$

So that the force is proportional to $1/R^7$.
                       """)
            c.Title.menu_title("Part c", level=3, parent=q1_title)
            c.Text(R"""
<blockquote>
The ionization energy of a sodium atom is 5.14 eV.
The electron affinity of a chlorine atom is 3.62 eV.
The bond length of a NaCl molecule is 2.36 Å.
Calculate the total energy released when a NaCl molecule is formed.

The actual experimental value is 4.26 eV.
Comment on the sign of your error.

</blockquote>
""")
            with c.Admonition.show_working():
                c.Text(R"""
The Coulomb energy of the NaCl molecule is

$$
U_\mathrm{coul} = -\frac{e^2}{4\pi\epsilon_0 R} = -\frac{e^2}{4\pi\epsilon_0 (2.36\, Å)} = 6.09 \, \mathrm{eV}.
$$

The energy released is then

$$
E_\mathrm{affinity} - E_\mathrm{ionization} + U_\mathrm{coul} = 3.62 - 5.14 + 6.09 = 4.58 \, \mathrm{eV}.
$$

This is too big!
There must be a repulsive force, and this repulsive force must be what's stopping the atoms from collapsing into each other.
This would be Pauli repulsion, which is not included in our simple model.
""")
            c.Title.menu_title(
                "Q2: Covalent bonding in detail", level=2, parent=self
            )
            c.Text(
                "I'll write this up if I find the time, as it's the only optional problem on the set."
            )
            q3_title = c.Title.menu_title(
                "Q3: Interatomic potentials", level=2, parent=self
            )
            c.Title.menu_title("Part a", level=3, parent=q3_title)
            c.Text(R"""
<blockquote>

Just thinking qualitatively, we expect the potential energy of a pair of atoms to look something like this:

TODO: inject a Lennard-Jones plotly plot here

This potential can be expanded about its minimum to give

$$
V(x) = \frac{\kappa}{2} (x - x_0)^2 + \frac{\kappa_3}{3!} (x - x_0)^3 + \ldots
$$

The Lennard-Jones potential is one such model with the correct qualitative shape (in fact, it's exactly what I plotted above).
Its functional form is

$$
V(x) = 4 \epsilon \left[ \left(\frac{\sigma}{x}\right)^{12} - \left(\frac{\sigma}{x}\right)^6 \right].
$$

What is the physical meaning of the exponent 6?

</blockquote>
""")
            with c.Admonition.show_working():
                c.Text(R"""
The exponent 6 comes from the fact that the Lennard-Jones potential is used to model Van der Waals interactions.
There are a few interesting things to note here:

- Lennard-Jones is one guy with a double-barrelled surname!
- If we wanted to study interactions in a crystal, we might want to use something like the [Morse potential](https://en.wikipedia.org/wiki/Morse_potential).
- The twelfth power is wrong. It models Pauli repulsion, which has a very different functional form. We keep it because it's extremely easy to square numbers with a computer, and we've already had to calculate the sixth power to get the attractive part of the potential! Really, any power greater than 6 would have worked, and we choose 12 for computational efficiency.""")
            c.Title.menu_title("Part b", level=3, parent=q3_title)
            c.Text(R"""
<blockquote>
Find $x_0$, $\kappa$, and $\kappa_3$ for the Lennard-Jones potential.
</blockquote>""")
            with c.Admonition.show_answer():
                c.Text(R"""
This is just algebra - Taylor expand the potential and compare coefficients.

$$
x_0 = 2^{\frac{1}{6}}\sigma,
~~~
\kappa = 36 \left( 2^{\frac{2}{3}} \frac{\epsilon}{ \sigma^2} \right),
~~~
\kappa _3 = - 756\sqrt{2} \frac{\epsilon}{\sigma^3}.
$$
""")
            q4_title = c.Title.menu_title(
                "Q4: Classical model of thermal expansion", level=2, parent=self
            )
            c.Text(R"""
<blockquote>

In classical statistical mechanics, the expectation of $x$ is

$$
\langle x \rangle _{\beta} = \frac{\int  x e^{-\beta V(x)} dx}{\int  e^{-\beta V(x)} dx}.
$$

We can't do those integrals with arbitrary $V(x)$, but we could expand the exponentials as

$$
e^{-\beta V(x)} = e^{\frac{\beta \kappa}{2} (x - x_0)^2} \left[ 1 + \frac{\beta \kappa_3}{3!} (x - x_0)^3 + \ldots \right],
$$

and let the limits of integration go to $\pm \infty$.

</blockquote>""")
            c.Title.menu_title("Part a", level=3, parent=q4_title)
            c.Text(R"""
<blockquote>

Why is this expansion of the exponent and extension of the limits of integration valid?

</blockquote>""")
            with c.Admonition.show_answer():
                c.Text(R"""
The *real* answer is that we do it because it's the only way to make progress.
You figure out what it means only if your results are interesting!

The answer that the question is probably looking for is that, if $k_B T$ is small, we're going to have a very peaked Boltzmann distribution, and the integrals will be dominated by the region around the minimum of the potential.

I hear you though - sure, that lets us expand the limits and write $V(x) \approx \frac{\kappa}{2} (x - x_0)^2 + \frac{\kappa_3}{3!} (x - x_0)^3 + \ldots$, but then why Taylor expand the exponential on the cubic part, and not the quadratic part?

I'll provide an exact bound on this on the last part of the question, but we're just requiring that the cubic term is appreciably smaller than the quadratic term.
""")
            c.Title.menu_title("Part b", level=3, parent=q4_title)
            c.Text(R"""
<blockquote>

Use this to derive $\langle x \rangle _{\beta}$ and show that the coefficient of thermal expansion is

$$
\alpha = \frac{1}{L} \frac{\partial L}{\partial T} = \frac{1}{x_0} \frac{k_B \kappa_3}{2 \kappa^2}.
$$

</blockquote>
""")
            with c.Admonition.show_working():
                c.Text(R"""
There are two important tricks here:

1. All odd integrals are 0 by symmetry
2. Shift all the integrals by $x_0$

Just applying the tricks above leaves us with

$$
\langle x \rangle _{\beta} = \left[\int^\infty_{-\infty} e^{\frac{\beta\kappa}{2} x^2}\left(x_0 + \frac{\beta \kappa_3}{3!} x^4 \right) dx \right]
/
\left[ {\int^\infty_{-\infty} e^{\frac{\beta\kappa}{2} x^2} dx}\right] \, .
$$

Now, evaluating the Gaussian integrals gives

$$
\langle x \rangle _{\beta} = x_0 + \frac{k_3 k_B T}{2 \kappa^2} + \ldots
$$

The coefficient of thermal expansion is then

$$
\alpha = \frac{1}{L} \frac{dL}{dT} = \frac{1}{x_0} \frac{k_B \kappa_3}{2 \kappa^2},
$$

as required.""")
            c.Title.menu_title("Part c", level=3, parent=q4_title)
            c.Text(R"""
<blockquote>
In what temperature range is the above expansion valid?
</blockquote>""")
            with c.Admonition.show_working():
                c.Text(R"""

Ok, now it's time to make the terms and conditions surrounding out approximation a bit more precise.

Rewriting our expression by Taylor expanding the cubic term, but not the quadratic term, is reasonable when""")
                approximation_conditions = c.Text(R"""
$$
\kappa_3 \Delta x \ll \kappa
$$""")
                c.Text(R"""
The typical energies that we'll access are on the order of

$$
k_B T = \frac{\kappa}{2}(x - x_0)^2 - \frac{\kappa_3}{3!} (x - x_0)^3 \, .
$$

If the third term is much smaller, as we require for our funky expansion to work, we have

$$
k_B T \approx \frac{\kappa}{2}(x - x_0)^2 = \frac{\kappa}{2} (\Delta x)^2 \, .
$$

Rearranging this gives us typical displacements on the order of

$$
\Delta x \approx \sqrt{\frac{2 k_B T}{\kappa}} \, .
$$""")
                c.Text("Subbing this back into the")
                c.DropdownReference(
                    "approximation condition", ref=approximation_conditions
                )
                c.Text(R"""
gives us

$$
\kappa_3^2 \frac{k_B T}{\kappa} \ll \kappa^2 \, ,
$$

and then, equivalently,

$$
k_B T \ll \frac{\kappa^3}{\kappa_3^2} \, .
$$""")
            c.Title.menu_title("Part d", level=3, parent=q4_title)
            c.Text(R"""
<blockquote>

This is valid for a 2-particle system, but not a many atom chain.
Why?
How would you modify the calculation to account for this?

</blockquote>""")
            with c.Admonition.show_answer():
                c.Text(R"""
Well... our potential only has a single distance between two atoms in it!
As a result, we're basically studying the properties of a bunch of non-interacting harmonic oscillators. (okay, anharmonic oscillators because of the cubic term, but you get the idea!)

To properly handle the many-atom chain, we need to account for the fact that the coupled differential equations that show up when we try to solve for the motion of the chain are going to lead to normal modes.
There will be some dispersion relation ($\omega(k)$) that tells us how the normal modes of the chain are going to behave as a function of wavevector $k$.

We can then think about thermally occupying these modes using Bose statistics, and calculate the average expansion of the chain as a function of temperature.""")
            q5_title = c.Title.menu_title(
                "Q5: Phonons on a one-dimensional monatomic chain",
                level=2,
                parent=self,
            )
            c.Title.menu_title("Part a", level=3, parent=q5_title)
            c.Text(R"""
<blockquote>

What is meant by a normal mode?
What is meant by a phonon?
Explain why phonons obey Bose-Einstein statistics.

</blockquote>""")
            with c.Admonition.show_answer():
                c.Text(R"""
For normal modes, quoting wikipedia:

*"A normal mode is a pattern of motion in which all parts of the system move sinusoidally with the same frequency and with a fixed phase relation."*

Phonons are quanta of vibration.

Phonons obey Bose-Einstein statistics because there's no reason to limit the number of phonons in a given mode.""")
            c.Title.menu_title("Part b", level=3, parent=q5_title)
            c.Text(R"""
<blockquote>

Derive the dispersion relation for longitudinal oscillations of a one dimensional chain of N identical atoms of mass $m$, lattice spacing $a$ and spring constant $\kappa$.

</blockquote>""")
            with c.Admonition.show_answer():
                c.Text("This is bookwork.")
                monatomic_phonon_dispersion = c.Text(R"""
$$
\omega = 2 \sqrt{\frac{\kappa}{m}} \left| \, \sin \left( \frac{ka}{2} \right) \right|
$$""")
            c.Title.menu_title("Part c", level=3, parent=q5_title)
            c.Text(R"""
<blockquote>

Show that the mode with wavevector $k$ has the same pattern of mass displacements as the mode with wavevector $k + 2 \pi / a$.
Show that the dispersion relation is periodic in $k$-space (reciprocal space).

How many *different* normal modes are there?

</blockquote>
""")
            with c.Admonition.show_working():
                c.Text(R"""

The first part is just a matter of plugging in $k + 2 \pi / a$ into the dispersion relation.
It's a trig function...

The second part only requires a small amount of algebra.""")
                state_spacing = c.Text(R"""
From periodic boundary conditions, we have

$$
e^{i(\omega t + kna)} = e^{i(\omega t + k(n+N)a)} \, ,
$$

which immediately requires that

$$
e^{i k N a} = 1 \, .
$$

This means that $kNa = 2\pi p$, where $p$ is an integer.
Or, equivalently,

$$
k = \frac{2\pi p}{Na} \, .
$$

This means that the spacing between adjacent $k$ states is

$$
\Delta k = \frac{2\pi}{Na} \, .
$$""")
                c.Text(R"""
Noting that $L = Na$, that means $\Delta k = 2\pi / L$.

We get the number of modes by diving the range of $k$ by the spacing between adjacent $k$ states, so

$$
N = \frac{\mathrm{range}}{\mathrm{spacing}} = \frac{2\pi/a}{2\pi/L} = L/a = N \, .
$$

So... Debye's fudge was correct!
""")
            c.Title.menu_title("Part d", level=3, parent=q5_title)
            c.Text(R"""
<blockquote>

- Derive the phase and group velocities and sketch them as a function of $k$.
- What is the sound velocity?
- Show that the sound velocity is given by $v_s = \sqrt{\beta^{-1}/\rho}$, where $\rho$ is the mass density and $\beta$ is the compressibility.

</blockquote>""")
            with c.Admonition.show_working():
                c.Text(R"""
Okay, there are a few small things to show here, so let's get to it.
We get the group velocity by differentiating the""")
                c.DropdownReference(
                    "dispersion relation", ref=monatomic_phonon_dispersion
                )
                c.Text(R"""
with respect to $k$:

$$
v_g = \frac{d\omega}{dk} = a \sqrt{\frac{\kappa}{m}} \cos \left( \frac{ka}{2} \right) \mathrm{sgn}(k) \, .
$$

Be careful about differentiating modulus functions!
The sgn function is 1 for positive $k$ and -1 for negative $k$.

The phase velocity is simply

$$
v_p = \frac{\omega}{k} =\frac {2}{k} \sqrt{\frac{\kappa}{m}} \left| \, \sin \left( \frac{ka}{2} \right) \right| \, .
$$

The sound velocity is just the group velocity at $k=0$, so

$$
v_s = a \sqrt{\frac{\kappa}{m}} \, .
$$""")
                c.Text(R"""
To show the final part, we just need an expression for the compressibility.
The compressibility is defined as""")
                compressibility = c.Text(R"""
$$
\beta = -\frac{1}{L} \frac{\partial L}{\partial F} \, .
$$""")
                c.Text(R"""
We can consider the interatomic distances of atoms in the chain as a function of the force applied:

$$
x(F) = a - \frac{F}{\kappa} \, .
$$

This gives us $L = N x(F)$, which we can differentiate to get

$$
\frac{\partial L}{\partial F} = -\frac{N}{\kappa} \, .
$$""")
                c.Text("This means that the")
                c.DropdownReference("compressibility", ref=compressibility)
                c.Text("is")
                c.Text(R"""
$$
\beta = \frac{1}{L} \frac{N}{\kappa} = \frac{1}{\kappa a} \, .
$$

Using the fact that $\rho = m / a$, we finally get

$$
v_s = \sqrt{\frac{1}{\beta \rho}} = a \sqrt{\frac{\kappa}{m}} \, .
$$""")
            c.Title.menu_title("Part e", level=3, parent=q5_title)
            c.Text(R"""
<blockquote>
Calculate and sketch the density of states per frequency $g(\omega)$.
</blockquote>""")
            with c.Admonition.show_working():
                c.Text("The density of states is")
                density_of_states = c.Text(R"""
$$
g(\omega) = \frac{dN}{d\omega} = \frac{dN}{dk} \frac{dk}{d\omega}
$$""")
                c.Text(R"""

The rest of the problem is just being careful with the algebra, wavevector degeneracy etc. ($+k$ and $-k$ have the same $\omega$, which gives an extra factor of 2).

Subbing in the expression for the""")
                c.DropdownReference(
                    "dispersion relation", ref=monatomic_phonon_dispersion
                )
                c.Text("into the")
                c.DropdownReference("density of states", ref=density_of_states)
                c.Text(R"""
gives

$$
\frac{dN}{dk} \frac{dk}{d\omega}
=
\frac{2 Na}{2\pi a \sqrt{\kappa / m} \cos({ka/2})} = \frac{Na}{2\pi v_g}
$$""")
                c.Text(R"This is a function of $k$, so we just need to use our")
                c.DropdownReference(
                    "dispersion relation", ref=monatomic_phonon_dispersion
                )
                c.Text(R"""
to swap out $k$ for $\omega$.
Doing this gives

$$
g(\omega) = \frac{N}{\pi\sqrt{\kappa/m - (\omega/2)^2}} \, .
$$""")
            c.Title.menu_title("Part f", level=3, parent=q5_title)
            c.Text(R"""
<blockquote>
Write an expression for the heat capacity of this chain.
You will get an integral that you can't do analytically.
</blockquote>""")
            with c.Admonition.show_working():
                c.Text(R"""
Since the wording of the question is so vague, I'd actually recommend not substituting in the expression for the density of states.""")
                phonon_heat_capacity = c.Text(R"""
The internal energy is

$$
U = \int g(\omega) \hbar \omega \left( \frac{1}{e^{\hbar \omega / k_B T} - 1} \right) d\omega \, .
$$

The heat capacity is then just $C = \frac{dU}{dT}$, which we may/may not be able to do depending on the form of $g(\omega)$.
""")
            c.Title.menu_title("Part g", level=3, parent=q5_title)
            c.Text(R"""
<blockquote>
Show that, at high temperature, the law of Dulong and Petit is obeyed.
</blockquote>""")
            with c.Admonition.show_working():
                c.Text(R"""

We can do this quite easily because we didn't substitute in the expression for the density of states.

Using our""")
                c.DropdownReference(
                    "expression for the heat capacity", ref=phonon_heat_capacity
                )
                c.Text(R"""
we just need to Taylor expand the exponential in the integrand to get

$$
C = \partial _T \int d\omega\, g(\omega) k_B T = N k_B \, .
$$

where we used the fact that $g(\omega) = dN/d\omega$ and we cancelled the $d\omega$ terms ;).
""")
            q6_title = c.Title.menu_title(
                "Q6: Phonons on a one-dimensional diatomic chain",
                level=2,
                parent=self,
            )
            c.Title.menu_title("Part a", level=3, parent=q6_title)
            c.Text(R"""
<blockquote>
What's the difference between an acoustic and an optical mode?
</blockquote>""")
            with c.Admonition.show_answer():
                c.Text(R"""
Acoustic modes are modes where adjacent atoms move in phase.
Optical modes are modes where adjacent atoms move out of phase.
""")
            c.Title.menu_title("Part b", level=3, parent=q6_title)
            c.Text(R"""
<blockquote>
Derive the longitudinal dispersion relation $\omega(k)$ for a one-dimensional diatomic chain of atoms of masses $m_1$ and $m_2$, lattice spacing $a$, and spring constant $\kappa$.
</blockquote>""")
            with c.Admonition.show_answer():
                c.Text(
                    "Not quite bookwork, but not far off, as a very similar problem is solved in the book."
                )
                diatomic_phonon_dispersion = c.Text(R"""
$$
\omega^2 = \frac{\kappa}{m_1 m_2}\left[(m_1 + m_2) \pm \sqrt{(m_1 + m_2)^2 - 4 m_1 m_2 \sin^2 \left( \frac{ka}{2} \right)}\right]
$$""")
            c.Title.menu_title("Part c", level=3, parent=q6_title)
            c.Text(R"""
<blockquote>

Determine the frequencies of the acoustic and optical modes at $k=0$, as well as at the Brillouin zone boundary.

Determine the sound velocity.

Show that the group velocity is zero at the Brillouin zone boundary.

Show that the sound velocity is again given by $v_s = \sqrt{\beta^{-1}/\rho}$.

</blockquote>

Let's start by plotting the dispersion relation, to get a feel for what's going on.""")
            ui.plotly(get_diatomic_dispersion_plot(1, 2))
            with c.Admonition.show_working():
                c.Text(
                    "There are a few things to get on with here, but it's all just plugging in numbers to the"
                )
                c.DropdownReference(
                    "dispersion relation", ref=diatomic_phonon_dispersion
                )
                c.Text("that we derived in the last part.")
                c.Text(r"""
As we can see from the plot, for the acoustic mode $\omega(k=0) = 0$.
Subbing in $k=0$ into the
""")
                c.DropdownReference(
                    "dispersion relation", ref=diatomic_phonon_dispersion
                )
                c.Text(R"""
gives

$$
\omega(k=0) = \sqrt{\frac{2\kappa(m_1 + m_2)}{m_1 m_2}}
$$

Now, evaluating the dispersion relation at the Brillouin zone boundary gives

$$
\omega^2(k=\frac{\pi}{a}) = \frac{\kappa}{m_1 m_2} \left(m_1 + m_2 \pm (m_1 - m_2)\right) \, ,
$$

which gives us two distinct modes at the Brillouin zone boundary

$$
\omega_1 = \sqrt{\frac{2\kappa }{m_1}} \, , ~~~ \omega_2 = \sqrt{\frac{2\kappa }{ m_2}} \, .
$$""")
                c.Text(R"""
Now let's look at the sound velocity.
This is just the group velocity at $k=0$.
The trick here is to make $k$ small *before* taking the derivative, so replace $\sin^2\left(\frac{ka}{2}\right)$ with $\left(\frac{ka}{2}\right)^2$ in the""")
                c.DropdownReference(
                    "dispersion relation", ref=diatomic_phonon_dispersion
                )
                c.Text(R"""
, and you end up with

$$
\omega = ka\sqrt{\frac{\kappa}{2(m_1 + m_2)}} \, ,
$$

where we've of course taken the acoustic branch.
This means that the sound velocity is

$$
v_s = a\sqrt{\frac{\kappa}{2(m_1 + m_2)}} \, .
$$

Now we need to show that the group velocity is zero at the Brillouin zone boundary.
This is obvious from the plot - however we change the values of $m_1$ and $m_2$, so long as they're different, the dispersion relation flattens out at the Brillouin zone boundary.

Doing this mathematically is as simple as expanding the dispersion relation around $k=\pi/a$, and showing that it's quadratic in $k$.
This is pretty clear from the fact that we're basically expanding $\sin{x}$ around $\pi/2$, where it's stationary.

Finally, we need to show that the sound velocity is given by $v_s = \sqrt{\beta^{-1}/\rho}$ again.
This time, we have

$$
\rho = \frac{m_1 + m_2}{a} \, ,
$$

and

$$
\beta = -\frac{1}{L} \frac{\partial L}{\partial F} = \frac{2}{\kappa a}
$$

as the compressibility of 2 sprigs in series is half the compressibility of a single spring.
This gives us once again

$$
\sqrt{\frac{1}{\beta \rho}} = a\sqrt{\frac{\kappa}{2(m_1 + m_2)}} = v_s \, .
$$""")
            c.Title.menu_title("Part d", level=3, parent=q6_title)
            c.Text(R"""
<blockquote>

Sketch the dispersion in both the reduced and the extended zone scheme.

If there are $N$ unit cells, how many different normal modes are there?

How many branches of excitation are there? In other words, how many excitations are there at each $k$ in the reduced zone scheme?

</blockquote>
""")
            with c.Admonition.show_answer():
                c.Text(R"""
Well, I already plotted the dispersion relation, so... see above!
If there are $N$ unit cells, there are $2N$ different normal modes, because there are two atoms per unit cell and so $2N$ degrees of freedom.

As for the branches, there are two branches of excitation at each $k$ in the reduced zone scheme (see the plot).
This is because there's two atoms in the unit cell.

If we had 3 atoms in the unit cell, we'd have 3 branches of excitation at each $k$ in the reduced zone scheme.
One of these branches would be acoustic, and the other two would be optical.
We could never have more than 1 acoustic mode, because there's only one way to make all the atoms move in phase.""")
            c.Title.menu_title("Part e", level=3, parent=q6_title)
            c.Text(R"""
<blockquote>
What happens when $m_1 = m_2$?
</blockquote>""")
            with c.Admonition.show_answer():
                c.Text(R"""
The optical modes disappear, as the two atoms are indistinguishable.
The gap between the acoustic and optical modes at the Brillouin zone boundary closes.
The new lattice constant is $a/2$.
We have one mode per $k$, but our Brillouin zone is now twice as big, so the total number of modes is the same (as we haven't gained or lost any degrees of freedom).

You can play around with the plot to see this in action.""")
            q7_title = c.Title.menu_title(
                "Q7: The tight-binding model",
                level=2,
                parent=self,
            )
            c.Title.menu_title("Part a", level=3, parent=q7_title)
            c.Text(R"""
<blockquote>

Derive and sketch the dispersion relation for a monatomic one-dimensional chain with hopping integral $-t$, and on-site energy $\epsilon$.

How many different eigenstates are there in the system?

What is the effective mass of the electron near the bottom of the band?

What's the density of states?

If each atom is monovalent, what's the density of states at the Fermi surface?

Estimate the heat capacity at low temperature.

What's the heat capacity if the material is divalent?

What's the spin susceptibility if the material is divalent?

</blockquote>""")
            with c.Admonition.show_answer():
                c.Text(R"""
The derivation of the dispersion relation is covered nicely in Steve Simon's book - I'd recommend following that.
I'm not going to include the plot, because it's just a cosine function.
The dispersion relation that we should derive is""")

                tight_binding_dispersion = c.Text(R"""
$$
E = \epsilon - 2t \cos(ka)
$$""")
            c.Text(R"""
There are $N$ wavevector eigenstates, so, including spin, there are $2N$ eigenstates in the system.

Let's calculate the density of states.""")
            with c.Admonition.show_working():
                c.Text(R"""
Let's search for $g(E)$, the density of states per energy.
Using the""")
                c.DropdownReference("spacing between states", ref=state_spacing)
                c.Text(R"""
gives us

$$
g(E) = \frac{dN}{dk} \frac{dk}{dE} = 4\, \frac{Na}{2\pi} \frac{dk}{dE} \, ,
$$""")
                c.Text(R"""
where the factor of 4 comes from the spin degeneracy, and the fact that both $k$ and $-k$ give the same energy.
We can then differentiate the""")
                c.DropdownReference(
                    "dispersion relation", ref=tight_binding_dispersion
                )
                c.Text(R"""to get""")
                c.Text(R"""
$$
g(E) = \frac{N}{\pi t} \frac{1}{\sqrt{1 - \left(\frac{E - \epsilon}{2t}\right)^2}} \, .
$$""")
            c.Text(R"""
To figure out the density of states at the Fermi energy, we need to understand that a monovalent atom would exactly half-fill the band, as there are a total of $2N$ states that can be occupied by electrons.""")
            c.Text(R"""
That means that the highest occupied state is at $k =\pm \frac{\pi}{2a}$.
Subbing this into the""")
            c.DropdownReference(
                "dispersion relation", ref=tight_binding_dispersion
            )
            c.Text(R"""gives us""")
            with c.Admonition.show_answer():
                fermi_surface_density_of_states = c.Text(R"""
$$
g(E_F) = \frac{N}{\pi t} \, .
$$""")
            c.Text(R"""
To estimate the heat capacity at low temperature, we should remember from last week that, for an electron gas, the heat capacity per particle is

$$
C = \gamma k_B^2 g(E_F) T \, ,
$$

where $\gamma$ is a constant of order unity.""")
            with c.Admonition.show_answer():
                c.Text(
                    "To solve the problem, all we need to do is sub in our expression for the "
                )
                c.DropdownReference(
                    "density of states at the Fermi surface",
                    ref=fermi_surface_density_of_states,
                )
                c.Text(R"""
to get

$$
C = \gamma k_B^2 \frac{N}{\pi t} T \, .
$$""")
            c.Text(R"""
Finally, if the material is divalent, the band will be completely filled.
This means that the heat capacity will be very large at low temperatures, and the spin susceptibility will be very small, because there are no states available for electrons to move into.""")

        return div
