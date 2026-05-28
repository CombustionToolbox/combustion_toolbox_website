# Rocket performance considering the finite-area-chamber approximation

## Introduction

The **finite-area-chamber approximation (FAC)** extends the previous IAC model by accounting for the finite contraction between the combustion chamber and the throat. In this case, the gas does not remain at rest inside the chamber: it accelerates as it moves from the injector toward the chamber outlet and then continues toward the sonic throat and the nozzle exit. The FAC formulation therefore provides a more realistic representation of rocket-chamber flow while still retaining the idealized assumptions of equilibrium thermochemistry and quasi-one-dimensional isentropic expansion. The model implemented in Combustion Toolbox is described and validated against NASA CEA in {cite}`cuadra2026a`.

In addition to the nozzle expansion ratio,

```{eval-rst}
.. math::
    :nowrap:

    \begin{equation}
      A^*_e = \frac{A_e}{A_t},
    \end{equation}
```

the FAC model introduces the chamber contraction ratio

```{eval-rst}

.. math::
    :nowrap:

    \begin{equation}
      A^*_c = \frac{A_c}{A_t}
    \end{equation}
```

where $A_c$ is the chamber cross-sectional area, $A_t$ is the throat area, and $A_e$ is the nozzle exit area.

In `CT-ROCKET`, FAC calculations are performed with the {mat:class}`~src.+combustiontoolbox.+rocket.@RocketSolver.RocketSolver` class using the problem type `ROCKET_FAC`.

## Governing model

The FAC formulation introduces one additional geometric parameter relative to the IAC model:

- the chamber contraction ratio $A_c/A_t$,
- together with the nozzle expansion ratio $A_e/A_t$.

The fresh propellants first react near the injector region under equilibrium conditions. The downstream chamber, throat, and nozzle states are then adjusted iteratively so that the solution simultaneously satisfies the conservation equations, the prescribed geometry, and the thermochemical constraints.

As in the IAC formulation, the nozzle expansion is treated as isentropic. In equilibrium-nozzle calculations, the mixture composition is allowed to evolve during the expansion so that thermochemical equilibrium is satisfied at each station (shifting equilibrium).

Internally, the FAC algorithm relies on repeated calls to the IAC machinery to converge the injector, chamber, throat, and exit states consistently.

As a result, the FAC model returns five thermodynamic states:

- the initial propellant mixture,
- the injector state,
- the chamber outlet state,
- the throat state,
- the nozzle exit state.

Compared with `ROCKET_IAC`, the FAC formulation provides direct access to the thermodynamic evolution inside the chamber, not only across the nozzle.
## Numerical example

The following example computes a generalized **RP-1/LOX** parametric study with a chamber pressure of $22$ bar, a chamber contraction ratio $A_c/A_t = 2$, an exit ratio $A_e/A_t = 1.8$, and a range of equivalence ratios.

```matlab
% Import packages
import combustiontoolbox.databases.NasaDatabase
import combustiontoolbox.core.*
import combustiontoolbox.rocket.*

% Get NASA database
DB = NasaDatabase();

% Define chemical system
system = ChemicalSystem(DB);

% Initialize mixture
mix = Mixture(system);

% Define chemical state
set(mix, {'RP_1'}, 'fuel', 1);
set(mix, {'O2bLb'}, 'oxidizer', 1);

% Define properties
mixArray1 = setProperties(mix, ...
    'temperature', 298.15, ...
    'pressure', 22, ...
    'equivalenceRatio', 1:0.01:4, ...
    'areaRatioChamber', 2, ...
    'areaRatio', 1.8);

% Initialize solver
solver = RocketSolver('problemType', 'ROCKET_FAC');

% Solve problem
[mixArray1, mixArray2_inj, mixArray2_c, mixArray3, mixArray4] = solver.solveArray(mixArray1);

% Generate report
report(solver, mixArray1, mixArray2_inj, mixArray2_c, mixArray3, mixArray4);
```

The returned arrays correspond to:

- `mixArray1`: initial propellant state,
- `mixArray2_inj`: injector state,
- `mixArray2_c`: chamber outlet state,
- `mixArray3`: throat state,
- `mixArray4`: nozzle exit state.

In the same fashion as the IAC example, the `report` method generates summary plots of composition, thermodynamic properties, and performance quantities. For instance, the following movie shows the variation of the nozzle-exit molar fractions as a function of equivalence ratio for a **RP-1/LOX**  mixture using the FAC model, parametrized by the nozzle expansion ratio $A_e/A_t$:

:::{figure} /_static/gif/validation_rocket.gif
:name: fig_rocket_fac_validation
:width: 720px
:align: center

Representative comparison of nozzle-exit properties computed with the FAC model and NASA CEA for RP-1/LOX liquid-bipropellant rocket calculations.
:::

The broader [**Rocket calculations** section of the validations page](../../validations.md#rocket-calculations) also includes LH$_2$/LOX, LCH$_4$/LOX, and MMH/N$_2$O$_4$ cases.