# Database

Combustion Toolbox generates its own databases taking into account the NASA-9 polynomials fitting to evaluate the thermodynamic functions of the species for the specific heat, enthalpy, and entropy as function of temperature, namely

```{eval-rst}
.. math::
    :nowrap:

    \begin{eqnarray}
        C_p^\circ/R &=& a_1T^{-2} + a_2T^{-1} + a_3 + a_4T + a_5T^2 + a_6T^3 + a_7T^4,\\
        H^\circ/R   &=& -a_1T^{-2} + a_2T^{-1} \ln{T} + a_3 + a_4T/2  + a_5T^2/3 + a_6T^3/4 \\
                    &\phantom{{}={}}& + a_7T^4/5 + a_8/T,\\
        S^\circ/R   &=& -a_1T^{-2}/2 - a_2T^{-1} + a_3\ln{T} + a_4T  + a_5T^2/2 + a_6T^3/3 \\
                    &\phantom{{}={}}& + a_7T^4/4 + a_9,
    \end{eqnarray}

```

where $a_i$ from $i=1, \dots, 7$ are the temperature coefficients and from $i =8, 9$ the integration constants, respectively. Depending of the species the polynomials fit up to 20000 K [1]. These values are available in the [source code](https://github.com/AlbertoCuadra/combustion_toolbox/blob/master/Databases/thermo.inp) and can be also obtained from [NASA's thermo build website](https://cearun.grc.nasa.gov/ThermoBuild/). 

This data is collected and formatted into a more accessible structure. We can distinguish from:

* DB_master: structured database from NASA's thermo file.
* DB: structured database with custom thermodynamic functions for faster data access.

This allows to evaluate the thermodynamic functions, e.g., the Gibbs energy [kJ/mol] function, and the thermal enthalpy of $\text{CO}_2$ at $T = 2000 \text{ K}$  with these simple callbacks

```matlab
>> g0_CO2  = species_g0('CO2', 2000, DB)
>> DhT_CO2 = species_DhT('CO2', 2000, DB) 
```

Another important parameter comes from the conservation of mass, which is the stoichiometric matrix $A_0$, by generalizing this constraint condition we have

```{eval-rst}
.. math::
    :nowrap:

    \begin{equation}
        \sum\limits_{j = 1}^{\text{NS}} a_{ij} n_j - b_i^\circ = 0,
    \end{equation}
```

or in matricial form

```{eval-rst}
.. math::
    :nowrap:

    \begin{equation}
        \underbrace{\left(\begin{array}{c c c c}
        a_{11} & a_{21} & \cdots & a_{\text{NS}1} \\
        a_{12} & a_{22} & \cdots & a_{\text{NS}2} \\
        \vdots & \vdots &  & \vdots \\
        a_{1\text{NE}} & a_{2\text{NE}} & \cdots & a_{\text{NS}\text{NE}} \\
        \end{array}\right)}_{\mathbf{A^T}}
        \underbrace{\left(\begin{matrix}
            \ce{n_1}\\
            \ce{n_2}\\
            \ce{\vdots}\\
            \ce{n_{\text{NS}}}
            \end{matrix}\right)}_{\mathbf{N}}
        - \underbrace{\left(\begin{matrix}
            \ce{b_1}\\
            \ce{b_2}\\
            \ce{\vdots}\\
            \ce{b_{\text{NE}}}
            \end{matrix}\right)}_{\mathbf{b^\circ}} = 0,
    \end{equation}

```

where $a_{ij}$ are the stoichiometric coefficients of the species, which represent the number of atoms of element $i$ per mole of species $j$. The number of moles and the total number of atoms of the $j$ species and $i$ element reads $n_j$ and $b_i$, respectively. This is computed during the initialization of the variable `self`. Using one of the predefined list of species, e.g., `soot formation`, this can be initializate as

```matlab
self = App('soot formation')
```

A simple test can be performed by considering the global exothermic reaction of hydrogen bromide

```{eval-rst}
.. math::
    :nowrap:

    \begin{equation}
        \text{H}_2 + \text{Br}_2 \rightleftharpoons 2\text{HBr}.
    \end{equation}
```

The stochiometric matrix in this case is 

```{eval-rst}
.. math::
    :nowrap:

    \begin{equation}
        \left(\begin{array}{c c c}
        0 & 2 & 1\\
        2 & 0 & 1\\
        \end{array}\right)
        \left(\begin{matrix}
            n_{\ce{H_2}}\\
            n_{\ce{Br_2}}\\
            n_{\ce{HBr}}\\
            \end{matrix}\right)
        - \left(\begin{matrix}
            b_{\ce{Br}}^\circ\\
            b_{\ce{H}}^\circ\\
            \end{matrix}\right) = 0.
    \end{equation}
```

A quick check using Combustion Toolbox:

```matlab
>> self = App({'H2', 'Br2', 'HBr'});
>> print_stochiometric_matrix(self, 'transpose')
```

 ```matlab
Transpose stochiometric matrix:

          H2    Br2    HBr
          __    ___    ___

    BR    0      2      1 
    H     2      0      1 
 ```


***

Routines

```{note}
We are still documenting these functions.
```

***

1. B. J. McBride, NASA Glenn coefficients for calculating thermodynamic
properties of individual species, National Aeronautics and Space Ad-
ministration, John H. Glenn Research Center, 2002.