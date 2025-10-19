# Importing packages and classes

The Combustion Toolbox (CT) is organized using namespaces (**starting from version 1.1.0**). The main namespace is <tt>combustiontoolbox</tt>. The classes and methods included in CT's modules (described in detail later) rely on several <tt>core</tt> and <tt>database</tt> classes, including:

   * {mat:class}`~src.+combustiontoolbox.+core.@Elements.Elements`: stores the list of elements that may appear in the database.
   * {mat:class}`~src.+combustiontoolbox.+core.@Species.Species`: object containing the properties of a chemical species.
   * {mat:class}`~src.+combustiontoolbox.+core.@ChemicalSystem.ChemicalSystem`: object that defines the chemical system.
   * {mat:class}`~src.+combustiontoolbox.+core.@EquationState.EquationState`: an abstract class that contains common methods for the equation of state.
   * {mat:class}`~src.+combustiontoolbox.+core.@EquationStateIdealGas.EquationStateIdealGas`: object that defines an ideal gas equation of state.
   * {mat:class}`~src.+combustiontoolbox.+core.@Mixture.Mixture`: object that defines a multicomponent mixture.
   * {mat:class}`~src.+combustiontoolbox.+databases.@Database.Database`: an abstract class that contains common methods for the databases.
   * {mat:class}`~src.+combustiontoolbox.+databases.@NasaDatabase.NasaDatabase`: a structured thermochemical database including data from {cite:t}`Mcbride2002, burcat2005` with *griddedInterpolant* objects (see MATLAB built-in function <tt>griddedInterpolant.m</tt>) that contain piecewise cubic Hermite interpolating polynomials (PCHIP) {cite:p}`fritsch1980` for faster data access.
   * {mat:class}`~src.+combustiontoolbox.+databases.@BurcatDatabase.BurcatDatabase`: a structured thermochemical database including data from {cite:t}`burcat2005` with *griddedInterpolant* objects that contain piecewise cubic Hermite interpolating polynomials (PCHIP) {cite:p}`fritsch1980` for faster data access.

To get started, let's import one of the subpackages of the Combustion Toolbox, the `databases` package. This package contains the classes that define the databases used in CT. To import the `databases` package, use the following command:
```matlab
import combustiontoolbox.databases.*
```

For importing a specific class, such as {mat:class}`~src.+combustiontoolbox.+databases.@NasaDatabase.NasaDatabase`, use:
```matlab
import combustiontoolbox.databases.NasaDatabase
```

In addition to the classes described above, there are other essential classes in the Combustion Toolbox, for example:
   * {mat:class}`~src.+combustiontoolbox.+equilibrium.@EquilibriumSolver.EquilibriumSolver`: solver class for equilibrium calculations,
   * {mat:class}`~src.+combustiontoolbox.+shockdetonation.@ShockSolver.ShockSolver`: solver class for shock calculations,
   * {mat:class}`~src.+combustiontoolbox.+shockdetonation.@DetonationSolver.DetonationSolver`: solver class for detonation calculations,
   * {mat:class}`~src.+combustiontoolbox.+rocket.@RocketSolver.RocketSolver`: solver class for rocket calculations,

These classes are part of the CT-EQUIL (<tt>equilibrium</tt>), CT-SD (<tt>shockdetonation</tt>), and CT-ROCKET (<tt>rocket</tt>) modules (subpackages), respectively. All the classes and subpackages are imported as shown below:
```matlab
import combustiontoolbox.equilibrium.equilibriumSolver
import combustiontoolbox.shockdetonation.shockSolver
import combustiontoolbox.rocket.Rocket
```

For typical tasks, in addition to the solvers required, you will often need the following subpackages:
```matlab
import combustiontoolbox.databases.NasaDatabase
import combustiontoolbox.core.*
import combustiontoolbox.utils.display.*
```

This setup will ensure that you have access to the key components of the Combustion Toolbox for most of your tasks.

## Summary

`````{tab-set}

````{tab-item} Database and core classes

```matlab
% Import packages
import combustiontoolbox.databases.NasaDatabase
import combustiontoolbox.core.*
```

````

````{tab-item} Equilibrum solver

```matlab
% Import packages
import combustiontoolbox.databases.NasaDatabase
import combustiontoolbox.core.*
import combustiontoolbox.equilibrium.*
```

````

````{tab-item} Shock and Detonation solvers

```matlab
% Import packages
import combustiontoolbox.databases.NasaDatabase
import combustiontoolbox.core.*
import combustiontoolbox.shockdetonation.*
```

````

````{tab-item} Rocket solver

```matlab
% Import packages
import combustiontoolbox.databases.NasaDatabase
import combustiontoolbox.core.*
import combustiontoolbox.rocket.*
```

````

`````
