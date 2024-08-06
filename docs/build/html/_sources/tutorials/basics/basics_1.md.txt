# Importing packages and classes
The Combustion Toolbox (CT) is organized using namespaces (**starting from version 1.1.0**). The main namespace is `combustiontoolbox`. The classes and methods included in CT's modules (described in detail later) rely on several `core` and `database` classes, namely:
   * <tt>Elements</tt>: stores the list of elements that may appear in the database.
   * <tt>Species</tt>: object containing the properties of a chemical species.
   * <tt>ChemicalSystem</tt>: object that defines the chemical system.
   * <tt>EquationState</tt>: object that defines the equation of state.
   * <tt>Mixture</tt>: object that defines a multicomponent mixture.
   * <tt>Database</tt>: abstract class that contains common methods for the databases.
   * <tt>NasaDatabase</tt>: a structured thermochemical database including data from {cite:t}`Mcbride2002, burcat2005` with *griddedInterpolant* objects (see MATLAB built-in function <tt>griddedInterpolant.m</tt>) that contain piecewise cubic Hermite interpolating polynomials (PCHIP) {cite:p}`fritsch1980` for faster data access.

Let's start by importing one of the subpackages of the Combustion Toolbox, the `databases` package. This package contains the classes that define the databases used in CT. To import the `databases` package, we can use the following command:
```matlab
import combustiontoolbox.databases.*
```
or we can import a specific class from the `databases` package:
```matlab
import combustiontoolbox.databases.NasaDatabase
```
to import only the `NasaDatabase` class.

In addition to the classes described above, there are other essential classes in the Combustion Toolbox, for example:
   * <tt>equilibriumSolver</tt>: solver class for equilibrium calculations,
   * <tt>shockSolver</tt>: solver class for shock calculations,
   * <tt>detonationSolver</tt>: solver class for detonation calculations,
   * <tt>Rocket</tt>: solver class for rocket calculations,

which are part of the `equilibrium`, `shockdetonation`, and `rocket` modules, respectively. All the classes and subpackages are imported as shown before. Thus, to import, e.g., the `equilibriumSolver` class this will be done as follows:
```matlab
import combustiontoolbox.equilibrium.equilibriumSolver
```