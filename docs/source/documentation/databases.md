# Databases

Combustion Toolbox generates its own databases taking into account the NASA-9 polynomials fitting to evaluate the dimensionless thermodynamic functions of the species for the specific heat, enthalpy, and entropy as function of temperature, namely

```{eval-rst}
.. math::
    :nowrap:

    \begin{eqnarray}
        c_p^\circ/R &=& a_1T^{-2} + a_2T^{-1} + a_3 + a_4T + a_5T^2 + a_6T^3 + a_7T^4,\\
        h^\circ/RT   &=& -a_1T^{-2} + a_2T^{-1} \ln{T} + a_3 + a_4T/2  + a_5T^2/3 + a_6T^3/4 \\
                    &\phantom{{}={}}& + a_7T^4/5 + a_8/T,\\
        s^\circ/R   &=& -a_1T^{-2}/2 - a_2T^{-1} + a_3\ln{T} + a_4T  + a_5T^2/2 + a_6T^3/3 \\
                    &\phantom{{}={}}& + a_7T^4/4 + a_9,
    \end{eqnarray}
```

where $a_i$ from $i=1, \dots, 7$ are the temperature coefficients and $i =8, 9$ are the integration constants, respectively. Depending of the species the polynomials fit up to 20000 K [1]. These values are available in the [source code](https://github.com/AlbertoCuadra/combustion_toolbox/blob/master/Databases/thermo.inp) and can be also obtained from [NASA's thermo build website](https://cearun.grc.nasa.gov/ThermoBuild/). 

To compute the dimensionless Gibbs energy, $g_i^\circ (T) / RT$, from NASA's polynomials we use the next expression 
```{eval-rst}
.. math::
    :nowrap:

    \begin{equation}
        g_i^\circ/RT = h^\circ/RT - s^\circ/R,
    \end{equation}
```
or equivalently 

```{eval-rst}
.. math::
    :nowrap:

    \begin{eqnarray}
        g_i^\circ/RT &=& -a_1T^{-2}/2 + a_2T^{-1} (1 + \ln{T}) + a_3(1 - \ln{T}) - a_4T/2 - a_5T^2/6 - a_6T^3/12 \\
                    &\phantom{{}={}}& - a_7T^4/20 + a_8/T - a_9.
    \end{eqnarray}
```


This data is collected and formatted into a more accessible structure. We can distinguish from:

* `DB_master`: structured database from NASA's thermo file.
* `DB`: structured database with piecewise cubic Hermite interpolating polynomials and linear extrapolation for faster data access.

The use of piecewise cubic Hermite interpolating polynomials increments the performance of Combustion Toolbox in approximate 200% as shown in **Figure 1** obtaining the same results as seen  in **Figure 2**. To evaluate the thermodynamic functions, e.g., the Gibbs energy [kJ/mol] function, or the thermal enthalpy [kJ/mol] of $\text{CO}_2$ at $T = 2000 \text{ K}$ is as simple as using these callbacks

```matlab
>> g0_CO2  = species_g0('CO2', 2000, DB)
>> DhT_CO2 = species_DhT('CO2', 2000, DB) 
```

<p class= "only-light" align="center">
    <img alt="Performance thermo" style="border-width:0" src="..\_static\img\performance_thermo.svg" width="800"/>
</p>

<p class= "only-dark" align="center">
    <img alt="Performance thermo" style="border-width:0" src="..\_static\img\performance_thermo_dark.svg" width="800"/>
</p>

**Figure 1:** *Performance test, execution times for over $10^5$ calculations of the specific heat at constant pressure, enthalpy, Gibbs energy, and entropy, denoted as $c_p$, $h_0$, $g_0$, and $s_0$, respectively, using the NASA's 9 coefficient polynomials (dark blue) and the piecewise cubic Hermite interpolating polynomials (teal). The test has been carried out with an Intel(R) Core(TM) i7-8700 CPU @ 3.20GHz. Note: lower is better.*

<p class= "only-light" align="center">
    <img alt="Validation thermo" style="border-width:0" src="..\_static\img\validation_thermo.svg" width="800"/>
</p>

<p class= "only-dark" align="center">
    <img alt="Validation thermo" style="border-width:0" src="..\_static\img\validation_thermo_dark.svg" width="800"/>
</p>

**Figure 2:** *Comparison of entropy  [kJ/(mol-K)] as a function of temperature [K] obtained using the piecewise cubic Hermite interpolating polynomials (lines) and using the NASA's 9 coefficient polynomials (symbols) for a set of species.*

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

A simple test can be performed by considering the global exothermic reaction of hydrogen bromide with $n_j$ moles

```{eval-rst}
.. math::
    :nowrap:

    \begin{equation}
        \text{H}_2 + \text{Br}_2 \rightleftharpoons 2\text{HBr}
    \end{equation}
```
which have only three species involve. The system obtained is

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
>> print_stoichiometric_matrix(self, 'transpose')
```

 ```matlab
Transpose stoichiometric matrix:

          H2    Br2    HBr
          __    ___    ___

    BR    0      2      1 
    H     2      0      1 
 ```

1. McBride, Bonnie J. NASA Glenn coefficients for calculating thermodynamic properties of individual species. National Aeronautics and Space Administration, John H. Glenn Research Center at Lewis Field, 2002.