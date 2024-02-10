# Chemical equilibrium

In this section, we will cover how to perform chemical equilibrium calculations with the Combustion Toolbox. Chemical equilibrium is solved via minimization of the Gibbs/Helmholtz free energy combining the method of Lagrange multipliers with a multidimensional Newton-Raphson (NR) method, based on the mathematical formulation set forth by NASA in its CEA code {cite:p}`gordon1994`. Our dedicated CT-EQUIL module has been developed to precisely determine the equilibrium composition of multi-component gas mixtures undergoing essential thermochemical transformations. These transformations occur from an initial state (reactants), defined by its composition, temperature, and pressure, to a final state (products), characterized by a set of chemical species (in gaseous--- including ions---or pure condensed phase) along with two thermodynamic state functions, such as enthalpy and pressure, e.g., for isobaric combustion processes.

The CT-EQUIL module facilitates the computation of chemical equilibrium composition and thermodynamic properties for a range of specified state function pairs:
* `TP` (temperature and pressure),
* `HP` (enthalpy and pressure),
* `SP` (entropy and pressure),
* `TV` (temperature and volume),
* `EV` (internal energy and volume),
* `SV` (entropy and volume).

Additionally, Combustion Toolbox enables the computation of chemical equilibrium under various assumptions regarding the final gas mixture, including calorically perfect gas, calorically imperfect gas with frozen chemistry, or calorically imperfect gas with equilibrium chemistry, including dissociation and ionization.

In many practical applications, the equilibrium temperature of a system is not initially determined, thereby necessitating the provision of supplementary information to close the problem. This additional information may be obtained from an enthalpy, internal energy, or entropy conservation equation, subject to the requirement that the corresponding state function $f$ remains unchanged, namely
```{eval-rst}
.. math::
    :nowrap:

    \begin{equation}
      \Delta f\left(T\right) \equiv f_{\rm F}\left(T\right) - f_{\rm I}\left(T_{\rm I}\right) = 0,
    \end{equation}
```
where the subscripts F and I refer here to the final and initial states of the mixture, respectively. Unlike in NASA's CEA code, we have increased the flexibility of the CT-EQUIL module by decoupling this additional equation and retrieved the new condition by using a second-order NR method
```{eval-rst}
.. math::
    :nowrap:

    \begin{equation}
      T_{k+1} = T_k-\frac{f\left(T_k\right)}{f^\prime\left(T_k\right)}.
    \end{equation}
```

```{toctree}
    :caption: Contents
    :maxdepth: 2
    :titlesonly:
    
chemical_equilibrium/chemical_equilibrium_1
chemical_equilibrium/chemical_equilibrium_2
```