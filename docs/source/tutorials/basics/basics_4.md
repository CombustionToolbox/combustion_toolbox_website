# Defining initial state of a mixture

The initial state of a mixture (`reactants`) is defined by its chemical composition, temperature, and pressure. For this example, let's assume that we have a stoichiometric mixture of methane (CH$_4$) and ideal-air (79% N$_2$ and 21% O$_2$ in volume) at 300 K and 1 bar.


````{Note}
Importing the Combustion Toolbox (CT) subpackages and defining the database and chemical system are the first steps to start working with the code. To do that, type the following at the prompt:

```matlab
import combustiontoolbox.databases.NasaDatabase
import combustiontoolbox.core.*

DB = NasaDatabase();
chemicalSystem = ChemicalSystem(DB);
```
````

To define a mixture we need to create an instance of the {mat:class}`~src.+combustiontoolbox.+core.@Mixture.Mixture` class. This class contains the properties and methods to define the state of the mixture and requires the chemical system as input, thus
```matlab
mix = Mixture(chemicalSystem);
```
is used to create the {mat:class}`~src.+combustiontoolbox.+core.@Mixture.Mixture` object <tt>mix</tt>.

## Defining initial chemical species

In the Combustion Toolbox (CT), the chemical species of the initial mixture are categorized as follows:
* `Fuel`: chemical species considered as fuel.
* `Oxidizer`: chemical species that react with the fuel.
* `Inert`: chemical species that remain inert and do not react with the fuel or oxidizer, maintaining a frozen composition.
* `Unknown`: chemical species that are not classified.

Considering that all the species react, we can write at the prompt:

```matlab
set(mix, {'CH4'}, 'fuel', 1);
set(mix, {'N2', 'O2'}, 'oxidizer', [79/21, 1]);
```

## Defining initial composition

The above classification enables us to specify the chemical composition of a premixed combustion system using the equivalence ratio, defined as
```{eval-rst}
.. math::
    :nowrap:

    \begin{equation}
        \phi = \dfrac{ \text{fuel-oxidizer-ratio} }{ (\text{fuel-oxidizer-ratio})_{\text{st}} } = \dfrac{ n_{\text{fuel}} / n_{\text{oxidizer}} }{ \left( n_{\text{fuel}} / n_{\text{oxidizer}} \right)_{\text{st}}}.
    \end{equation}
```

Here, $n$ represents the number of moles, and the subscript `st` denotes the stoichiometric value. When $\phi = 1$, the mixture is said to be stoichiometric, i.e., the fuel and oxidizer are present in the exact proportions required for complete combustion. If $\phi < 1$ the mixture is said to be fuel-lean, and if $\phi > 1$ the mixture is said to be fuel-rich.

```{note}
The number of moles have to be specified in the same order as the corresponding set of species.
```

The initial composition can be defined with the number of moles $n_j$ of each chemical species in the mixture, or with the equivalence ratio $\phi$.


`````{tab-set}

````{tab-item} Number of moles
For a stoichiometric mixture of methane and ideal-air, we have $n_{\rm CH_4} = 1$, $n_{\rm O_2} = 2$, and $n_{\rm N_2} = 2 \cdot 79/21$. This can be defined as follows:

```matlab
set(mix, {'CH4'}, 'fuel', 1);
set(mix, {'N2', 'O2'}, 'oxidizer', 2 * [79/21, 1]);
```
where the factor 2 in front of the oxidizer moles represents the stoichiometric coefficient of the reaction.

````

````{tab-item} Equivalence ratio
For a stoichiometric mixture of methane and ideal-air, we have $\phi = 1$. Note, that to define the composition properly we have to specify the number of oxidizers moles relative to O$_2$. This can be done as follows:

```matlab
set(mix, {'CH4'}, 'fuel', 1);
set(mix, {'N2', 'O2'}, 'oxidizer', [79/21, 1]);
setEquivalenceRatio(mix, 'equivalenceRatio', 1);
```
where the vector [79/21, 1] represents the ratio of oxidizers moles relative to O$_2$ when the equivalence ratio is defined.
````

`````

````{tip}
There are calculations in which is not necessary to differentiate between fuel, oxidizer, and inert species. In those cases, we can just define them as:
    
```matlab
set(mix, {'CH4', 'N2', 'O2'}, [1, 2 * 79/21, 2]);
```

````

## Defining initial temperature and pressure

To define the initial temperature and pressure of the mixture, we can use the {mat:func}`~src.+combustiontoolbox.+core.@Mixture.Mixture.setProperties` method within the {mat:class}`~src.+combustiontoolbox.+core.@Mixture.Mixture` class, namely:

```matlab
mix = setProperties(mix, 'temperature', 300, 'pressure', 1);
```
or using the {mat:func}`~src.+combustiontoolbox.+core.@Mixture.Mixture.setTemperature` and {mat:func}`~src.+combustiontoolbox.+core.@Mixture.Mixture.setPressure` methods:
```matlab
setTemperature(mix, 300);
setpressure(mix, 1);
```

```{warning}
The `default units` for temperature and pressure are `K` and `bar`, respectively.
```


## Printing the state of the mixture
To print the state of the mixture, we can use the {mat:func}`~src.+combustiontoolbox.+core.@Mixture.print` method:
```matlab
print(mix);
```
which will yield the following output:
```matlab
***************************************
---------------------------------------
Equivalence ratio = 1.0000
---------------------------------------
               |    MIXTURE 1
T [K]          |       300.0000
p [bar]        |         1.0000
r [kg/m3]      |         1.1078
h [kJ/kg]      |      -254.5297
e [kJ/kg]      |      -344.7954
g [kJ/kg]      |     -2429.5892
s [kJ/(kg-K)]  |         7.2502
W [g/mol]      |        27.6333
(dlV/dlp)T [-] |        -1.0000
(dlV/dlT)p [-] |         1.0000
cp [kJ/(kg-K)] |         1.0786
gamma [-]      |         1.3869
gamma_s [-]    |         1.3869
sound vel [m/s]|       353.8198
---------------------------------------
MIXTURE 1               Xi [-]
N2                   7.1493e-01
O2                   1.9005e-01
CH4                  9.5023e-02
MINORS[+212]         0.0000e+00

TOTAL                1.0000e+00
---------------------------------------
***************************************
```

## Summary

`````{tab-set}

````{tab-item} Number of moles

```matlab
% Import packages
import combustiontoolbox.databases.NasaDatabase
import combustiontoolbox.core.*

% Define database
DB = NasaDatabase();

% Initialize chemical system
chemicalSystem = ChemicalSystem(DB);

% Initialize mixture
mix = Mixture(chemicalSystem);

% Define initial chemical species
set(mix, {'CH4'}, 'fuel', 1);
set(mix, {'N2', 'O2'}, 'oxidizer', 2 * [79/21, 1]);

% Define initial temperature and pressure
mix = setProperties(mix, 'temperature', 300, 'pressure', 1);

% Print the state of the mixture
print(mix);
```

````

````{tab-item} Equivalence ratio

```matlab
% Import packages
import combustiontoolbox.databases.NasaDatabase
import combustiontoolbox.core.*

% Define database
DB = NasaDatabase();

% Initialize chemical system
chemicalSystem = ChemicalSystem(DB);

% Initialize mixture
mix = Mixture(chemicalSystem);

% Define initial chemical species
set(mix, {'CH4'}, 'fuel', 1);
set(mix, {'N2', 'O2'}, 'oxidizer', [79/21, 1]);

% Define initial temperature, pressure, and equivalence ratio
mix = setProperties(mix, 'temperature', 300, 'pressure', 1, 'equivalenceRatio', 1);

% Print the state of the mixture
print(mix);
```

````

`````