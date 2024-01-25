# Defining initial state of a mixture

The initial state of a mixture (`reactants`) is defined by its chemical composition, temperature, and pressure. For this example, let's assume that we have a stoichiometric mixture of methane (CH$_4$) and ideal-air (79% N$_2$ and 21% O$_2$ in volume) at 300 K and 1 bar.


````{tip}
Remember, that initializing the Combustion Toolbox (CT) is the first step to start working with the code. To do that, type the following at the prompt:

```matlab
self = App();
```
````


## Defining initial chemical species

In the Combustion Toolbox (CT), the chemical species of the initial mixture are categorized as follows:
* `Fuel`: chemical species considered as fuel.
* `Oxidizer`: chemical species that react with the fuel.
* `Inert`: chemical species that remain inert and do not react with the fuel or oxidizer, maintaining a frozen composition.

Considering that all the species react, we can write at the prompt:

```matlab
self.PD.S_Fuel     = {'CH4'};
self.PD.S_Oxidizer = {'N2', 'O2'};
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
self.PD.N_Fuel = 1;
self.PD.N_Oxidizer = 2 * [1, 79/21];
```
where the factor 2 in front of the oxidizer is due to the stoichiometric coefficients of the reaction.

````

````{tab-item} Equivalence ratio
For a stoichiometric mixture of methane and ideal-air, we have $\phi = 1$. However, we have to specify the number of moles of oxidizers relative to O$_2$ to define the composition properly, thus

```matlab
self = set_prop(self, 'phi', 1);
self.PD.ratio_oxidizers_O2 = [79, 21] / 21;
```

````

`````

```{tip}
There are chemical calculations in which is not necessary to differentiate between fuel, oxidizer, and inert species. In those cases, we can just consider all the species as fuel and provide their corresponding number of moles.
```

## Defining initial temperature and pressure

To define the initial temperature and pressure of the mixture, we can use the <tt>set_prop.m</tt> function as follows:

```matlab
self = set_prop(self, 'TR', 300, 'pR', 1);
```

```{warning}
The `default units` for temperature and pressure are `K` and `bar`, respectively.
```

## Summary

`````{tab-set}

````{tab-item} Number of moles

```matlab
% Initialize CT
self = App();
% Define initial chemical species
self.PD.S_Fuel     = {'CH4'};
self.PD.S_Oxidizer = {'N2', 'O2'};
% Define initial composition (in moles)
self.PD.N_Fuel = 1;
self.PD.N_Oxidizer = 2 * [1, 79/21];
% Define initial temperature and pressure
self = set_prop(self, 'TR', 300, 'pR', 1);
```

````

````{tab-item} Equivalence ratio

```matlab
% Initialize CT
self = App();
% Define initial chemical species
self.PD.S_Fuel     = {'CH4'};
self.PD.S_Oxidizer = {'N2', 'O2'};
% Define initial composition (with equivalence ratio)
self = set_prop(self, 'phi', 1);
self.PD.ratio_oxidizers_O2 = [79, 21] / 21;
% Define initial temperature and pressure
self = set_prop(self, 'TR', 300, 'pR', 1);
```

````

`````

