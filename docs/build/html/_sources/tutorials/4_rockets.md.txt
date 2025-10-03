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
  
Thermochemical states are handled through the [CT-EQUIL module](./1_chemical_equilibrium.md). The formulation follows the methodology originally developed in NASA's CEA code {cite:p}`gordon1994`.

Two limiting cases are supported through `RocketSolver`:

- `ROCKET_IAC` - **Infinite-area-chamber approximation (IAC):** Isentropic combustion process.
- `ROCKET_FAC` - **Finite-area-chamber approximation (FAC):** Entropic combustion process.

These models allow for rapid estimation of propulsion performance, including the **characteristic velocity** ($c^*$), **thrust coefficient** ($C_F$), and **specific impulse** ($I_{\text{sp}}$), while accounting for chemical equilibrium, composition-dependent thermodynamics, and finite expansion effects.

## Congratulations!
Congratulations you have finished the Combustion Toolbox MATLAB tutorial! You should now be ready to begin using the Combustion Toolbox on your own (see the `examples` folder).

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