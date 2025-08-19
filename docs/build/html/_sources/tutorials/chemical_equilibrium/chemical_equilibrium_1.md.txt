# Chemical equilibrium at constant temperature and pressure

Following the example used in the preciding section, let's compute the equilibrium composition of a stoichiometric CH$_4$-ideal air mixture at 3000 K and 1.01325 bar (1 atm). To obtain the equilibrium composition, we have to define the chemical species that can appear in the final state. The combustion of typical hydrocarbon fuels, such as methane, is a complex process that involves hundreds of chemical species. However, the number of species that have a significant impact on the properties of the final mixture is much smaller. Combustion Toolbox provides a list of predefined species that can be used to compute the equilibrium composition of a mixture. The list of predefined species can be found in the routine {mat:func}`~src.+combustiontoolbox.+core.@ChemicalSystem.setListSpecies`. Alternatively, refer to the [Using predefined chemical systems](https://combustion-toolbox-website.readthedocs.io/en/latest/tutorials/basics/basics_4.html#using-predefined-chemical-systems) tutorial section.

For a preliminary analysis, we will consider a set of 23 species:

* CO$_2$, CO, H$_2$O, H$_2$, O$_2$, N$_2$, C<sub>gr</sub>,
* C$_2$, C$_2$H$_4$, CH, CH$_3$, CH$_4$, CN, H,
* HCN, HCO, N, NH, NH$_2$, NH$_3$, NO, O, OH,
  
which typically appear in the combustion of hydrocarbon fuels with air. This set of species is defined in the routine {mat:func}`~src.+combustiontoolbox.+core.@ChemicalSystem.setListSpecies` as `Soot formation`, which also includes Ar.

## Import packages

```matlab
import combustiontoolbox.databases.NasaDatabase
import combustiontoolbox.core.*
import combustiontoolbox.equilibrum.*
import combustiontoolbox.utils.display.*
```


## Define database

```````{tab-set}
``````{tab-item} Plain code
To define the database type the following at the MATLAB prompt:

```matlab
DB = NasaDatabase()
```

Here DB is a {mat:class}`~src.+combustiontoolbox.+databases.@NasaDatabase.NasaDatabase` object that inherits from the superclass {mat:class}`~src.+combustiontoolbox.+databases.@Database.Database`.
``````

``````{tab-item} GUI
`````{note}
This section is under development. Stay tuned!
`````

```````

## Defining chemical system

```````{tab-set}
``````{tab-item} Plain code

To initialize the Combustion Toolbox (CT) with this set of species, type the following at the MATLAB prompt:

`````{tab-set}
````{tab-item} Predefined list of species
```matlab
chemicalSystem = ChemicalSystem(DB, 'soot formation');
```
````

````{tab-item} Specifiying a custom list of species
```matlab
chemicalSystem = ChemicalSystem(DB, {'CO2', 'CO', 'H2O', 'H2', 'O2', 'N2', 'Cbgrb', ...
            'C2', 'C2H4', 'CH', 'CH3', 'CH4', 'CN', 'H', ...
            'HCN', 'HCO', 'N', 'NH', 'NH2', 'NH3', 'NO', 'O', 'OH'});
```
````
`````


``````

``````{tab-item} GUI
`````{note}
This section is under development. Stay tuned!
`````

```````

## Setting the initial chemical composition

```````{tab-set}
``````{tab-item} Plain code
To indicate the species and chemical composition in the initial mixture:
`````{tab-set}
````{tab-item} Individual study
For a stochiometric CH$_4$-ideal air mixture:
```matlab
set(mix, {'CH4'}, 'fuel', 1);
set(mix, {'N2', 'O2'}, 'oxidizer', [7.52, 2]);
```

This is the same as specifying a unit value for the equivalence ratio:
```matlab
set(mix, {'CH4'}, 'fuel', 1);
set(mix, {'N2', 'O2'}, 'oxidizer', [79/21, 1]);
setEquivalenceRatio(mix, 1);
```

````

````{tab-item} Parametric study
For a lean-to-rich CH$_4$-ideal air mixtures:
```matlab
set(mix, {'CH4'}, 'fuel', 1);
set(mix, {'N2', 'O2'}, 'oxidizer', [79/21, 1]);
mixArray = setProperties(mix, 'equivalenceRatio', 0.5:0.01:4);
```

````
`````

``````

``````{tab-item} GUI
`````{note}
This section is under development. Stay tuned!
`````

```````

## Setting the initial thermodynamic state
```````{tab-set}
``````{tab-item} Plain code
To indicate the temperature [K] and pressure [bar] of the initial mixture, type:
```matlab
mix = Mixture(chemicalSystem);
setTemperature(mix, 3000);
setPressure(mix, 1 * 1.01325);
```

``````

``````{tab-item} GUI
`````{note}
This section is under development. Stay tuned!
`````

```````

## Define solver 

```````{tab-set}
``````{tab-item} Plain code
In this example, we have a constant temperature and pressure (TP) problem. To solve it, we need to use the {mat:class}`~src.+combustiontoolbox.+equilibrium.@EquilibriumSolver.EquilibriumSolver` class, which is defined as follows:
```matlab
solver = EquilibriumSolver('TP');
```

``````

``````{tab-item} GUI
`````{note}
This section is under development. Stay tuned!
`````

```````

## Perform chemical calculations

```````{tab-set}
``````{tab-item} Plain code
To solve parametrics studies, all the solvers implemented in CT have a method called {mat:func}`~src.+combustiontoolbox.+equilibrium.@EquilibriumSolver.EquilibriumSolver.solveArray`, which allows you to solve a set of cases at once. To solve the parametric study defined above, run
```matlab
solver.solveArray(mixArray);
```

``````

``````{tab-item} GUI
`````{note}
This section is under development. Stay tuned!
`````

```````

## Results

```````{tab-set}
``````{tab-item} Plain code
The mixArray handle will be updated with the new state. By default, all the solvers implemented the Combustion Toolbox print the results through the command window, which gives for the stoichiometric case ($\phi$ = 1):

```matlab
****************************************************
----------------------------------------------------
Problem type: TP  | Equivalence ratio = 1.0000
----------------------------------------------------
               |    MIXTURE 1
T [K]          |      3000.0000
p [bar]        |         1.0132
r [kg/m3]      |         0.1029
h [kJ/kg]      |      2574.2794
e [kJ/kg]      |      1589.5140
g [kJ/kg]      |    -30246.9319
s [kJ/(kg-K)]  |        10.9404
W [g/mol]      |        25.3293
(dlV/dlp)T [-] |        -1.0285
(dlV/dlT)p [-] |         1.5830
cp [kJ/(kg-K)] |         5.5609
gamma [-]      |         1.1680
gamma_s [-]    |         1.1357
sound vel [m/s]|      1057.5349
----------------------------------------------------
MIXTURE 1               Xi [-]
N2                   6.4771e-01
H2O                  1.1162e-01
CO                   5.8485e-02
OH                   3.5936e-02
H2                   3.0822e-02
CO2                  2.8615e-02
H                    2.7583e-02
O2                   2.5914e-02
O                    1.8096e-02
NO                   1.5206e-02
N                    1.1123e-05
NH                   9.5804e-07
HCO                  1.2464e-07
NH2                  1.1860e-07
NH3                  3.0265e-08
HCN                  4.4103e-09
CN                   4.0110e-10
CH                   5.7109e-13
CH3                  1.5595e-13
CH4                  1.1358e-14
MINORS[+4]           0.0000e+00

TOTAL                1.0000e+00
----------------------------------------------------
****************************************************
```

````{note}
The solve and solveArray methods of all the solvers implemented in CT print the results in the command window by default. To avoid this, during the definition write:
```matlab
solver = EquilibriumSolver('TP', 'FLAG_RESULTS', false);
```
or alternatively
```matlab
set(solver, 'FLAG_RESULTS', false);
```


````

``````

``````{tab-item} GUI
`````{note}
This section is under development. Stay tuned!
`````

```````

## Postprocessed results (predefined plots for several cases)

```````{tab-set}
``````{tab-item} Plain code
There are some predefined charts based on the selected problem, in case you have calculated multiple cases. Just calling the solvers method {mat:func}`~src.+combustiontoolbox.+equilibrium.@EquilibriumSolver.EquilibriumSolver.report`, namely
```matlab
report(solver, mixArray);
```
will reproduce {numref}`fig_molar_fraction_chemical_equilibrium_1`, which represents the variation of the molar fraction with the equivalence ratio for lean to rich CH$_4$-ideal air mixtures at 3000 K and 1.01325 bar. 

:::{figure} ../../_static/img/Tutorial_1.svg
:name: fig_molar_fraction_chemical_equilibrium_1
:width: 1000px
:align: center

Variation of molar fraction for lean to rich CH$_4$-ideal air mixtures at 3000 K and 1.01325 bar, a set of 26 species considered and a total of 451 case studies. The computational time was of 2.39 seconds using a Intel(R) Core(TM) i7-11800H CPU @ 2.30GHz.
:::

``````

``````{tab-item} GUI
`````{note}
This section is under development. Stay tuned!
`````

```````

## Summary

`````{tab-set}

````{tab-item} Individual study

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
mix = setProperties(mix, 'temperature', 3000, 'pressure', 1 * 1.01325, 'equivalenceRatio', 1);

% Initialize solver
solver = EquilibriumSolver('problemType', 'TP');

% Solve problem
solver.solveArray(mix);

```

````

````{tab-item} Parametric study

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

% Initialize solver
solver = EquilibriumSolver('problemType', 'TP');

% Solve problem
solver.solveArray(mixArray);

% Automatically postprocess results
report(solver, mixArray);
```

````

`````