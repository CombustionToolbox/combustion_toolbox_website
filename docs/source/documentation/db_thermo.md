# Thermodynamic functions

Combustion Toolbox takes into account the NASA-9 polynomials fitting to evaluate the thermodynamic data of the species for the specific heat, enthalpy, and entropy as function of temperature, namely

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

where $a_i$ and $b_i$ are the temperature coefficients and the integration constants, respectively. Depending of the species the polynomials fit up to 20000 K [1]. This values are available in the [source code](https://github.com/AlbertoCuadra/combustion_toolbox/blob/master/Databases/thermo.inp) and can be also obtained from [NASA's thermo build website](https://cearun.grc.nasa.gov/ThermoBuild/).

&nbsp;

1. B. J. McBride, NASA Glenn coefficients for calculating thermodynamic
properties of individual species, National Aeronautics and Space Ad-
ministration, John H. Glenn Research Center, 2002.

