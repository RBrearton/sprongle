"""Define the problem set 2 page's main content."""

from nicegui import ui

from sprongle import components as c
from sprongle._sprongle_page import SpronglePage


class B2ProblemSet4(SpronglePage):
    """Define the B2 problem set 3 page."""

    def __init__(self) -> None:  # noqa: D107
        super().__init__("physics")

    def make_content(self) -> ui.element:  # noqa: D102, PLR0915:
        with ui.element() as div:
            c.Title("B2 problem set 4", level=1)
            c.Title.menu_title(
                "Q1: Sticky collision",
                level=2,
                parent=self,
            )
            c.Text(R"""
A particle of rest mass $m$ and kinetic energy $mc^2$ strikes a stationary
particle of rest mass $2m$ and combines with it while still conserving energy
and momentum. Find the rest mass and speed of the composite particle.
""")
            with c.Admonition.show_working():
                c.Text(R"""
The incident particle has

$$
E = 4mc^2 \,, ~~~ p^2 c^2 = E^2 - (mc^2)^2 = 15m^2 c^4 \,.
$$

Meanwhile, the 4-momentum of the target is $\left(2m c, 0\right)$.
This means that the final 4-momentum is $\left(6m c, p\right)$, where $p = \sqrt{15} m c$.
The rest mass of the final particle is then

$$
M_f = \sqrt{(6m)^2 - 15m^2} = \sqrt{21} m
$$

The speed is given by

$$
\beta = \frac{p}{E} = \frac{\sqrt{15}}{6}
$$
""")
            c.Title.menu_title(
                "Q2: Pair production",
                level=2,
                parent=self,
            )
            c.Text(R"""
Two photons may collide to produce an electron-positron pair.
If one photon has energy $E_0$ and the other has energy $E$, find the
threshold value of $E$ for this reaction, in terms of $E_0$ and the electron
rest mass $m$.
""")
            with c.Admonition.show_working():
                c.Text(R"""
From 4-momentum conservation $P^\mu_0 + P^\mu = P^\mu_+ + P^\mu_-$, squaring
both sides (and staying in energy units for convenience), we can evaluate the
left side in the lab frame, and the right side in the CM frame.
For the left side, $P^\mu_0 = (E_0, E_0)$ and $P^\mu = (E, -E)$, so

$$
P^\mu_0 + P^\mu = (E_0 + E, E_0 - E)
$$

and

$$
(P^\mu_0 + P^\mu)^2 = -4E_0E.
$$

On the right side, we have

$$
-4m^2c^4.
$$

Therefore

$$
E = \frac{m^2c^4}{E_0}.
$$
""")
            c.Text(R"""
High energy photons of galactic origin pass through the cosmic microwave
background radiation, which can be regarded as a gas of photons of energy
$2.3 \times 10^{-4} \, \text{eV}$. Calculate the threshold energy of the
galactic photons for the production of electron-positron pairs.
""")
            with c.Admonition.show_answer():
                c.Text(R"""
$$
E = 1.14 \times 10^{15} \, \text{eV}
$$""")
            q3_title = c.Title.menu_title(
                "Q3: Two-body decay",
                level=2,
                parent=self,
            )
            c.Text(R"""
A particle with known rest mass $M$ and energy $E$ decays into two products with
known rest masses $m_1$ and $m_2$. Find the energies $E_1$ and $E_2$ (in the
lab frame) of the products, by the following steps:
""")
            c.Title.menu_title("Part a", level=3, parent=q3_title)
            c.Text(R"""
Find the energies $E'_1$ and $E'_2$ of the products in the CM frame.
""")
            with c.Admonition.show_working():
                c.Text(R"""
In the CM frame, $P^\mu = (Mc, 0)$.
From 4-momentum conservation, we have $P^\mu_1 = P^\mu - P^\mu_2$, from which we obtain

$$
-m_1^2 c^2 = -M^2 c^2 - m_2^2 c^2 - 2 P^\mu (P_2)_{\mu} = -M^2 c^2 - m_2^2 c^2 + 2 M E_2
$$

$$
E'_2 = \frac{1}{2M} \left( -m_1^2 + M^2 + m_2^2 \right) c^2 = \frac{M^2c^2 + m_2^2c^2 - m_1^2 c^2}{2M}
$$

and similarly

$$
E'_1 = \frac{M^2c^2 + m_1^2c^2 - m_2^2 c^2}{2M}
$$
""")
            c.Title.menu_title("Part b", level=3, parent=q3_title)
            c.Text(R"""
Show that the momentum of either decay product in the CM frame is

$$
p = \frac{c}{2M} \left[ (m_1^2 + m_2^2 - M^2)^2 - 4 m_1^2 m_2^2 \right]^{1/2}
$$""")
            with c.Admonition.show_answer():
                c.Text(R"""
$$
p'^2 = \frac{(E'_1)^2}{c^2} - m_1^2 c^2 = \frac{1}{4M^2} \left[ (m_1^2 + m_2^2 - M^2)^2 - 4 m_1^2 m_2^2 \right] c^2
$$
""")
            c.Title.menu_title("Part c", level=3, parent=q3_title)
            c.Text(R"""
Find the Lorentz factor and the speed $v$ of the CM frame relative to the lab.
""")
            with c.Admonition.show_answer():
                c.Text(R"""
The Lorentz factor is simply $\gamma = \frac{E}{Mc^2}$, and the speed

$$
\beta = \sqrt{1 - \frac{M^2 c^4}{E^2}}
$$
""")
            c.Title.menu_title("Part d", level=3, parent=q3_title)
            c.Text(R"""
Write down, in terms of $v$, $\gamma$, $p$, $E'_1$ and $E'_2$, expressions for
$E_1$ and $E_2$ when the products are emitted (1) along the line of flight, and
(2) at right angles to the line of flight in the CM frame.""")
            with c.Admonition.show_working():
                c.Text(R"""
(1) Along the line of flight,

$$
E_1 = \gamma \left( E'_1 - \beta p'_1 c \right)
$$

$$
E_2 = \gamma \left( E'_2 + \beta p'_2 c \right)
$$

(2) emitted at right angles to the CM line of flight, $p'_\parallel = 0$, so

$$
E_1 = \gamma E'_1 \quad \text{and} \quad E_2 = \gamma E'_2.
$$
""")
            q4_title = c.Title.menu_title(
                "Q4: Motion in an electromagnetic field",
                level=2,
                parent=self,
            )
            c.Text(R"""
Consider a particle with mass $m$ and charge $q$ moving in a constant electric
field $\vec{E} = E \hat{x}$ and magnetic field $\vec{B} = B \hat{y}$ in
an inertial frame (S).
""")
            c.Title.menu_title("Part a", level=3, parent=q4_title)
            c.Text(R"""
Consider a frame (S') moving with velocity $\vec{v} = v \hat{z}$ relative
to (S). Write the fields $\vec{E'}$ and $\vec{B'}$ in this frame in terms
of $\vec{E}$, $\vec{B}$, and $\vec{v}$. Calculate $\vec{v}$
corresponding to $\vec{E'} = 0$ in (S') and show that this leads
to $\vec{B'} = \frac{\vec{B}}{\gamma_v}$, where
$\gamma_v = \left( 1 - \frac{v^2}{c^2} \right)^{-1/2}$.
What condition must the fields satisfy for such a frame to exist?
""")
            with c.Admonition.show_working():
                c.Text(R"""
The fields in frame (S') are related to those in frame (S) by the transformations:""")
                electric_field_transformation = c.Text(R"""
$$
\vec{E'}_{\parallel} = \vec{E}_{\parallel}, \quad \vec{E'}_{\perp} = \gamma_v \left( \vec{E}_{\perp} + \vec{v} \times \vec{B} \right),
$$""")
                magnetic_field_transformation = c.Text(R"""
$$
\vec{B'}_{\parallel} = \vec{B}_{\parallel}, \quad \vec{B'}_{\perp} = \gamma_v \left( \vec{B}_{\perp} - \frac{\vec{v} \times \vec{E}}{c^2} \right),
$$""")
                c.Text(R"""
where the subscripts $\parallel$ and $\perp$ denote components parallel and perpendicular to the velocity $\vec{v}$, respectively. Since $\vec{v}$ and $\vec{E}$ are orthogonal, $\vec{E}_{\parallel}$ and thus $\vec{E'}_{\parallel}$ equal zero. For $\vec{E'}_{\perp}$ to vanish, we require $\vec{E}_{\perp} + \vec{v} \times \vec{B} = \vec{E} + \vec{v} \times \vec{B} = 0$, which gives:

$$
\vec{v} = \frac{\vec{E} \times \vec{B}}{B^2} = \frac{\vec{E}}{B} \hat{z}.
$$

Since $\vec{B}_{\parallel}$, and thus $\vec{B'}_{\parallel}$, equal zero, we have:

$$
\vec{B'}_{\perp} = \vec{B'}_{\perp} = \gamma_v \left( \hat{B} \vec{B} - \frac{\vec{v} \times \vec{E}}{c^2} \right) = \gamma_v \left( \vec{B} - \frac{B v^2}{c^2} \right) \hat{y} = \frac{\vec{B}}{\gamma_v}.
$$

This transformation is only possible if $v < c$, which requires $\frac{E}{B} < c$.

Another way to approach this is by considering the invariance of the electromagnetic field's Lagrangian density, $\mathcal{L}$. It is given by:

$$
\mathcal{L} = \frac{\epsilon_0 E^2}{2} - \frac{B^2}{2 \mu_0}.
$$

If there exists a frame in which there is only a magnetic field, then $\mathcal{L} < 0$. This condition ensures that in any other frame, $\frac{E}{B} < c$.
""")
            c.Title.menu_title("Part b", level=3, parent=q4_title)
            c.Text(R"""
We assume this condition is satisfied.
The particle has a velocity $u$ in frame (S) with no initial component along the $y$-axis.
Write the equation of the trajectory in frame (S') and, from this, establish the parametric equations for the trajectory in (S), using the time $t'$ in (S') as the parameter.
Discuss the nature of the trajectory.
""")
            with c.Admonition.show_working():
                c.Text(R"""
In frame (S'), the particle is subject only to the magnetic field $\vec{B'}$.
Its initial velocity in frame (S) is $\vec{u}_0 = u_{0x} \hat{x} + u_{0z} \hat{z}$,
which corresponds to $u_{0x} \hat{x} + u'_{0z} \hat{z}$ in (S'), as the velocity
components along $x$ and $y$ are preserved.
Thus, in frame (S'), as shown in Question 4 of Problem Set 3, the particle moves with uniform velocity along circular trajectories in the $(x', z')$-plane:

$$
x' = A \cos \omega' t', \quad y' = 0, \quad z' = A \sin \omega' t',
$$

with $\omega' = \left| q \right| B' / (\gamma_{v'} m)$,
where $\gamma_{v'} = \left( 1 - \frac{u^2}{c^2} \right)^{-1/2}$ and $u'$ is the
(constant) velocity of the particle in frame (S'). We have $A^2 \omega'^2 = u'^2$.
Transforming to frame (S), we obtain:

$$
x = x' = A \cos \omega' t', \quad y = y' = 0, \quad z = \gamma_v \left( z' + v t' \right) = \gamma_v \left( A \sin \omega' t' + v t' \right).
$$

Without the electric field $\vec{E}$, the trajectory would simply be a circle
in the $(x, z)$ plane.
However, the presence of $\vec{E}$ introduces a drift of the particle with
velocity $\vec{v} \times \vec{E} \times \vec{B} / B^2$.
""")
            c.Title.menu_title("Part c", level=3, parent=q4_title)
            c.Text(R"""
Assume now that the condition required for the existence of a frame
with $\vec{E'} = 0$ is not satisfied. Instead, demonstrate that there exists a
frame (S') where $\vec{B'} = 0$. Describe the motion of a particle that is
initially at rest in this frame (S').
""")
            with c.Admonition.show_working():
                c.Text(R"""
In this case, we have $E/B > c$. """)
                c.Text("Looking at the")
                c.DropdownReference(
                    "magnetic field transformations",
                    ref=magnetic_field_transformation,
                )
                c.Text(R"""
for $\vec{B'}_{\perp}$ to vanish, the condition $\vec{B'}_{\perp} - \vec{v} \times \vec{E}/c^2 = \vec{B} - \vec{v} \times \vec{E}/c^2 = 0$ must hold. This leads to:

$$
\vec{v} = \frac{c^2 \vec{E} \times \vec{B}}{E^2} = \frac{c^2 \vec{B}}{E} \hat{z}.
$$

Since $E/B > c$, we verify that $v < c$.""")
                c.Text("Now using the")
                c.DropdownReference(
                    "electric field transformations",
                    ref=electric_field_transformation,
                )
                c.Text(R"""
the electric field in frame (S') is given as:

$$
\vec{E'}_{\perp} = \vec{E}_{\perp} = \gamma_v \left( \vec{E} - \frac{\vec{E} v^2}{c^2} \right) \hat{x} = \frac{\vec{E}}{\gamma_v}.
$$

In frame (S'), the particle is subject only to the constant electric field $\vec{E'}$. As shown in Question 4 of Problem Set 3, the particle undergoes hyperbolic motion in the $(x', c t')$-spacetime. If the particle is initially at rest at the origin, its motion is described as:

$$
x' = \frac{c^2}{\alpha'} \left( \sqrt{1 + \frac{\alpha'^2 t'^2}{c^2}} - 1 \right),
$$
$$
y' = 0, \quad z' = 0,
$$

where $\alpha' = \frac{q \vec{E'}}{m}$.

Transforming this motion back into frame (S), we obtain:

$$
x = x', \quad y = y' = 0, \quad z = \gamma_v v t'.
$$
""")
            c.Title.menu_title(
                "Q5: Interactions between two charged beams in a magnetic field",
                level=2,
                parent=self,
            )
            c.Text(R"""
A pair of parallel particle beams separated by a distance $d$ have the same uniform charge per unit length $\lambda$. In the laboratory frame, a magnetic field is applied with a direction and strength just sufficient to overcome the repulsion between the beams, so that they both propagate in a straight line at constant speed $v$. Find the size $B$ of this magnetic field, by both of the following methods:
""")
            c.Title.menu_title("Part a", level=3, parent=q4_title)
            c.Text("Do the whole calculation in the lab frame.")
            with c.Admonition.show_working():
                c.Text(R"""
The electric field of one line charge at the other is $\frac{\lambda}{2 \pi \epsilon_0 d}$. The magnetic field of one line at the other is $B_\lambda = \mu_0 \lambda v / 2 \pi d$. The configuration is such that the electric force is repulsive, and the magnetic force is attractive, so the total force on any given charge in one of the beams is

$$
f = qE - qv \left( B_\lambda + B \right)
$$

(since velocity is perpendicular to the field).
Setting $f = 0$ gives

$$
B = \frac{E}{v} - B_\lambda = \frac{\lambda}{2 \pi \epsilon_0 d v} \left( 1 - \frac{v^2}{c^2} \right).
$$
""")
            c.Title.menu_title("Part b", level=3, parent=q4_title)
            c.Text(R"""
Start with a calculation of the force exerted by either beam on a particle in the
other, in the rest frame of the beams. Transform this force to the laboratory frame
and hence deduce the required $B$ field in that frame. What form does the
externally applied field take in the rest frame of the beams?
""")
            with c.Admonition.show_working():
                c.Text(R"""
In the rest frame, the charge per unit length is $\lambda_0 = \lambda / \gamma$ (i.e., smaller—in the other frame it gets enhanced by contraction).
The distance between the beams is the same. The force on a charge in either beam is

$$
\frac{q \lambda}{\gamma 2 \pi \epsilon_0 d} + q E_0 = 0
$$

where $E_0$ is the electric part of the applied field.
This gives the size of $E_0$. Now transform it to the other frame: it there gives $B$ and also an electric field.
However, the latter is zero, so the applied field must include a magnetic contribution $B_0$ in the rest frame.
From the field transformation we then have

$$
\gamma (E_0 + v B_0) = 0, \quad B = \gamma \left( B_0 + \frac{v E_0}{c^2} \right)
$$

where we used that everything is mutually perpendicular. Using the first, $B_0 = -E_0 / v$; putting this in the second we have

$$
B = \gamma \frac{-E_0}{v} \left( 1 - \frac{v^2}{c^2} \right) = \frac{\lambda}{2 \pi \epsilon_0 d v} \left( 1 - \frac{v^2}{c^2} \right)
$$

which is the same result as before.""")
            q6_title = c.Title.menu_title(
                "Q6: Covariant generalisation of Ohm's law",
                level=2,
                parent=self,
            )
            c.Text(R"""
Consider a conductor moving with velocity $\vec{v}$ relative to an inertial reference frame (S).""")
            ohms_law = c.Text(R"""
The covariant generalisation of Ohm's law is expressed as:

$$
J^\mu + \frac{1}{c^2} (U_\nu J^\nu) U^\mu = \sigma_0 F^{\mu \nu} U_\nu,
$$""")
            c.Text(R"""
where $U^\mu = (\gamma_v c, \gamma_v \vec{v})$ is the 4-velocity of the conductor and $J^\mu = (\rho c, \vec{j})$ is the 4-current of the charges in the conductor, with $\rho$ and $\vec{j}$ representing the charge density and current as measured in (S).
The tensor $F^{\mu \nu}$ describes the electromagnetic field in frame (S) and $\sigma_0$ is a scalar which is invariant.
""")
            c.Title.menu_title("Part a", level=3, parent=q6_title)
            c.Text(R"""
Show that this equation reduces to $j_0 = \sigma_0 E_0$ in the rest frame of the conductor, where the subscript '0' denotes quantities in that frame.
This establishes $\sigma_0$ as the conductivity in the rest frame.
""")
            with c.Admonition.show_working():
                c.Text(R"""
In the rest frame of the conductor, the 4-velocity is $U^\mu = (c, 0)$ and the 4-current is $J^\nu = (\rho_0 c, j_0)$. Consequently, $U_\nu J^\nu = - \rho_0 c^2$ and $F^{\mu\nu} U_\nu = - c F^{\mu 0}$.
""")
                c.Text("Now using the expression for")
                c.DropdownReference("Ohm's law", ref=ohms_law)
                c.Text(R"""and setting $\mu = 0$ gives $\rho_0 c - \rho_0 c = 0$.

For $\mu = i$, we obtain

$$
j_{0,i} = - \sigma_0 c F^{i0}.
$$

Since $F^{i0} = - E_i / c$, this simplifies to

$$
j_0 = \sigma_0 E,
$$

recovering the familiar form of Ohm's law in the rest frame and confirming that $\sigma_0$ is the conductivity in this frame.
""")
            c.Title.menu_title("Part b", level=3, parent=q6_title)
            c.Text(R"""
Show that the current in frame (S) is given by:

$$
\vec{j} = \rho v + \gamma_v \sigma_0 \left[ \vec{E} + \frac{\vec{v} \times \vec{B}}{c} - \frac{\vec{v} (\vec{v} \cdot \vec{E})}{c^2} \right].
$$""")
            with c.Admonition.show_working():
                c.Text("Starting with the")
                c.DropdownReference("expression for Ohm's law", ref=ohms_law)
                c.Text(R"""
and setting $\mu = 0$, we find:

$$
\rho c + \frac{1}{c^2} \left( -\gamma_\nu \rho c^2 + \gamma_\nu \vec{v} \cdot \vec{j} \right) \gamma_\nu c = \sigma_0 \gamma_\nu \frac{\vec{v} \cdot \vec{E}}{c}.
$$

For $\mu = i$, this gives:

$$
j_i + \frac{1}{c^2} \left( -\gamma_\nu \rho c^2 + \gamma_\nu \vec{v} \cdot \vec{j} \right) \gamma_\nu v_i = \sigma_0 \gamma_\nu v_i \left[ \frac{E_i}{c} + (\vec{v} \times \vec{B})_i \right],
$$

where the equation with $\mu = 0$ is used to express the second term on the left-hand side in terms of $\vec{E}$. This can be rewritten as:

$$
j_i = \rho v_i + \gamma_\nu \sigma_0 \left[ E_i + (\vec{v} \times \vec{B})_i - \frac{\vec{v} \cdot \vec{E}}{c^2} v_i \right].
$$""")
            c.Title.menu_title("Part c", level=3, parent=q6_title)
            c.Text(R"""
c) Assume the conductor is uncharged in its rest frame, meaning $\rho_0 = 0$. Derive expressions for $\rho$ and $\vec{j}$ in frame (S) in terms of $\vec{v}$, $\vec{E}$, and $\vec{B}$.
""")
            with c.Admonition.show_working():
                c.Text(R"""
In the rest frame, $U_\nu J^\nu = - \rho_0 c^2 = 0$, which is an invariant.""")
                c.Text("Consequently,")
                c.DropdownReference("Ohm's law", ref=ohms_law)
                c.Text(R"simplifies to $J^\mu = \sigma_0 F^{\mu\nu} U_\nu$.")
                c.Text(R"""
We can therefore use the equations derived in part (b) for $\mu = 0$ and $\mu = i$, excluding the second term on the left-hand side.
This gives:

$$
\rho = \sigma_0 \gamma_\nu \frac{\vec{v} \cdot \vec{E}}{c^2} \,, ~~~ \vec{j} = \sigma_0 \gamma_\nu \left( \vec{E} + \vec{v} \times \vec{B} \right).
$$""")
            q7_title = c.Title.menu_title(
                "Q7: Angular momentum of the electromagnetic field",
                level=2,
                parent=self,
            )
            c.Text(R"""
The momentum density of the electromagnetic field is given by $\vec{g} = \frac{\vec{S}}{c^2}$, where $\vec{S} = \frac{\vec{E} \times \vec{B}}{\mu_0}$ is the Poynting vector.
The angular momentum density of the field can thus be defined as:

$$
\vec{L} = \vec{r} \times \vec{g}.
$$

This is related to the third-rank tensor:

$$
M^{\alpha\beta\gamma} = X^\gamma T^{\alpha\beta} - X^\beta T^{\alpha\gamma},
$$

where $T^{\alpha\beta}$ is the stress-energy tensor.
""")
            c.Title.menu_title("Part a", level=3, parent=q7_title)
            c.Text(R"""
Show that $\partial_\alpha M^{\alpha\beta\gamma} = 0$ (note that this equality would not hold if $T^{\alpha\beta}$ were not symmetric).""")
            with c.Admonition.show_working():
                c.Text(R"""
We have:

$$
\partial_\alpha M^{\alpha\beta\gamma} = X^\gamma \partial_\alpha T^{\alpha\beta} + T^{\gamma\beta} - X^\beta \partial_\alpha T^{\alpha\gamma} - T^\beta\gamma.
$$

Using $\partial_\alpha T^{\alpha\beta} = 0$ and $T^{\beta\gamma} = T^{\gamma\beta}$, we obtain $\partial_\alpha M^{\alpha\beta\gamma} = 0$.
This calculation demonstrates that the symmetry of $T^{\alpha\beta}$ is essential for $\partial_\alpha M^{\alpha\beta\gamma} = 0$ to hold, which was a key motivation for constructing a symmetric stress-energy tensor.""")
            c.Title.menu_title("Part b", level=3, parent=q7_title)
            c.Text(R"""
Rewrite the equation $\partial_\alpha M^{\alpha ij} = 0$, where $i, j = 1, \dots, 3$, in terms of $\vec{L}$ and the stress exerted by the electromagnetic field.
Recall that the stress on a surface with a normal in the $k$-direction is given by $T(k) = - \sigma_{ik} \hat{x}_i - \sigma_{jk} \hat{x}_j - \sigma_{kk} \hat{x}_k$, and that $\sigma_{ij}$ is symmetric.
""")
            with c.Admonition.show_working():
                c.Text(R"""
The components of $M^{\alpha ij}$ are:

$$
M^{0ij} = X^j T^{0i} - X^i T^{0j} = c x_j g_i - c x_i g_j = - c (\vec{r} \times \vec{g})_k = - c L_k,
$$

$$
M^{kij} = X^j T^{k i} - X^i T^{k j} = - x_j \sigma_{ki} + x_i \sigma_{kj}.
$$

Substituting into the equation $\partial_\alpha M^{\alpha ij} = 0$ gives:

$$
- \frac{\partial L_k}{\partial t} + \frac{\partial}{\partial x_k} \left( - x_j \sigma_{ki} + x_i \sigma_{kj} \right) = 0.
$$

Using the symmetry of $\sigma_{ij}$, the term $- x_j \sigma_{ki} + x_i \sigma_{kj}$ can be rewritten as $- x_j \sigma_{ik} + x_i \sigma_{jk} = - (\vec{r} \times \vec{T}(k))_k$.

Thus, the equation $\partial_\alpha M^{\alpha ij} = 0$ is a continuity equation for angular momentum:

$$
\frac{\partial L_k}{\partial t} + \partial_i  (\vec{r} \times \vec{T}(k))_i = 0.
$$

Inspired by the fact that the term on the right is a divergence, we can integrate this equation over the entire volume $\mathcal{V}$ to find the conservation of the $k$-component of angular momentum:

$$
\int_{\mathcal{V}} L_k \, dV = \text{constant},
$$

where we found that the integral of the divergence term is zero using the divergence theorem; by the definition of the volume $\mathcal{V}$, the electromagnetic field vanishes at the boundaries.
""")
            c.Title.menu_title("Part c", level=3, parent=q7_title)
            c.Text(R"""
c) Write the equation $\partial_\alpha M^{\alpha 0i} = 0$, for $i = 1 \dots 3$, and show that it leads to:

$$
\frac{d\vec{R}}{dt} = \frac{c^2 \vec{G}}{E},
$$

where $\vec{R}$ is the coordinate of the center of mass of the electromagnetic field, defined by:

$$
\vec{R} \int_{\mathcal{V}} \mathcal{E} \, dV = \int_{\mathcal{V}} \vec{r} \mathcal{E} \, dV.
$$

Here, $\mathcal{E}$ is the electromagnetic energy density, and $E$ and $\vec{G}$ are the total electromagnetic energy and momentum, respectively.
""")
            with c.Admonition.show_working():
                c.Text(R"""
Integrating $\partial_\alpha M^{\alpha 0i} = 0$ over the entire volume $\mathcal{V}$ gives:

$$
\int_{\mathcal{V}} \partial_t M^{00i} = 0,
$$

since the integral of the divergence term vanishes. We have:

$$
M^{00i} = X^i T^{00} - X^0 T^{0i} = x_i \mathcal{E} - c^2 t g_i.
$$

Integrating this over the volume gives: $R_i \mathcal{E} - c^2 t G_i$. Taking the time derivative yields:

$$
\frac{d \vec{R}}{dt} = \frac{c^2 \vec{G}}{\mathcal{E}}.
$$

Note: This result is analogous to the case of a system of particles, where the velocity of the center of momentum is given by $\vec{v}_{\text{cm}} = \frac{p_{\text{total}} c^2}{E_{\text{total}}}$.
""")

        return div
