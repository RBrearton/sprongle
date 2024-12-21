---
title: B2 problem set 2 
subtitle: Symmetry and relativity
description: Problem set 2 for the third year symmetry and relativity course at Oxford University
# status: new
---


## Q1: Chemical bonding

### Part a

!!! question

    Qualitatively describe the five different types of chemical bonds and why they occur.

Just copy the table out of Steve Simon's "The Oxford Solid State Basics" book.
To avoid *direct* plagiarism, I won't copy the table here.

### Part b

!!! question

    Describe qualitatively the phenomenon of Van der Waals forces.
    Explain why the force is attractive and proportional to $1/R^7$.

Van der Waals forces are the attractive forces between molecules.
They are caused by the fluctuating electric fields of the molecules.
We can get the $1/R^7$ dependence without thinking too hard - it's clear from dimensional analysis, so we don't need to remember exact forms of results from electrostatics.

???+ info "Show working"

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

### Part c

!!! question

    The ionization energy of a sodium atom is 5.14 eV.
    The electron affinity of a chlorine atom is 3.62 eV.
    The bond length of a NaCl molecule is 2.36 Å.
    Calculate the total energy released when a NaCl molecule is formed.

    The actual experimental value is 4.26 eV.
    Comment on the sign of your error.

???+ info "Show working"

    The Coloumb energy of the NaCl molecule is

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

## Q2: Covalent bonding in detail

I'll write this up if I find the time, as it's the only asterisked problem on the set.

## Q3: Interatomic potentials

### Part a

!!! question

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

The exponent 6 comes from the fact that the Lennard-Jones potential is used to model Van der Waals interactions.
There are a few interesting things to note here:

-   Lennard-Jones is one guy with a double-barrelled surname!
-   If we wanted to study interactions in a crystal, we might want to use something like the [Morse potential](https://en.wikipedia.org/wiki/Morse_potential).
-   The twelfth power is wrong. It models Pauli repulsion, which has a very different functional form. We keep it because it's extremely easy to square numbers with a computer, and we've already had to calculate the sixth power to get the attractive part of the potential! Really, any power greater than 6 would have worked, and we choose 12 for computational efficiency.

### Part b

!!! question

    Find $x_0$, $\kappa$, and $\kappa_3$ for the Lennard-Jones potential.

This is just algebra - Taylor expand the potential and compare coefficients.

??? success "Answer"

    $$
    x_0 = 2^{\frac{1}{6}}\sigma,
    $$

    $$
    \kappa = 36 \left( 2^{\frac{2}{3}} \frac{\epsilon}{ \sigma^2} \right),
    $$

    $$
    \kappa _3 = - 756\sqrt{2} \frac{\epsilon}{\sigma^3}.
    $$

## Q4: Classical model of thermal expansion

!!! question

    In classical statistical mechanics, the expectation of $x$ is

    $$
    \langle x \rangle _{\beta} = \frac{\int  x e^{-\beta V(x)} dx}{\int  e^{-\beta V(x)} dx}.
    $$

    We can't do those integrals with arbitrary $V(x)$, but we could expand the exponentials as

    $$
    e^{-\beta V(x)} = e^{\frac{\beta \kappa}{2} (x - x_0)^2} \left[ 1 + \frac{\beta \kappa_3}{3!} (x - x_0)^3 + \ldots \right],
    $$

    and let the limits of integration go to $\pm \infty$.

### Part a

!!! question

    Why is this expansion of the exponent and extension of the limits of integration valid?

The *real* answer is that we do it because it's the only way to make progress.
You figure out what it means only if your results are interesting!

The answer that the question is probably looking for is that, if $k_B T$ is small, we're going to have a very peaked Boltzmann distribution, and the integrals will be dominated by the region around the minimum of the potential.

I hear you though - sure, that lets us expand the limits and write $V(x) \approx \frac{\kappa}{2} (x - x_0)^2 + \frac{\kappa_3}{3!} (x - x_0)^3 + \ldots$, but then why Taylor expand the exponential on the cubic part, and not the quadratic part?

I'll provide an exact bound on this on the last part of the question, but we're just requiring that the cubic term is appreciably smaller than the quadratic term.

### Part b

!!! question

    Use this to derive $\langle x \rangle _{\beta}$ and show that the coefficient of thermal expansion is

    $$
    \alpha = \frac{1}{L} \frac{\partial L}{\partial T} = \frac{1}{x_0} \frac{k_B \kappa_3}{2 \kappa^2}.
    $$

There are two important tricks here:

1.  All odd integrals are 0 by symmetry
2.  Shift all the integrals by $x_0$

???+ info "Show working"

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

    as required.

### Part c

!!! question

    In what temperature range is the above expansion valid?

Ok, now it's time to make the terms and conditions surrounding out approximation a bit more precise.

???+ info "Show working"

    Rewriting our expression by Taylor expanding the cubic term, but not the quadratic term, is reasonable when

    $$
    \kappa_3 \Delta x \ll \kappa
    $$

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
    $$

    Subbing this back into the original approximation conditions(1) gives us
    {.annotate}

    1.  <h2>Approximation conditions</h2>
        This is the simplest and most clearly correct statement of our approximation conditions.
        $$
        \kappa_3 \sqrt{\frac{2 k_B T}{\kappa}} \ll \kappa
        $$
        {.annotate}

    $$
    \kappa_3^2 \frac{k_B T}{\kappa} \ll \kappa^2 \, ,
    $$

    and then, equivalently,

    $$
    k_B T \ll \frac{\kappa^3}{\kappa_3^2} \, .
    $$

### Part d

!!! question

    This is valid for a 2-particle system, but not a many atom chain.
    Why?
    How would you modify the calculation to account for this?

Well... our potential only has a single distance between two atoms in it!
As a result, we're basically studying the properties of a bunch of non-interacting harmonic oscillators. (okay, anharmonic oscillators because of the cubic term, but you get the idea!)

To properly handle the many-atom chain, we need to account for the fact that the coupled differential equations that show up when we try to solve for the motion of the chain are going to lead to normal modes.
There will be some dispersion relation ($\omega(k)$) that tells us how the normal modes of the chain are going to behave as a function of wavevector $k$.

We can then think about thermally occupying these modes using Bose statistics, and calculate the average expansion of the chain as a function of temperature.

## Q5: Phonons on a one-dimensional monatomic chain

### Part a

!!! question

    What is meant by a normal mode?
    What is meant by a phonon?
    Explain why phonons obey Bose-Einstein statistics.

For normal modes, quoting wikipedia:

*"A normal mode is a pattern of motion in which all parts of the system move sinusoidally with the same frequency and with a fixed phase relation."*

Phonons are quanta of vibration.

Phonons obey Bose-Einstein statistics because there's no reason to limit the number of phonons in a given mode.

### Part b

!!! question

    Derive the dispersion relation for longitudinal oscillations of a one dimensional chain of N identical atoms of mass $m$, lattice spacing $a$ and spring constant $\kappa$.

This is bookwork.

??? success "Answer"

    $$
    \omega = 2 \sqrt{\frac{\kappa}{m}} \left| \, \sin \left( \frac{ka}{2} \right) \right|
    $$

### Part c

!!! question

    Show that the mode with wavevector $k$ has the same pattern of mass displacements as the mode with wavevector $k + 2 \pi / a$.
    Show that the dispersion relation is periodic in $k$-space (reciprocal space).

    How many *different* normal modes are there?

The first part is just a matter of plugging in $k + 2 \pi / a$ into the dispersion relation.
It's a trig function...

The second part only requires a small amount of algebra.

???+ info "Show working"

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
    $$

    Noting that $L = Na$, that means $\Delta k = 2\pi / L$.

    We get the number of modes by diving the range of $k$ by the spacing between adjacent $k$ states, so

    $$
    N = \frac{\mathrm{range}}{\mathrm{spacing}} = \frac{2\pi/a}{2\pi/L} = L/a = N \, .
    $$

    So... Debye's fudge was correct!

### Part d

!!! question

    -   Derive the phase and group velocities and sketch them as a function of $k$.
    -   What is the sound velocity?
    -   Show that the sound velocity is given by $v_s = \sqrt{\beta^{-1}/\rho}$, where $\rho$ is the mass density and $\beta$ is the compressibility.

Okay, there are a few small things to show here, so let's get to it.

???+ info "Show working"

    We get the group velocity by differentiating the dispersion relation(1) with respect to $k:
    {.annotate}

    1.  <h2>Monatomic phonon dispersion</h2>
        This is a bookwork result that we derived in part b.  
        $$
        \omega = 2 \sqrt{\frac{\kappa}{m}} \left| \, \sin \left( \frac{ka}{2} \right) \right|
        $$
        {.annotate}

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
    $$

    To show the final part, we just need an expression for the compressibility.
    The compressibility is defined as

    $$
    \beta = -\frac{1}{L} \frac{\partial L}{\partial F} \, .
    $$

    We can consider the interatomic distances of atoms in the chain as a function of the force applied:

    $$
    x(F) = a - \frac{F}{\kappa} \, .
    $$

    This gives us $L = N x(F)$, which we can differentiate to get

    $$
    \frac{\partial L}{\partial F} = -\frac{N}{\kappa} \, .
    $$

    This means that the compressibility is

    $$
    \beta = \frac{1}{L} \frac{N}{\kappa} = \frac{1}{\kappa a} \, .
    $$

    Using the fact that $\rho = m / a$, we finally get

    $$
    v_s = \sqrt{\frac{1}{\beta \rho}} = a \sqrt{\frac{\kappa}{m}} \, .
    $$

### Part e

!!! question

    Calculate and sketch the density of states per frequency $g(\omega)$.

???+ info "Show working"

    The density of states is

    $$
    g(\omega) = \frac{dN}{d\omega} = \frac{dN}{dk} \frac{dk}{d\omega}
    $$

The rest of the problem is just being careful with the algebra, wavevector degeneracy etc. ($+k$ and $-k$ have the same $\omega$, which gives an extra factor of 2).

???+ info "Show working"

    Subbing in the expression for the dispersion relation(1) into the density of states(2)
    {.annotate}

    1.  <h2>Monatomic phonon dispersion</h2>
        This is a bookwork result that we derived in part b.
        $$
        \omega = 2 \sqrt{\frac{\kappa}{m}} \left| \, \sin \left( \frac{ka}{2} \right) \right|
        $$
        {.annotate}
    2.  <h2>Density of states</h2>
        This is a bookwork result that we just derived.
        $$
        g(\omega) = \frac{dN}{d\omega} = \frac{dN}{dk} \frac{dk}{d\omega}
        $$
        {.annotate}

    $$
    \frac{dN}{dk} \frac{dk}{d\omega}
    =
    \frac{2 Na}{2\pi a \sqrt{\kappa / m} \cos({ka/2})} = \frac{Na}{2\pi v_g}
    $$

    This is as a function of $k$, so we just need to use our dispersion relation to swap out $k$ for $\omega$.
    Doing this gives

    $$
    g(\omega) = \frac{N}{\pi\sqrt{\kappa/m - (\omega/2)^2}} \, .
    $$

### Part f

!!! question

    Write an expression for the heat capacity of this chain.
    You will get an integral that you can't do analytically.

Since the wording of the question is so vague, I'd actually recommend not substituting in the expression for the density of states.

???+ info "Show working"

    The internal energy is

    $$
    U = \int g(\omega) \hbar \omega \left( \frac{1}{e^{\hbar \omega / k_B T} - 1} \right) d\omega \, .
    $$

    The heat capacity is then just $C = \frac{dU}{dT}$, which we may/may not be able to do depending on the form of $g(\omega)$.

### Part g

!!! question

    Show that, at high temperature, the law of Dulong and Petit is obeyed.

We can do this quite easily because we didn't substitute in the expression for the density of states.

???+ info "Show working"

    Using our expression for the heat capacity(1), we can Taylor expand the exponential in the integrand to get
    {.annotate}

    1.  <h2>1D monatomic phonon heat capacity</h2>
        The internal energy is

        $$
        U = \int g(\omega) \hbar \omega \left( \frac{1}{e^{\hbar \omega / k_B T} - 1} \right) d\omega \, .
        $$

        The heat capacity is then just $C = \frac{dU}{dT}$, which we may/may not be able to do depending on the form of $g(\omega)$.

    $$
    C = \partial _T \int d\omega\, g(\omega) k_B T = N k_B \, .
    $$

    where we used the fact that $g(\omega) = dN/d\omega$ and we cancelled the $d\omega$ terms(1).
    {.annotate}

    2.  Stay mad, mathematicians :laughing:

## Q6: Phonons on a one-dimensional diatomic chain

### Part a

!!! question

    What's the difference between an acoustic and an optical mode?

Acoustic modes are modes where adjacent atoms move in phase.
Optical modes are modes where adjacent atoms move out of phase.

### Part b

!!! question

    Derive the longitudinal dispersion relation $\omega(k)$ for a one-dimensional diatomic chain of atoms of masses $m_1$ and $m_2$, lattice spacing $a$, and spring constant $\kappa$.

Not quite bookwork, but not far off, as a very similar problem is solved in the book.

??? success "Answer"

    $$
    \omega^2 = \frac{\kappa}{m_1 m_2}\left[(m_1 + m_2) \pm \sqrt{(m_1 + m_2)^2 - 4 m_1 m_2 \sin^2 \left( \frac{ka}{2} \right)}\right]
    $$

### Part c

!!! question

    Determine the frequencies of the acoustic and optical modes at $k=0$, as well as at the Brillouin zone boundary.

    Determine the sound velocity.

    Show that the group velocity is zero at the Brillouin zone boundary.

    Show that the sound velocity is again given by $v_s = \sqrt{\beta^{-1}/\rho}$.

There are a few things to get on with here, but it's all just plugging in numbers to the dispersion relation(1) that we quoted in the last part.
{.annotate}

1.  <h2>1D diatomic phonon dispersion</h2>
    We wrote this down in the last part.

    $$
    \omega^2 = \frac{\kappa}{m_1 m_2}\left[(m_1 + m_2) \pm S \right]
    $$

    where

    $$
    S = \sqrt{(m_1 + m_2)^2 - 4 m_1 m_2 \sin^2 \left( \frac{ka}{2} \right)}
    $$

<!-- NOTE: it would be nice to get this back natively in mkdocs by injecting the html. -->
<!-- Let's start by plotting the dispersion relation, to get a feel for what's going on.

!DIATOMIC_DISPERSION_PLOT -->

???+ info "Show working"

    For the acoustic mode $\omega(k=0) = 0$.
    Subbing in $k=0$ into the dispersion(1) gives
    {.annotate}

    1.  <h2>1D diatomic phonon dispersion</h2>
        The dispersion relation for a diatomic chain is

        $$
        \omega^2 = \frac{\kappa}{m_1 m_2}\left[(m_1 + m_2) \pm S \right]
        $$

        where

        $$
        S = \sqrt{(m_1 + m_2)^2 - 4 m_1 m_2 \sin^2 \left( \frac{ka}{2} \right)}
        $$


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
    $$

    Now let's look at the sound velocity.
    This is just the group velocity at $k=0$.
    The trick here is to make $k$ small *before* taking the derivative, so replace $\sin^2\left(\frac{ka}{2}\right)$ with $\left(\frac{ka}{2}\right)^2$ in the dispersion relation(1), and you end up with
    {.annotate}

    2.  <h2>1D diatomic phonon dispersion</h2>
        The dispersion relation for a diatomic chain is

        $$
        \omega^2 = \frac{\kappa}{m_1 m_2}\left[(m_1 + m_2) \pm S \right]
        $$

        where

        $$
        S = \sqrt{(m_1 + m_2)^2 - 4 m_1 m_2 \sin^2 \left( \frac{ka}{2} \right)}
        $$


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
    $$

### Part d

!!! question

    Sketch the dispersion in both the reduced and the extended zone scheme.

    If there are $N$ unit cells, how many different normal modes are there?

    How many branches of excitation are there? In other words, how many excitations are there at each $k$ in the reduced zone scheme?

Well, I already plotted the dispersion relation, so... see above(1).
If there are $N$ unit cells, there are $2N$ different normal modes, because there are two atoms per unit cell and so $2N$ degrees of freedom.
{.annotate}

1.  If the plot doesn't show up, please send me angry emails :sweat_smile:

As for the branches, there are two branches of excitation at each $k$ in the reduced zone scheme (see the plot).
This is because there's two atoms in the unit cell.

If we had 3 atoms in the unit cell, we'd have 3 branches of excitation at each $k$ in the reduced zone scheme.
One of these branches would be acoustic, and the other two would be optical.
We could never have more than 1 acoustic mode, because there's only one way to make all the atoms move in phase.

### Part e

!!! question

    What happens when $m_1 = m_2$?

The optical modes disappear, as the two atoms are indistinguishable.
The gap between the acoustic and optical modes at the Brillouin zone boundary closes.
The new lattice constant is $a/2$.
We have one mode per $k$, but our Brillouin zone is now twice as big, so the total number of modes is the same (as we haven't gained or lost any degrees of freedom).

## Q7: The tight-binding model

### Part a

!!! question

    Derive and sketch the dispersion relation for a monatomic one-dimensional chain with hopping integral $-t$, and on-site energy $\epsilon$.

    How many different eigenstates are there in the system?

    What is the effective mass of the electron near the bottom of the band?

    What's the density of states?

    If each atom is monovalent, what's the density of states at the Fermi surface?

    Estimate the heat capacity at low temperature.

    What's the heat capacity if the material is divalent?

    What's the spin susceptibility if the material is divalent?

The derivation of the dispersion relation is covered nicely in Steve Simon's book - I'd recommend following that.
I'm not going to include the plot, because it's just a cosine function.
The dispersion relation that we should derive is

??? success "Answer"

    $$
    E = \epsilon - 2t \cos(ka)
    $$

There are $N$ wavevector eigenstates, so, including spin, there are $2N$ eigenstates in the system.

Let's calculate the density of states.

???+ info "Show working"

    Let's search for $g(E)$, the density of states per energy.
    Using the spacing between adjacent $k$ states(1), gives us
    {.annotate}

    1.  <h2>State spacing</h2>
        We covered this earlier! Here's a recap.
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
        $$

    $$
    g(E) = \frac{dN}{dk} \frac{dk}{dE} = 4\, \frac{Na}{2\pi} \frac{dk}{dE} \, ,
    $$

    where the factor of 4 comes from the spin degeneracy, and the fact that both $k$ and $-k$ give the same energy.
    We can then differentiate the dispersion relation(1) to get
    {.annotate}

    2.  <h2>Monatomic tight-binding dispersion</h2>
        The electronic tight binding dispersion relation for a monatomic chain is
        $$
        E = \epsilon - 2t \cos(ka)
        $$
        {.annotate}

    $$
    g(E) = \frac{N}{\pi t} \frac{1}{\sqrt{1 - \left(\frac{E - \epsilon}{2t}\right)^2}} \, .
    $$

To figure out the density of states at the Fermi energy, we need to understand that a monovalent atom would exactly half-fill the band, as there are a total of $2N$ states that can be occupied by electrons.

That means that the highest occupied state is at $k =\pm \frac{\pi}{2a}$.
Subbing this into the dispersion relation(1) gives us
{.annotate}

1.  <h2>Monatomic tight-binding dispersion</h2>
    The electronic tight binding dispersion relation for a monatomic chain is
    $$
    E = \epsilon - 2t \cos(ka)
    $$
    {.annotate}

??? success "Answer"
    $$
    g(E_F) = \frac{N}{\pi t} \, .
    $$

To estimate the heat capacity at low temperature, we should remember from last week that, for an electron gas, the heat capacity per particle is

$$
C = \gamma k_B^2 g(E_F) T \, ,
$$

where $\gamma$ is a constant of order unity.

??? success "Answer"

    To solve the problem, all we need to do is sub in our expression for $g(E_F)$(1) to get
    {.annotate}

    1.  <h2>Fermi surface density of states</h2>
        We derived this just above.
        $$
        g(E_F) = \frac{N}{\pi t} \, .
        $$
        {.annotate}

    $$
    C = \gamma k_B^2 \frac{N}{\pi t} T \, .
    $$

Finally, if the material is divalent, the band will be completely filled.
This means that the heat capacity will be very large at low temperatures, and the spin susceptibility will be very small, because there are no states available for electrons to move into.
