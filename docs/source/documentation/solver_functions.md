# Functions

A collection of functions necessary to obtain different data in the solver module. Here we can find:
   * general functions,
   * root finding algorithms,
   * thermodynamics properties.

## General functions

A collection of general functions necessary to obtain different data in the solver module.

***

:::{dropdown} Routines
```{eval-rst}
.. automodule:: src.solver.functions
   :members:
```
:::

## Root finding algorithms

Roots algorithm used to obtain the temperature at equilibrium for a given thermochemical transformation. The methods implemented are:
   * Newton-Raphson method.
   * Steffensen-Aitken method.

***

:::{dropdown} Routines
```{eval-rst}
.. automodule:: src.solver.functions.root_finding
   :members:
.. automodule:: src.solver.functions.root_finding.newton
   :members:
.. automodule:: src.solver.functions.root_finding.steffenson
   :members:
```
:::


## Thermodynamic properties

Functions to obtain thermodynamic properties from a given mixture.

***

:::{dropdown} Routines
```{eval-rst}
.. automodule:: src.solver.functions.thermo
   :members:
```
:::