# Rockets

This section introduces the `CT-ROCKET` module for computing the performance of chemical rocket propulsion systems using a one-dimensional flow approximation. The schematic in {numref}`fig_sketch_rocket` depicts the physical components considered in this analysis:

- **Injector** (inj), where propellants are introduced at negligible velocity.
- **Combustion chamber** (c), a region of constant cross-sectional area $A_c$, bounded by an adiabatic wall.
- **Converging nozzle** section (c-t), with decreasing area $A(x)$, which accelerates the subsonic flow toward the throat.
- **Throat** (t), the location of minimum area $A_t$ where the flow becomes sonic.
- **Diverging nozzle** section (t-e), with increasing area $A(x)$, which enables supersonic expansion and thrust generation.

:::{figure} /_static/img/sketch_rocket.svg
:name: fig_sketch_rocket
:width: 600px
:align: center

Schematic of a chemically reacting rocket flow including chamber, throat, and expanding nozzle.
:::

 The solver is implemented in the {mat:class}`~src.+combustiontoolbox.+rocket.@RocketSolver.RocketSolver` class and provides tools to evaluate the idealized performance of a propellant system under a set of simplifying assumptions:

- One-dimensional flow.
- Uniform cross-sectional area in the chamber.
- Negligible inlet velocity at the injector.
- Infinitely fast chemistry at injection.
- Adiabatic combustion.
- Isentropic expansion through the nozzle.
- Homogeneous mixture (no slip or temperature difference between phases).
- Ideal gas equation of state.
- Continuity of temperature and velocity between gaseous and condensed species.
  
Thermochemical states are handled through the [CT-EQUIL module](./1_chemical_equilibrium.md). The formulation follows the methodology originally developed in NASA's CEA code {cite:p}`gordon1994`, while the implementation and validation of `CT-ROCKET` within Combustion Toolbox are discussed in {cite:p}`cuadra2026a`.

Two limiting cases are supported through {mat:class}`~src.+combustiontoolbox.+rocket.@RocketSolver.RocketSolver`:

- `ROCKET_IAC` - **Infinite-area-chamber approximation (IAC):** Isentropic combustion process.
- `ROCKET_FAC` - **Finite-area-chamber approximation (FAC):** Entropic combustion process.

These models allow for rapid estimation of propulsion performance, including the **characteristic velocity** ($c^*$), **thrust coefficient** ($C_F$), and **specific impulse** ($I_{\text{sp}}$), while accounting for chemical equilibrium, composition-dependent thermodynamics, and finite expansion effects.

The two formulations differ in how the combustion chamber is modeled:

- In the **IAC model**, the chamber is treated as infinitely large. The combustion process is therefore modeled as an isobaric equilibrium transformation, followed by an isentropic acceleration toward the throat and nozzle exit.
- In the **FAC model**, the chamber has a finite cross-sectional area. The flow accelerates inside the chamber, so the injector, chamber outlet, and throat states must be determined consistently.

```{toctree}
:caption: Contents
:maxdepth: 1
:titlesonly:

rockets/rockets_1
rockets/rockets_2
```
