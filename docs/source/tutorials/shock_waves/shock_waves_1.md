# Incident shock waves

In this tutorial, we will cover how to solve the Rankine-Hugoniot equations for a planar incident shock wave, namely

```{eval-rst}
.. math::
    :nowrap:

    \begin{equation}
      p_2 = p_1 + \rho_1 u_1^2 \left( 1-\dfrac{\rho_1}{\rho_2}\right) \quad \text{and} \quad 
    h_2 = h_1 + \dfrac{u_1^2}{2}\left[1- \left(\dfrac{\rho_1}{\rho_2}\right)^2\right],
    \end{equation}
```
where $p$, $\rho$, $u$, and $h$ represent pressure, density, velocity, and specific enthalpy, respectively, and the subscripts 1 and 2 refer to the upstream and downstream states of the shock wave. This equation must be supplemented by the equation of state, which for an ideal gas reads

```{eval-rst}
.. math::
    :nowrap:

    \begin{equation}
    p = \rho R T / W,
    \end{equation}
```
where $R$ is the universal gas constant, $T$ is the temperature, and $W$ is the molecular weight of the gas. 

To solve these equations using the Combustion Toolbox, we will use the {mat:func}`~src.+combustiontoolbox.+shockdetonation.@ShockSolver.ShockSolver`  class, part of the `+combustiontoolbox.+shockdetonation` (CT-SD) subpackage (module). Below is an example that solves the Rankine-Hugoniot equations for a planar incident shock wave in air (79% $\text{N}_2$, 21% $\text{O}_2$ by volume), with an initial temperature $T_1 = 300$ K, pressure $p_1 = 1$ bar, and a pre-shock Mach number $\mathcal{M}_1 \in [1, 10]$:

```matlab
% Import packages
import combustiontoolbox.databases.NasaDatabase
import combustiontoolbox.core.*
import combustiontoolbox.shockdetonation.ShockSolver

% Get NASA's database
DB = NasaDatabase();

% Define chemical system
system = ChemicalSystem(DB);

% Initialize mixture
mix = Mixture(system);

% Define chemical state
set(mix, {'N2', 'O2'}, [79/21, 1]);

% Define properties
mixArray1 = setProperties(mix, 'temperature', 300, 'pressure', 1, 'Mach', 1:0.1:10);

% Initialize shock solver
solver = ShockSolver();

% Perform shock calculations
[mixArray1, mixArray2] = solveArray(solver, mixArray1);

% Generate report
report(solver, mixArray1, mixArray2);
```

This code snippet will generate two figures: Molar fraction of species in the mixture as a function of the pre-shock Mach number and the variation of the thermodynamic properties (e.g., temperature, pressure) as a function of the pre-shock Mach number.

<p align="center">
    <img src="../../_static/img/shock_waves_1_fig1.svg" width="1000">
</p>

<p align="center">
    <img src="../../_static/img/shock_waves_1_fig2.svg" width="1000">
</p>

````{tip}
The Combustion Toolbox allows to consider different caloric models regarding the final gas mixture, including calorically perfect gas, calorically imperfect gas with frozen chemistry, or calorically imperfect gas with equilibrium chemistry, including dissociation and ionization. 
````

For example, to consider the calorically perfect gas approximation, initialize the {mat:func}`~src.+combustiontoolbox.+shockdetonation.@ShockSolver.ShockSolver` class as follows

```matlab
solver = ShockSolver('FLAG_TCHEM_FROZEN', true);
````

For the calorically imperfect gas with frozen chemistry model, also known as the thermally perfect gas model, use

```matlab
solver = ShockSolver('FLAG_FROZEN', true);
````