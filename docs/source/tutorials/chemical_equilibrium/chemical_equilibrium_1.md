# Chemical equilibrium at constant temperature and pressure

As a first example, let's compute the equilibrium composition of a stoichiometric CH$_4$-ideal air mixture at 3000 K and 1.01325 bar (1 atm). To obtain the equilibrium composition, we have to define the chemical species that can appear in the final state. The combustion of typical hydrocarbon fuels, such as methane, is a complex process that involves hundreds of chemical species. However, the number of species that have a significant impact on the properties of the final mixture is much smaller. Combustion Toolbox provides a list of predefined species that can be used to compute the equilibrium composition of a mixture. The list of predefined species can be found in the routine `list_species.m`.

For a preliminary analysis, we will consider a set of 24 species:

* CO$_2$, CO, H$_2$O, H$_2$, O$_2$, N$_2$, C<sub>gr</sub>,
* C$_2$, C$_2$H$_4$, CH, CH, CH$_3$, CH$_4$, CN, H,
* HCN, HCO, N, NH, NH$_2$, NH$_3$, NO, O, OH,
  
which typically appear in the combustion of hydrocarbon fuels with air. This set of species is defined in the routine `list_species.m` as `Soot formation`, which also includes He and Ar. 


## Defining chemical system

```````{tab-set}
``````{tab-item} Plain code

To initialize the Combustion Toolbox (CT) with this set of species, type the following at the MATLAB prompt:

`````{tab-set}
````{tab-item} Predefined list of species
```matlab
self = App('Soot formation');
```
````

````{tab-item} Specifiying a custom list of species
```matlab
self = App({'CO2', 'CO', 'H2O', 'H2', 'O2', 'N2', 'Cbgrb', ...
            'C2', 'C2H4', 'CH', 'CH', 'CH3', 'CH4', 'CN', 'H', ...
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

## Setting the initial thermodynamic state
```````{tab-set}
``````{tab-item} Plain code
To indicate the temperature [K] and pressure [bar] of the initial mixture, type:
```matlab
self = set_prop(self, 'TR', 300, 'pR', 1 * 1.01325);
```

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
self.PD.S_Fuel     = {'CH4'};
self.PD.N_Fuel     = 1;
self.PD.S_Oxidizer = {'N2', 'O2'};
self.PD.N_Oxidizer = [7.52, 2];
```

This is the same as specifying a unit value for the equivalence ratio:
```matlab
self.PD.S_Fuel     = {'CH4'};
self.PD.S_Oxidizer = {'N2', 'O2'};
self.PD.ratio_oxidizers_O2 = [79, 21]/21;
self = set_prop(self, 'phi', 1);
```

The last two lines of code establish the proportion of the oxidizers species over O$_2$ and the equivalence ratio, respectively. The number of moles are calculated considering that the number of moles of fuel is one by default.
````

````{tab-item} Parametric study
For a lean-to-rich CH$_4$-ideal air mixtures:
```matlab
self.PD.S_Fuel     = {'CH4'};
self.PD.S_Oxidizer = {'N2', 'O2'};
self.PD.ratio_oxidizers_O2 = [79, 21]/21;
self = set_prop(self, 'phi', 0.5:0.01:4);
```

The last two lines of code establish the proportion of the oxidizers species over O$_2$ and the equivalence ratio, respectively. The number of moles are calculated considering that the number of moles of fuel is one by default.
````
`````

``````

``````{tab-item} GUI
`````{note}
This section is under development. Stay tuned!
`````

```````
## Set chemical transformation 

```````{tab-set}
``````{tab-item} Plain code
Depending on the problem you want to solve, you may need to configure additional inputs. In this case, to compute the equilibrium composition at the defined temperature and pressure (TP), we have to set these values as
```matlab
self = set_prop(self, 'pP', self.PD.pR.value, 'TP', 3000);
```

```{note}
Here, the pressure of the final state has been defined using the defined value of the initial state, `self.PD.pR.value`.
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
To solve the aforementioned problem, run
```matlab
self = solve_problem(self, 'TP');
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
The results are contained in `self.PS`. By default, `solve_problem.m` prints the results through the command window, which gives for the stoichiometric case (phi=1):
```matlab
COMPUTING Nº MOLES FROM EQUIVALENCE RATIO (PHI).
***********************************************************
-----------------------------------------------------------
Problem type: TP  | phi = 1.0000
-----------------------------------------------------------
               |    REACTANTS    |      PRODUCTS
T [K]          |       300.0000  |      3000.0000
p [bar]        |         1.0132  |         1.0132
r [kg/m3]      |         1.1225  |         0.1029
h [kJ/kg]      |      -254.5296  |      2574.2795
e [kJ/kg]      |      -344.7953  |      1589.5140
g [kJ/kg]      |     -2428.4002  |    -30246.9221
s [kJ/(kg-K)]  |         7.2462  |        10.9404
W [g/mol]      |        27.6333  |        25.3293
(dlV/dlp)T [-] |                 |        -1.0285
(dlV/dlT)p [-] |                 |         1.5830
cp [kJ/(kg-K)] |         1.0786  |         5.5609
gamma [-]      |         1.3869  |         1.1680
gamma_s [-]    |         1.3869  |         1.1357
sound vel [m/s]|       353.8198  |      1057.5349
-----------------------------------------------------------
REACTANTS               Xi [-]
N2                   7.1493e-01
O2                   1.9005e-01
CH4                  9.5023e-02
MINORS[+22]          0.0000e+00

TOTAL                1.0000e+00
-----------------------------------------------------------
PRODUCTS                Xi [-]
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
NH                   9.5805e-07
HCO                  1.2464e-07
NH2                  1.1860e-07
NH3                  3.0265e-08
HCN                  4.4103e-09
CN                   4.0110e-10
CH                   5.7109e-13
CH3                  1.5595e-13
CH4                  1.1358e-14
MINORS[+5]           0.0000e+00

TOTAL                1.0000e+00
-----------------------------------------------------------
***********************************************************
```

````{note}
The `solve_problem.m` function prints the results in the command window by default. To avoid this, write before:
```matlab
 self.Misc.FLAG_RESULTS = false
```

or modify its default value directly in `miscellaneous.m`.
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
There are some predefined charts based on the selected problem, in case you have calculated multiple cases. Just calling the routine
```matlab
post_results(self);
```
will reproduce **Figure 1**, which represents the variation of the molar fraction with the equivalence ratio for lean to rich CH$_4$-ideal air mixtures at 3000 [K] and 1.01325 [bar]. 

<p align="center">
    <img src="../../_static/img/Tutorial_1.svg" width="1000">
</p>

**Figure 1:** *Example TP: variation of molar fraction for lean to rich CH$_4$-ideal air mixtures at 3000 [K] and 1.01325 [bar], a set of 26 species considered and a total of 451 case studies. The computational time was of 2.39 seconds using a Intel(R) Core(TM) i7-11800H CPU @ 2.30GHz.*

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
% Initialize CT and define chemical system
self = App('Soot formation');

% Define initial chemical composition
self.PD.S_Fuel     = {'CH4'};
self.PD.S_Oxidizer = {'N2', 'O2'};
self.PD.ratio_oxidizers_O2 = [79, 21]/21;
self = set_prop(self, 'phi', 1);

% Define initial thermochemical state
self = set_prop(self, 'TR', 300, 'pR', 1 * 1.01325);

% Set chemical transformation
self = set_prop(self, 'pP', self.PD.pR.value, 'TP', 3000);

% Perform chemical calculations
self = solve_problem(self, 'TP');


```

````

````{tab-item} Parametric study

```matlab
% Initialize CT and define chemical system
self = App('Soot formation');

% Define initial chemical composition
self.PD.S_Fuel     = {'CH4'};
self.PD.S_Oxidizer = {'N2', 'O2'};
self.PD.ratio_oxidizers_O2 = [79, 21]/21;
self = set_prop(self, 'phi', 0.5:0.01:4);

% Define initial thermochemical state
self = set_prop(self, 'TR', 300, 'pR', 1 * 1.01325);

% Set chemical transformation
self = set_prop(self, 'pP', self.PD.pR.value, 'TP', 3000);

% Perform chemical calculations
self = solve_problem(self, 'TP');

% Postprocess results
post_results(self);
```

````

`````


## Congratulations!
Congratulations you have finished the Combustion Toolbox MATLAB tutorial! You should now be ready to begin using the Combustion Toolbox on your own (see the `examples` folder).