# Functions
Here we can find the documentation of the routines of the problems that can be solved in the Combustion Toolbox. We can distinguish three main types:

## Solvers

Routines to solve different type of problems. We can distinguish three main types:
   * chemical equilibrium,
   * shocks and detonations,
   * rocket propellant performance.

***
```{eval-rst}
.. automodule:: src.Solver
   :members:
```
***

### Functions

A collection of functions necessary to obtain different data.

***
```{eval-rst}
.. automodule:: src.Solver.Functions
   :members:
```
***

#### Root finding algorithms

Roots algorithm used to obtain the temperature at equilibrium for a given thermochemical transformation. The methods implemented are:
   * Newton-Raphson method.
   * Steffensen-Aitken method.

***
```{eval-rst}
.. automodule:: src.Solver.Functions.root_finding
   :members:
```
***

#### Thermodynamics properties

Functions to obtain thermodynamic properties from a given mixture.

***
```{eval-rst}
.. automodule:: src.Solver.Functions.Thermo
   :members:
```
***


<!-- ### Chemical equilibrium

```{eval-rst}
.. automodule:: src.Solver.chemical_equilibrium
   :members:
```

### Shocks and detonations

```{eval-rst}
.. automodule:: src.Solver.shocks_detonations
   :members:
```

### Rocket propellant performance

```{eval-rst}
.. automodule:: src.Solver.Rocket
   :members:
```

## Settings

### self

```{eval-rst}
.. automodule:: src.Settings.self.App
```

```{eval-rst}
.. automodule:: src.Settings.self.Constants
```

```{eval-rst}
.. automodule:: src.Settings.self.Elements
```

```{eval-rst}
.. automodule:: src.Settings.self.Miscellaneous
```

```{eval-rst}
.. automodule:: src.Settings.self.ProblemDescription
```

```{eval-rst}
.. automodule:: src.Settings.self.ProblemSolution
```

```{eval-rst}
.. automodule:: src.Settings.self.Species
```

```{eval-rst}
.. automodule:: src.Settings.self.TunningProperties
```

### Functions

```{eval-rst}
.. automodule:: src.Settings.functions
   :members:
```

### Extensions

```{eval-rst}
.. automodule:: src.Settings.functions
   :members:
``` -->
