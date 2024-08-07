# Defining chemical system

The chemical system encompasses all chemical species that may be involved in the system. To define it, we use the {mat:class}`~src.+combustiontoolbox.+core.@ChemicalSystem.ChemicalSystem` class from the core subpackage, which can be imported as follows:
```matlab
import combustiontoolbox.core.*
```
or directly as
```matlab
import combustiontoolbox.core.ChemicalSystem
```

This system requires information from the thermodynamic database used. For instance, using NASA's database, we can define the chemical system as demonstrated below:
```matlab
% Import packages
import combustiontoolbox.databases.NasaDatabase
import combustiontoolbox.core.*

% Define database
DB = NasaDatabase();

% Define chemical system
chemicalSystem = ChemicalSystem(DB);
```

As a canonical example, let's establish the chemical system for the complete combustion of a stoichiometric CH$_4$-ideal air mixture, represented by the global reaction
```{eval-rst}
.. math::
    :nowrap:

    \begin{equation}
        \underbrace{\text{CH}_4 + 2 (\text{O}_2 + 3.76 \text{N}_2)}_{\rm{reactants\ (initial\ state)}} \rightleftharpoons \underbrace{\text{CO}_2 + 2 \text{H}_2\text{O} + 7.52 \text{N}_2}_{\rm{products\ (final\ state)}}.
    \end{equation}

```
where CO$_2$, H$_2$O, and N$_2$ represents the products and CH$_4$, O$_2$, and N$_2$ the reactants. To define the products in the chemical system, we can write at the prompt:
```matlab
chemicalSystem = ChemicalSystem(DB, {'N2', 'CO2', 'H2O'});
```

```{note}
The list of species defined in the chemical system includes only the reaction products at equilibrium. However, as previously mentioned, the reactants are also part of the system. The {mat:func}`~src.+combustiontoolbox.+core.@ChemicalSystem.ChemicalSystem` class automatically incorporates these reactants for internal calculations, but they will not be considered as reactives species. This allows us to precisely define the products that may appear in the system at equilibrium.
```

## Identifying all possible products

Thermochemical transformations typically entail numerous chemical species, and occasionally we lack prior knowledge of all relevant species in the system. In such cases, we can recall in {mat:func}`~src.+combustiontoolbox.+core.@ChemicalSystem.findProducts` routine introduced in [*Accessing the databases*](https://combustion-toolbox-website.readthedocs.io/en/latest/tutorials/basics/basics_2.html#.md#accessing-the-databases). This routine allows us to identify all potential chemical species resulting from a chemical transformation (products), given a set of species (reactants). For this example, we can write at the prompt:

```matlab
listSpecies = findProducts(chemicalSystem, {'CH4', 'O2', 'N2'})
```

This will yield a list of over 200 chemical species. By default, the {mat:func}`~src.+combustiontoolbox.+core.@ChemicalSystem.findProducts` function scans for species in the database, including the condensed species and excluding the ionized species. To search for species in Burcat's database and include ionized species, we have to enable the `flag_burcat` and `flag_ion` options, setting both to `true`, as follows:
```matlab
listSpecies = findProducts(chemicalSystem, {'CH4', 'O2', 'N2'}, 'flag_burcat', true, 'flag_ion', true);
```
generating a list of +1000 chemical species.

````{tip}
In cases where no chemical system is defined, CT automatically identifies all potential products given a set of reactants, i.e., it uses the {mat:func}`~src.+combustiontoolbox.+core.@ChemicalSystem.findProducts` routine to construct the chemical system, taking into account the default flag values `flag_burcat`, `flag_ion`, `flag_condensed` defined in <tt>Species.m</tt>.
````

## Using predefined chemical systems

The Combustion Toolbox incorporates a range of predefined chemical systems, outlined in the {mat:func}`~src.+combustiontoolbox.+core.@ChemicalSystem.setListSpecies` routine. For example, some of the predefined chemical systems are defined below:

`````{tab-set}

````{tab-item} Air

* Calculations for air.
* Neglects ionization of chemical species.

```matlab
listSpecies = setListSpecies(chemicalSystem, 'air');
```

Chemical species included:
```matlab
listSpecies = {'CO2', 'CO', 'O2', 'N2', 'Ar', 'O', 'O3', ...
             'N', 'NO', 'NO2', 'NO3', 'N2O', 'N2O3', ...
             'N2O4', 'N3', 'C'};
```

````

````{tab-item} Air ions

* Calculations for air.
* Considers ionization of chemical species.

```matlab
listSpecies = setListSpecies(chemicalSystem, 'air ions');
```

Chemical species included:
```matlab
listSpecies = {'eminus', 'Ar', 'Arplus', 'C', 'Cplus', 'Cminus', ...
             'CN', 'CNplus', 'CNminus', 'CNN', 'CO', 'COplus', ...
             'CO2', 'CO2plus', 'C2', 'C2plus', 'C2minus', 'CCN', ...
             'CNC', 'OCCN', 'C2N2', 'C2O', 'C3', 'C3O2', 'N', ...
             'Nplus', 'Nminus', 'NCO', 'NO', 'NOplus', 'NO2', ...
             'NO2minus', 'NO3', 'NO3minus', 'N2', 'N2plus', ...
             'N2minus', 'NCN', 'N2O', 'N2Oplus', 'N2O3', 'N2O4', ...
             'N2O5', 'N3', 'O', 'Oplus', 'Ominus', 'O2', 'O2plus', ...
             'O2minus', 'O3'};
```

````

````{tab-item} HC/O2/N2

* Calculations for hydrocarbon (HC) combustion in air.
* Neglects most dissociation chemical species and excludes ions.

```matlab
listSpecies = setListSpecies(chemicalSystem, 'HC/O2/N2');
```


Chemical species included:
```matlab
listSpecies = {'CO2', 'CO', 'H2O', 'H2', 'O2', 'N2', 'Ar'}
```

````

````{tab-item} Soot formation

* Calculations for hydrocarbon (HC) combustion in air.
* Considers soot formation and a small set of minor species.
* Excludes ionized chemical species.

```matlab
listSpecies = setListSpecies(chemicalSystem, 'soot formation');
```

Chemical species included:
```matlab
listSpecies = {'CO2', 'CO', 'H2O', 'H2', 'O2', 'N2', 'Ar', 'Cbgrb', ...
             'C2', 'C2H4', 'CH', 'CH', 'CH3', 'CH4', 'CN', 'H', ...
             'HCN', 'HCO', 'N', 'NH', 'NH2', 'NH3', 'NO', 'O', 'OH'};
```

````

````{tab-item} Soot formation extended

* Calculations for hydrocarbon (HC) combustion in air.
* Considers soot formation and a large set of minor species.
* Excludes ionized chemical species.

```matlab
listSpecies = setListSpecies(chemicalSystem, 'soot formation extended');
```

Chemical species included:
```matlab
listSpecies = {'CO2', 'CO', 'H2O', 'H2', 'O2', 'N2', 'Ar', 'Cbgrb', ...
             'C2', 'C2H', 'C2H2_acetylene', 'C2H2_vinylidene', ...
             'C2H3_vinyl', 'C2H4', 'C2H5', 'C2H5OH', 'C2H6', ...
             'C2N2', 'C2O', 'C3', 'C3H3_1_propynl', ...
             'C3H3_2_propynl', 'C3H4_allene', 'C3H4_propyne', ...
             'C3H5_allyl', 'C3H6O_acetone', 'C3H6_propylene', ...
             'C3H8', 'C4', 'C4H2_butadiyne', 'C5', 'C6H2', 'C6H6', ...
             'C8H18_isooctane', 'CH', 'CH2', 'CH2CO_ketene', ...
             'CH2OH', 'CH3', 'CH3CHO_ethanal', 'CH3CN', ...
             'CH3COOH', 'CH3O', 'CH3OH', 'CH4', 'CN', 'COOH', 'H', ...
             'H2O2', 'HCCO', 'HCHO_formaldehy', 'HCN', 'HCO', ...
             'HCOOH', 'HNC', 'HNCO', 'HNO', 'HO2', 'N', 'N2O', ...
             'NCO', 'NH', 'NH2', 'NH2OH', 'NH3', 'NO', 'NO2', ...
             'O', 'OCCN', 'OH', 'C3O2', 'C4N2', 'CH3CO_acetyl', ...
             'C4H6_butadiene', 'C4H6_1butyne', 'C4H6_2butyne', ...
             'C2H4O_ethylen_o', 'CH3OCH3', 'C4H8_1_butene', ...
             'C4H8_cis2_buten', 'C4H8_isobutene', ...
             'C4H8_tr2_butene', 'C4H9_i_butyl', 'C4H9_n_butyl', ...
             'C4H9_s_butyl', 'C4H9_t_butyl', 'C6H5OH_phenol', ...
             'C6H5O_phenoxy', 'C6H5_phenyl', 'C7H7_benzyl', ...
             'C7H8', 'C8H8_styrene', 'C10H8_naphthale'};
```

````

````{tab-item} HC/O2/N2 propellants

* Calculations for hydrocarbon (HC) combustion (propellants) in air.
* Considers soot formation and a large set of minor species.
* Excludes ionized chemical species.

```matlab
listSpecies = setListSpecies(chemicalSystem, 'HC/O2/N2 propellants');
```

Chemical species included:
```matlab
listSpecies = {'CO2', 'CO', 'H2O', 'H2', 'O2', 'N2', 'Ar', 'Cbgrb', ...
             'C2', 'C2H', 'C2H2_acetylene', 'C2H2_vinylidene', ...
             'C2H3_vinyl', 'C2H4', 'C2H5', 'C2H5OH', 'C2H6', ...
             'C2N2', 'C2O', 'C3', 'C3H3_1_propynl', ...
             'C3H3_2_propynl', 'C3H4_allene', 'C3H4_propyne', ...
             'C3H5_allyl', 'C3H6O_acetone', 'C3H6_propylene', ...
             'C3H8', 'C4', 'C4H2_butadiyne', 'C5', 'C6H2', 'C6H6', ...
             'C8H18_isooctane', 'CH', 'CH2', 'CH2CO_ketene', ...
             'CH2OH', 'CH3', 'CH3CHO_ethanal', 'CH3CN', ...
             'CH3COOH', 'CH3O', 'CH3OH', 'CH4', 'CN', 'COOH', 'H', ...
             'H2O2', 'HCCO', 'HCHO_formaldehy', 'HCN', 'HCO', ...
             'HCOOH', 'HNC', 'HNCO', 'HNO', 'HO2', 'N', 'N2O', ...
             'NCO', 'NH', 'NH2', 'NH2OH', 'NH3', 'NO', 'NO2', ...
             'O', 'OCCN', 'OH', 'C3O2', 'C4N2', 'RP_1', 'H2bLb', ...
             'O2bLb'};
```

````

````{tab-item} Si/HC/O2/N2 propellants

* Calculations for Silicon (Si) combustion (propellants) in air.
* Considers soot formation and a minor set of minor species.
* Excludes ionized chemical species.

```matlab
listSpecies = setListSpecies(chemicalSystem, 'Si/HC/O2/N2 propellants');
```

Chemical species included:
```matlab
listSpecies = {'CO2', 'CO', 'H2O', 'H2', 'O2', 'N2', 'Ar', 'Cbgrb', ...
             'C2', 'C2H4', 'CH', 'CH', 'CH3', 'CH4', 'CN', 'H', ...
             'H2O2', 'HCN', 'HCO', 'N', 'NH', 'NH2', 'NH3', 'NO', 'O', 'OH', ...
             'O2bLb', 'Si', 'SiH', 'SiH2', 'SiH3', 'SiH4', 'SiO2', 'SiO', ...
             'SibLb', 'SiO2bLb', 'Si2'};
```

````

`````

## Summary

`````{tab-set}

````{tab-item} Automatic selection of products

```matlab
% Import packages
import combustiontoolbox.databases.NasaDatabase
import combustiontoolbox.core.*

% Define database
DB = NasaDatabase();

% Define chemical system
chemicalSystem = ChemicalSystem(DB);
```

````

````{tab-item} Using predefined chemical system

```matlab
% Import packages
import combustiontoolbox.databases.NasaDatabase
import combustiontoolbox.core.*

% Define database
DB = NasaDatabase();

% Define chemical system
chemicalSystem = ChemicalSystem(DB, {'HC/O2/N2'});
```

````

`````