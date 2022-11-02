# Utilities

A collection of routines with multiple purposes organized as follows:

* ```unclasified```
* ```databases```
* ```display```
* ```eos```
* ```export```
* ```extensions```
* ```root_finding```
* ```thermo```
* ```validations```

## Unclasified utility functions

A collection of unclasified functions necessary to perform all the calculations in CT.

***

:::{dropdown} Routines
```{eval-rst}
.. automodule:: src.utils
   :members:
```
:::

## Database functions

A collection of functions necessary to obtain generate the databases in CT.

***

:::{dropdown} Routines
```{eval-rst}
.. automodule:: src.utils.databases
   :members:
```
:::

## Display functions

A collection of functions necessary to display the results (command window and plots).

***

:::{dropdown} Routines
```{eval-rst}
.. automodule:: src.utils.display
   :members:
```
:::

## Equation of State functions

A collection of Equation of States (EoS) implemented in CT.

***

:::{dropdown} Routines
```{eval-rst}
.. automodule:: src.utils.eos
   :members:
```
:::

## Export functions

A collection of functions to export results.

***

:::{dropdown} Routines
```{eval-rst}
.. automodule:: src.utils.export
   :members:
```
:::

## Extensions functions

A collection of external functions from other repositories.

* Combustion Toolbox's color palette is obtained from the following repository: Stephen (2021). ColorBrewer: Attractive and Distinctive Colormaps (https://github.com/DrosteEffect/BrewerMap), GitHub. Retrieved December 3, 2021.
* For validations, Combustion Toolbox uses CPU Info from the following repository: Ben Tordoff (2022). CPU Info (https://github.com/BJTor/CPUInfo/releases/tag/v1.3), GitHub. Retrieved March 22, 2022.
* Combustion Toolbox's splash screen is based on a routine from the following repository: Ben Tordoff (2022). SplashScreen (https://www.mathworks.com/matlabcentral/fileexchange/30508-splashscreen), MATLAB Central File Exchange. Retrieved October 15, 2022.


## Root finding algorithms

Roots algorithm used to obtain the temperature at equilibrium for a given thermochemical transformation. The methods implemented are:
   * Newton-Raphson method.
   * Steffensen-Aitken method.

***

:::{dropdown} Routines
```{eval-rst}
.. automodule:: src.utils.root_finding
   :members:
.. automodule:: src.utils.root_finding.newton
   :members:
.. automodule:: src.utils.root_finding.steffenson
   :members:
```
:::


## Thermodynamic properties

Functions to obtain thermodynamic properties from a given mixture.

***

:::{dropdown} Routines
```{eval-rst}
.. automodule:: src.utils.thermo
   :members:
```
:::

## Validations functions

A collection of functions to generate the validations automatically.

***

:::{dropdown} Routines
```{eval-rst}
.. automodule:: src.utils.validations
   :members:
```
:::