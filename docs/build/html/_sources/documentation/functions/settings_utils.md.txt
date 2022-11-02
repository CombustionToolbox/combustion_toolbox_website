# Functions

A collection of functions necessary to obtain different data in the settings module. Here we can find:
   * general utilities functions,
   * root finding algorithms,
   * thermodynamics properties.

## General utilities functions

A collection of general functions necessary to obtain different data in the settings module.

***

:::{dropdown} Routines
```{eval-rst}
.. automodule:: src.settings.functions
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
.. automodule:: src.settings.utils.root_finding
   :members:
.. automodule:: src.settings.utils.root_finding.newton
   :members:
.. automodule:: src.settings.utils.root_finding.steffenson
   :members:
```
:::


## Thermodynamic properties

Functions to obtain thermodynamic properties from a given mixture.

***

:::{dropdown} Routines
```{eval-rst}
.. automodule:: src.settings.utils.thermo
   :members:
```
:::