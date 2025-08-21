# Rocket performance analysis

This section introduces the `CT-ROCKET` module for computing the performance of chemical rocket propulsion systems, as depicted in {numref}`fig_sketch_rocket`. The core solver is implemented in the {mat:class}`~src.+combustiontoolbox.+rocket.@RocketSolver.RocketSolver` class and provides tools to evaluate the idealized performance of a propellant system under a set of simplifying assumptions:

- One-dimensional flow.
- Uniform cross-sectional area in the chamber.
- Negligible inlet velocity at the injector.
- Infinitely fast chemistry at injection.
- Adiabatic combustion.
- Isentropic expansion through the nozzle.
- Homogeneous mixture (no slip or temperature difference between phases).
- Ideal gas equation of state.
- Continuity of temperature and velocity between gaseous and condensed species.
  
Thermochemical states are handled through the [CT-EQUIL module](./1_chemical_equilibrium.md). The formulation follows the methodology originally developed in NASA's CEA code {cite:p}`gordon1994`.

Two limiting cases are supported through `RocketSolver`:

- **Infinite-area-chamber approximation (IAC):** Isentropic combustion process.
- **Finite-area-chamber approximation (FAC):** Entropic combustion process.

These models allow for rapid estimation of propulsion performance, including the **characteristic velocity** ($c^*$), **thrust coefficient** ($C_F$), and **specific impulse** ($I_{\text{sp}}$), while accounting for chemical equilibrium, composition-dependent thermodynamics, and finite expansion effects.

:::{figure} /_static/img/sketch_rocket.svg
:name: fig_sketch_rocket
:width: 600px
:align: center

Schematic of a chemically reacting rocket flow including chamber, throat, and expanding nozzle.
:::

<!-- 

See the following dedicated pages for usage examples and detailed implementation of each model.

```{toctree}
:caption: Contents
:maxdepth: 1
:titlesonly:

rockets/rockets_IAC
rockets/rockets_FAC
``` 

-->