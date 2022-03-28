# Functions

A collection of functions necessary to obtain different data in the solver module. Here we can find:
   * general functions,
   * root finding algorithms,
   * thermodynamics properties.

## General functions

A collection of general functions necessary to obtain different data in the solver module.

***

```{eval-rst}
.. collapse:: Routines

   .. automodule:: src.Solver.Functions
      :members:
```

## Root finding algorithms

Roots algorithm used to obtain the temperature at equilibrium for a given thermochemical transformation. The methods implemented are:
   * Newton-Raphson method.
   * Steffensen-Aitken method.

***

```{eval-rst}
.. collapse:: Routines

   .. automodule:: src.Solver.Functions.root_finding
      :members:
   .. automodule:: src.Solver.Functions.root_finding.newton
      :members:
   .. automodule:: src.Solver.Functions.root_finding.steffenson
      :members:
```

## Thermodynamics properties

Functions to obtain thermodynamic properties from a given mixture.

***

```{eval-rst}
.. collapse:: Routines

   .. automodule:: src.Solver.Functions.Thermo
      :members:
```