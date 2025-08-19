# Chemical equilibrium at constant enthalpy and pressure

Let's consider the adiabatic combustion of acetylene (C$_2$H$_2$) with ideal air (79% N$_2$, 21% O$_2$ in volume) at constant pressure with $p = 1.01325$ bar (1 atm) and an equivalence ratio $\phi \in (0.5, 5)$. In this scenario, the equilibrium temperature of the system, denoted as $T$, is not initially determined, and we need to provide supplementary information to close the problem. For an adiabatic isobaric process, the enthalpy of the system remains constant, thus
```{eval-rst}
.. math::
    :nowrap:

    \begin{equation}
      \Delta f\left(T\right) \equiv h_{\rm F}\left(T\right) - h_{\rm I}\left(T_{\rm I}\right) = 0,
    \end{equation}
```
where the subscripts F and I refer here to the final (products) and initial (reactants) states of the mixture, respectively.

Similar to the preceding case, we will consider a set of 23 species involved in the combustion of hydrocarbon fuels with air, namely:

* CO$_2$, CO, H$_2$O, H$_2$, O$_2$, N$_2$, C<sub>gr</sub>,
* C$_2$, C$_2$H$_4$, CH, CH$_3$, CH$_4$, CN, H,
* HCN, HCO, N, NH, NH$_2$, NH$_3$, NO, O, OH.
  
This set, referred to as 'Soot formation,' is defined in the routine list_species.m and includes Ar.

```{tip}
The Combustion Toolbox offers various predefined list of species. To explore the complete list, type <tt>help combustiontoolbox.core.ChemicalSystem.findProducts</tt> at the MATLAB prompt or refer to the [Using predefined chemical systems](https://combustion-toolbox-website.readthedocs.io/en/latest/tutorials/basics/basics_4.html#using-predefined-chemical-systems) tutorial section.
```

Let's start by importing the Combustion Toolbox packages and defining the chemical system and initial state of the mixture (chemical composition, temperature, and pressure):

```matlab
% Import packages
import combustiontoolbox.databases.NasaDatabase
import combustiontoolbox.core.*
import combustiontoolbox.equilibrium.*
import combustiontoolbox.utils.display.*

% Get Nasa database
DB = NasaDatabase();

% Define chemical system
system = ChemicalSystem(DB, 'soot formation');

% Initialize mixture
mix = Mixture(system);

% Define chemical state
set(mix, {'CH4'}, 'fuel', 1);
set(mix, {'N2', 'O2'}, 'oxidizer', [79/21, 1]);

% Define properties
mixArray = setProperties(mix, 'temperature', 3000, 'pressure', 1 * 1.01325, 'equivalenceRatio', 0.5:0.01:5);
```

To close the problem, we maintain constant enthalpy and pressure. This problem type is denoted as HP in the Combustion Toolbox. By default, the code ensures that the enthalpy of the final state equals that of the initial state, so for this problem we do not need to specify additional parameters. Then, we can initialize the solver as follows:

```matlab
% Initialize equilibrium solver
solver = EquilibriumSolver('problemType', 'HP');
```

Finally, we can solve the problem and visualize the results:
```matlab
% Perform chemical calculations
solveArray(solver, mixArray);

% Postprocess results
report(solver, mixArray);
```

If everything goes well, the last promt should display the following message:

```matlab
*******************************************************
-------------------------------------------------------
Problem type: HP  | Equivalence ratio = 0.5000
-------------------------------------------------------
               |    MIXTURE 1
T [K]          |      1776.8223
p [bar]        |         1.0132
r [kg/m3]      |         0.2011
h [kJ/kg]      |       321.9942
e [kJ/kg]      |      -181.7991
g [kJ/kg]      |    -15487.8841
s [kJ/(kg-K)]  |         8.8978
W [g/mol]      |        29.3242
(dlV/dlp)T [-] |        -1.0000
(dlV/dlT)p [-] |         1.0017
cp [kJ/(kg-K)] |         1.3539
gamma [-]      |         1.2660
gamma_s [-]    |         1.2660
sound vel [m/s]|       798.6200
-------------------------------------------------------
MIXTURE 1               Xi [-]
N2                   7.7233e-01
O2                   1.0142e-01
CO2                  8.2220e-02
H2O                  4.0942e-02
NO                   2.6404e-03
OH                   3.6588e-04
CO                   4.1312e-05
O                    3.0817e-05
H2                   5.5205e-06
H                    6.8729e-07
N                    2.1015e-11
NH                   7.3009e-13
NH3                  3.5644e-13
NH2                  1.4186e-13
HCO                  1.7906e-14
MINORS[+10]          0.0000e+00

TOTAL                1.0000e+00
-------------------------------------------------------
*******************************************************

```

Two plots should also appear, illustrating the equilibrium composition of the system as a function of the equivalence ratio $\phi$, and various properties (temperature, pressure, density, enthalpy, internal energy, Gibbs free energy, entropy, and adiabatic index) of the products as a function of $\phi$.

:::{figure} /_static/img/chemical_equilibrium_2_fig1.svg
:name: fig_chemical_equilibrium_2_fig1
:width: 1000px
:align: center

Variation of molar fraction for an HP transformation in lean-to-rich acetylene ($\text{C}_2\text{H}_2$)-ideal air mixtures at standard conditions ($T_1 = 300$ K, $p_1 = 1$ bar).
:::


:::{figure} /_static/img/chemical_equilibrium_2_fig2.svg
:name: fig_chemical_equilibrium_2_fig2
:width: 1000px
:align: center

Variation of thermodynamic properties for an HP transformation in lean-to-rich acetylene ($\text{C}_2\text{H}_2$)-ideal air mixtures at standard conditions ($T_1 = 300$ K, $p_1 = 1$ bar).
:::


Combustion Toolbox performs the calculations from the last case to the first one.

````{tip}
The convergence tolerances for the algorithms implemented in the Combustion Toolbox are properties of their respective solvers. Default values are specified at the beggining of the class. For instance, the default tolerance for molar composition is $10^{-14}$, for the multi-dimensional Newton-Raphson solver (where temperature is known) it is $10^{-5}$, and for the Newton-Raphson solver (when temperature is not known) used to satisfy conservation equation for enthalpy, internal energy, or entropy, the tolerance is set to $10^{-3}$.

These parameters can be easily adjusted by setting the corresponding property in the solver. For example, to decrease the tolerance (increase precision) for molar composition to $10^{-32}$, type
```matlab
set(solver, 'tolMoles', 1e-32);
```
prior to solving the problem. To visualize these changes (command window and default plots), execute:
```matlab
config = PlotConfig();
config.tolMolesDisplay = 1e-32;
set(solver, 'plotConfig', config);
```
````

Here, {mat:class}`~src.+combustiontoolbox.+utils.+display.@PlotConfig.PlotConfig` is a class from `utils.display` subpacakge with configuration data for plots.

## Summary

```matlab
% Import packages
import combustiontoolbox.databases.NasaDatabase
import combustiontoolbox.core.*
import combustiontoolbox.equilibrium.*
import combustiontoolbox.utils.display.*

% Get Nasa database
DB = NasaDatabase();

% Define chemical system
system = ChemicalSystem(DB, 'soot formation');

% Initialize mixture
mix = Mixture(system);

% Define chemical state
set(mix, {'C2H2_acetylene'}, 'fuel', 1);
set(mix, {'N2', 'O2'}, 'oxidizer', [79/21, 1]);

% Define properties
mixArray = setProperties(mix, 'temperature', 300, 'pressure', 1 * 1.01325, 'equivalenceRatio', 0.5:0.01:5);

% Initialize solver
solver = EquilibriumSolver('problemType', 'HP');

% Solve problem
solver.solveArray(mixArray);

% Automatically postprocess results
report(solver, mixArray);
```