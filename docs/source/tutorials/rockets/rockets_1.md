# Rocket performance using the infinite-area-chamber approximation

## Introduction

The **infinite-area-chamber approximation (IAC)** is the simplest rocket-performance model available in Combustion Toolbox. It represents an idealized rocket engine in which the propellants first undergo adiabatic, constant-pressure equilibrium combustion in a chamber of effectively infinite area. Because the chamber area is assumed to be much larger than the throat area, the flow velocity in the chamber is negligible. The combustion products are then expanded through the nozzle under isentropic conditions.

This model is useful for preliminary performance estimates, propellant comparisons, and parametric sweeps over mixture ratio or equivalence ratio. It is especially convenient when the objective is to identify broad trends before moving to more detailed finite-area-chamber or finite-rate-chemistry models. The CT-ROCKET formulation and its validation against NASA CEA are described in {cite:p}`cuadra2026a`.

In `CT-ROCKET`, IAC calculations are performed with the {mat:class}`~src.+combustiontoolbox.+rocket.@RocketSolver.RocketSolver` class by selecting the problem type `ROCKET_IAC`. The solver returns the thermochemical state of the mixture at the main rocket stations:

* the initial propellant state,
* the chamber state,
* the nozzle throat state,
* the nozzle exit state, when an exit area ratio is specified.

Along with the thermochemical properties, the solver evaluates rocket-performance quantities such as gas velocity, sea-level specific impulse $I_{\text{sp}}$, and vacuum specific impulse $I_{\text{vac}}$.

## Governing model

The IAC model combines two idealized thermochemical transformations:

1. **Adiabatic constant-pressure equilibrium combustion**, used to determine the chamber state.
2. **Isentropic nozzle expansion**, used to determine the throat and exit states.

The chamber pressure $p_c$ is prescribed as part of the initial problem definition. The nozzle geometry is specified through the exit-to-throat area ratio

```{eval-rst}
.. math::
    :nowrap:

    \begin{equation}
      A^*_e = \frac{A_e}{A_t},
    \end{equation}
```

where $A_e$ is the nozzle exit area and $A_t$ is the throat area.

Once the chamber state is known, the throat state is obtained by enforcing the sonic condition. If an exit area ratio is provided, the exit state is then computed from the prescribed value of $A^*_e$ together with the isentropic expansion constraint. In equilibrium nozzle calculations, the mixture composition is allowed to adjust during the expansion so that thermochemical equilibrium is satisfied at each station; this is the shifting-equilibrium assumption.

## Numerical example

The following example computes the performance of **LH$_2$/LOX** mixtures at a chamber pressure close to 100 atm, an exit area ratio $A_e/A_t = 3$, and equivalence ratios in the range $\phi \in [1, 5]$:

```matlab
% Import packages
import combustiontoolbox.databases.NasaDatabase
import combustiontoolbox.core.*
import combustiontoolbox.rocket.*

% Load NASA database
DB = NasaDatabase();

% Define chemical system
system = ChemicalSystem(DB);

% Initialize mixture
mix = Mixture(system);

% Define reactants
set(mix, {'H2bLb'}, 'fuel', 1);
set(mix, {'O2bLb'}, 'oxidizer', 1);

% Define initial state and rocket parameters
mixArray1 = setProperties(mix, ...
    'temperature', 90, ...
    'pressure', 100 * 1.01325, ...
    'equivalenceRatio', 1:0.05:5, ...
    'areaRatio', 3);

% Initialize rocket solver
solver = RocketSolver('problemType', 'ROCKET_IAC');

% Solve IAC rocket problem
[mixArray1, mixArray2, mixArray3, mixArray4] = solver.solveArray(mixArray1);

% Generate summary report
report(solver, mixArray1, mixArray2, mixArray3, mixArray4);
```

The output arrays correspond to the following stations:

* `mixArray1`: initial propellant state,
* `mixArray2`: chamber state,
* `mixArray3`: throat state,
* `mixArray4`: exit state.

For parametric studies, the `report` method generates summary plots of composition, thermodynamic properties, and performance quantities. For instance, from the exit state we can extract the nozzle-exit molar fractions, temperature, pressure, velocity, and specific impulse as a function of equivalence ratio:

:::{figure} /_static/img/run_validation_ROCKET_CEA_17_molar.svg
:name: fig_rocket_iac_molar
:width: 1000px
:align: center

Variation of the nozzle-exit molar fractions as a function of equivalence ratio for a LH$_2$/LOX mixture using the IAC model.

:::{figure} /_static/img/run_validation_ROCKET_CEA_17_properties.svg
:name: fig_rocket_iac_properties
:width: 1000px
:align: center

Representative nozzle-exit properties for the same IAC calculation, compared with NASA CEA results.
:::
