# Chapman–Jouguet detonation waves

## Introduction

Chapman–Jouguet (CJ) detonation waves are computed by solving the Rankine–Hugoniot relations across a planar detonation front in a reactive gas mixture. As illustrated in {numref}`fig_sketch_normal_detonation`, a detonation wave consists of a leading shock followed by a tightly coupled reaction zone, in which the gas is compressed, heated, and chemically transformed.

:::{figure} /_static/img/sketch_normal_detonation.svg
:name: fig_sketch_normal_detonation
:width: 400px
:align: center

Schematic of a planar detonation wave in the wave-fixed frame.
:::

The upstream state is characterized by the velocity $u_1$, temperature $T_1$, pressure $p_1$, and chemical composition $\boldsymbol{n}_1$. The flow undergoes an abrupt thermodynamic transformation across the wave, driven by shock compression and chemical energy release. The downstream state $(u_2, p_2, T_2, \boldsymbol{n}_2)$ is obtained by solving the conservation equations for mass, momentum, and energy, assuming the products are in **chemical equilibrium**.

The Chapman–Jouguet condition imposes that the flow becomes sonic relative to the detonation front immediately behind the wave, i.e., $u_2 = a_2$. This condition selects the unique point where the Rayleigh line is tangent to the equilibrium Hugoniot curve (see {numref}`fig_sketch_diagram_detonation`), defining the minimum velocity for a self-sustaining detonation in chemical equilibrium.

:::{figure} /_static/img/sketch_diagram_detonation.svg
:name: fig_sketch_diagram_detonation
:width: 550px
:align: center

Family of admissible solutions defined by the Rankine–Hugoniot and Rayleigh relations for a planar, steady detonation wave.
:::

## Governing equations
For a one-dimensional planar shock, the **Rankine–Hugoniot relations** express the conservation of mass, momentum, and energy across the shock front as:
```{eval-rst}
.. math::
    :nowrap:

    \begin{equation}
      p_2 = p_1 + \rho_1 u_1^2 \left( 1-\dfrac{\rho_1}{\rho_2}\right) \quad \text{and} \quad 
      h_2 = h_1 + \dfrac{u_1^2}{2}\left[1- \left(\dfrac{\rho_1}{\rho_2}\right)^2\right],
    \end{equation}
```
where $h$ denotes specific enthalpy. These equations must be closed with the equation of state, which for an ideal gas reads:

```{eval-rst}
.. math::
    :nowrap:

    \begin{equation}
    p = \rho R T / W,
    \end{equation}
```
where $R$ is the universal gas constant and $W$ is the molecular weight of the gas.

## Numerical example

We now illustrate how to solve the Rankine–Hugoniot equations in the Combustion Toolbox using the class {mat:func}`~src.+combustiontoolbox.+shockdetonation.@DetonationSolver.DetonationSolver`  class, part of the `+combustiontoolbox.+shockdetonation` (CT-SD) subpackage (module). Below is an example for methane–air mixtures at standard temperature and pressure, over a range of equivalence ratios $\phi \in [0.5, 4.0]$:

```matlab
% Import packages
import combustiontoolbox.databases.NasaDatabase
import combustiontoolbox.core.*
import combustiontoolbox.shockdetonation.*

% Get Nasa database
DB = NasaDatabase();

% Define chemical system
system = ChemicalSystem(DB);

% Initialize mixture
mix = Mixture(system);

% Define chemical state
set(mix, {'CH4'}, 'fuel', 1);
set(mix, {'N2', 'O2'}, 'oxidizer', [79/21, 1]);

% Define properties
mixArray1 = setProperties(mix, 'temperature', 300, 'pressure', 1, 'equivalenceRatio', 0.5:0.01:4);

% Initialize solver
solver = DetonationSolver('problemType', 'DET');

% Solve problem
[mixArray1, mixArray2] = solver.solveArray(mixArray1);

% Generate report
report(solver, mixArray1, mixArray2);
```

This script generates two diagnostic figures: one for the species molar fractions in the detonation products as a function of equivalence ratio, and another for the thermodynamic and flow properties across the wave.

:::{figure} /_static/img/detonation_waves_1_fig1.svg
:name: fig:molar_fraction_normal_detonation
:width: 1000px
:align: center

Molar fraction of chemical species downstream of a Chapman–Jouguet detonation in methane–air mixtures as a function of equivalence ratio $\phi$, at $T_1 = 300$ K and $p_1 = 1$ bar.
:::

:::{figure} /_static/img/detonation_waves_1_fig2.svg
:name: fig:properties_normal_detonation
:width: 1000px
:align: center

Thermodynamic and flow properties downstream of a Chapman–Jouguet detonation in methane–air mixtures as a function of equivalence ratio $\phi$, at $T_1 = 300$ K and $p_1 = 1$ bar.
:::