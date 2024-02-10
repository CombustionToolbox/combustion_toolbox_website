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
TThe Combustion Toolbox offers various predefined list of species. To explore the complete list, type <tt>help list_species</tt> at the MATLAB prompt or refer to the [Using predefined chemical systems](https://combustion-toolbox-website.readthedocs.io/en/latest/tutorials/basics/basics_4.html#using-predefined-chemical-systems) tutorial section.
```

Let's start by initializing the Combustion Toolbox and defining the chemical system and the initial state of the mixture (chemical composition, temperature, and pressure):

```matlab
% Initialize CT and define chemical system
self = App('Soot formation');

% Define initial chemical composition
self.PD.S_Fuel     = {'C2H2_acetylene'};
self.PD.S_Oxidizer = {'N2', 'O2'};
self.PD.ratio_oxidizers_O2 = [79, 21]/21;
self = set_prop(self, 'phi', 0.5:0.01:5);

% Define initial thermochemical state
self = set_prop(self, 'TR', 300, 'pR', 1 * 1.01325);
```

To close the problem, we maintain constant enthalpy and pressure. This problem type is denoted as HP in the Combustion Toolbox. By default, the code ensures that the enthalpy of the final state equals that of the initial state; however, we must specify the pressure of the final state using the pP property:

```matlab
% Set chemical transformation
self = set_prop(self, 'pP', self.PD.pR.value);
```

````{note}
All parameters defining the problem are stored within the `PD` property of the `self` structure. While we consistently refer to self for ease of understanding, you may rename it to any other name as needed.
````

Finally, we can solve the problem and visualize the results:

```matlab
% Perform chemical calculations
self = solve_problem(self, 'HP');

% Postprocess results
post_results(self);
```

If everything goes well, the last promt should display the following message:

```matlab
*****************************************************
-----------------------------------------------------
Problem type: HP  | phi = 0.5000
-----------------------------------------------------
               |    REACTANTS    |      PRODUCTS
T [K]          |       300.0000  |      1776.8223
p [bar]        |         1.0132  |         1.0132
r [kg/m3]      |         1.1674  |         0.2011
h [kJ/kg]      |       321.9941  |       321.9941
e [kJ/kg]      |       235.1950  |      -181.7992
g [kJ/kg]      |     -1768.9710  |    -15487.8789
s [kJ/(kg-K)]  |         6.9699  |         8.8978
W [g/mol]      |        28.7369  |        29.3242
(dlV/dlp)T [-] |                 |        -1.0000
(dlV/dlT)p [-] |                 |         1.0017
cp [kJ/(kg-K)] |         1.0364  |         1.3539
gamma [-]      |         1.3873  |         1.2660
gamma_s [-]    |         1.3873  |         1.2660
sound vel [m/s]|       347.0091  |       798.6200
-----------------------------------------------------
REACTANTS               Xi [-]
N2                   7.5816e-01
O2                   2.0154e-01
C2H2_acetylene       4.0307e-02
MINORS[+22]          0.0000e+00

TOTAL                1.0000e+00
-----------------------------------------------------
PRODUCTS                Xi [-]
N2                   7.7233e-01
O2                   1.0142e-01
CO2                  8.2220e-02
H2O                  4.0942e-02
NO                   2.6404e-03
OH                   3.6588e-04
CO                   4.1312e-05
O                    3.0818e-05
H2                   5.5206e-06
H                    6.8730e-07
N                    2.1015e-11
NH                   7.3010e-13
NH3                  3.5644e-13
NH2                  1.4186e-13
HCO                  1.7907e-14
MINORS[+10]          0.0000e+00

TOTAL                1.0000e+00
-----------------------------------------------------
*****************************************************

```

Two plots should also appear, illustrating the equilibrium composition of the system as a function of the equivalence ratio $\phi$, and various properties (temperature, pressure, density, enthalpy, internal energy, Gibbs free energy, entropy, and adiabatic index) of the products as a function of $\phi$.


<p align="center">
    <img src="../../_static/img/chemical_equilibrium_2_fig1.svg" width="1000">
</p>

<p align="center">
    <img src="../../_static/img/chemical_equilibrium_2_fig2.svg" width="1000">
</p>


Combustion Toolbox performs the calculations from the last case to the first one, and the results are stored in the `PS` property of the `self` structure.

````{tip}
The convergence tolerances for various algorithms are stored in the TN (tuning) property within the self structure. Default values are specified in <tt>TuningProperties.m</tt>. For instance, the default tolerance for molar composition is $10^{-14}$, for the multi-dimensional Newton-Raphson solver (where temperature is known) it is $10^{-5}$, and for the Newton-Raphson solver (when temperature is not known) used to satisfy conservation equation for enthalpy, internal energy, or entropy, the tolerance is set to $10^{-4}$.

These parameters ca be easily adjusted by setting the corresponding property in the `TN` structure. For example, to increase the tolerance (increase precision) for molar composition to $10^{-32}$, type
```matlab
self.TN.tolN = 1e-32;
```
prior to solving the problem. To visualize these changes (command window and default plots), execute:
```matlab
self.C.mintol_display = 1e-32;
```
````

## Summary

```matlab
% Initialize CT and define chemical system
self = App('Soot formation');

% Define initial chemical composition
self.PD.S_Fuel     = {'C2H2_acetylene'};
self.PD.S_Oxidizer = {'N2', 'O2'};
self.PD.ratio_oxidizers_O2 = [79, 21]/21;
self = set_prop(self, 'phi', 0.5:0.01:5);

% Define initial thermochemical state
self = set_prop(self, 'TR', 300, 'pR', 1 * 1.01325);

% Set chemical transformation
self = set_prop(self, 'pP', self.PD.pR.value);

% Perform chemical calculations
self = solve_problem(self, 'HP');

% Postprocess results
post_results(self);
```