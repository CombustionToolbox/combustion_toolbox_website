# Validations
 
The Combustion Toolbox {cite:p}`cuadra2024a_preprint,combustiontoolbox` has been validated against established frameworks under a variety of problems. Below is a summary of **some of the validation** cases available, along with the reference codes used for comparison.

| Reference code                                  | Scope of application                                      |
| ----------------------------------------------- | -------------------------------------------------- |
| **[NASA CEA](https://cearun.grc.nasa.gov/)** {cite:p}`gordon1994`                                    | Chemical equilibrium, combustion, propulsion performance                 |
| **[Cantera](https://cantera.org/)** {cite:p}`cantera` | Chemical equilibrium, chemical kinetics, combustion, reactive flow simulations, transport, plasma and electrochemical systems |
| **[Caltech's SD-Toolbox](https://shepherd.caltech.edu/EDL/PublicResources/sdt/)** {cite:p}`Browne2008SDT` | Shock waves, detonations, high-enthalpy reactive flows |
| **[TEA](https://github.com/dzesmin/TEA)** {cite:p}`blecic2016` | Thermochemical equilibrium of exoplanetary atmospheres |

```{note}
Caltech's SD-Toolbox internally uses the [Cantera](https://cantera.org/) {cite:p}`cantera` software packag for thermochemical calculations.
```

```{warning}
For the sake of clarity, we only show a reduced set of species in the validation of the mole fractions.
```

**Contents**

- [Chemical equilibrium calculations](#chemical-equilibrium-calculations)
- [Shock wave calculations](#shock-wave-calculations)
- [Detonation wave calculations](#detonation-wave-calculations)
- [Rocket calculations](#rocket-calculations)
- [Exoplanet / TEA comparisons](#exoplanet-chemical-equilibrium-calculations)

## Chemical equilibrium calculations

Validations of the `EquilibriumSolver` for different problem types with **NASA CEA** as reference. The problem types covered are:
- `TP` (defined temperature and pressure)
- `HP` (defined enthalpy and pressure)
- `TV` (defined temperature and volume)
- `EV` (defined internal energy and volume)
- `SP` (defined entropy and pressure)
- `SV` (defined entropy and volume)


| Case | Mixture definition | Conditions | Equivalence ratio | Reference code | MATLAB script | Data source |
|------|--------------------|------------|-------------------|----------------|--------------|-------------|
| {ref}`TP 1 <sec:TP1>`| $\text{C}_6\text{H}_6 + \dfrac{7.5}{\phi}(\text{O}_2 + 3.76\ \text{N}_2)$ | $T = 2500\,\mathrm{K}$<br>$p = 1\,\mathrm{bar}$ | $0.5 \le \phi \le 4$ | NASA CEA| [run_validation_TP_CEA_1](https://github.com/CombustionToolbox/combustion_toolbox/blob/master/validations/cea/run_validation_TP_CEA_1.m) | [./validations/cea/data/tp](https://github.com/CombustionToolbox/combustion_toolbox/tree/master/validations/cea/data/tp) |
| {ref}`TP 2 <sec:TP2>` | $\text{C}_6\text{H}_6 + \dfrac{7.5}{\phi}\text{O}_2$ | $T = 2500\,\mathrm{K}$<br>$p = 1\,\mathrm{bar}$ | $0.5 \le \phi \le 4$ | NASA CEA| [run_validation_TP_CEA_2](https://github.com/CombustionToolbox/combustion_toolbox/blob/master/validations/cea/run_validation_TP_CEA_2.m) | [./validations/cea/data/tp](https://github.com/CombustionToolbox/combustion_toolbox/tree/master/validations/cea/data/tp) |
| {ref}`TP 3 <sec:TP3>` | $\text{CH}_3\text{OH} + \dfrac{1.5}{\phi}(\text{O}_2 + 3.76\ \text{N}_2)$ | $T = 2500\,\mathrm{K}$<br>$p = 1\,\mathrm{bar}$ | $0.5 \le \phi \le 4$ | NASA CEA| [run_validation_TP_CEA_3](https://github.com/CombustionToolbox/combustion_toolbox/blob/master/validations/cea/run_validation_TP_CEA_3.m) | [./validations/cea/data/tp](https://github.com/CombustionToolbox/combustion_toolbox/tree/master/validations/cea/data/tp) |
| {ref}`TP 4 <sec:TP4>` | $\text{CH}_3\text{OH} + \dfrac{1.5}{\phi}\text{O}_2$ | $T = 2500\,\mathrm{K}$<br>$p = 1\,\mathrm{bar}$ | $0.5 \le \phi \le 4$ | NASA CEA| [run_validation_TP_CEA_4](https://github.com/CombustionToolbox/combustion_toolbox/blob/master/validations/cea/run_validation_TP_CEA_4.m) | [./validations/cea/data/tp](https://github.com/CombustionToolbox/combustion_toolbox/tree/master/validations/cea/data/tp) |
| {ref}`HP 1 <sec:HP1>` | $\text{C}_2\text{H}_2 + \dfrac{2.5}{\phi}(\text{O}_2 + 3.76 \text{N}_2)$ | $T_\text{initial} = 300\,\mathrm{K}$<br>$p = 1\,\mathrm{bar}$ | $0.5 \le \phi \le 4$ | NASA CEA       | [run_validation_HP_CEA_1](https://github.com/CombustionToolbox/combustion_toolbox/blob/master/validations/cea/run_validation_HP_CEA_1.m) | [./validations/cea/data/hp](https://github.com/CombustionToolbox/combustion_toolbox/tree/master/validations/cea/data/hp) |
| {ref}`HP 2 <sec:HP2>` | $\text{C}_2\text{H}_2 + \dfrac{2.5}{\phi}\text{O}_2$                     | $T_\text{initial} = 300\,\mathrm{K}$<br>$p = 1\,\mathrm{bar}$ | $0.5 \le \phi \le 4$ | NASA CEA       | [run_validation_HP_CEA_2](https://github.com/CombustionToolbox/combustion_toolbox/blob/master/validations/cea/run_validation_HP_CEA_2.m) | [./validations/cea/data/hp](https://github.com/CombustionToolbox/combustion_toolbox/tree/master/validations/cea/data/hp) |
| {ref}`HP 3 <sec:HP3>` | $\text{CH}_4 + \dfrac{2}{\phi}(\text{O}_2 + 3.76 \text{N}_2)$            | $T_\text{initial} = 300\,\mathrm{K}$<br>$p = 1\,\mathrm{bar}$ | $0.5 \le \phi \le 4$ | NASA CEA       | [run_validation_HP_CEA_3](https://github.com/CombustionToolbox/combustion_toolbox/blob/master/validations/cea/run_validation_HP_CEA_3.m) | [./validations/cea/data/hp](https://github.com/CombustionToolbox/combustion_toolbox/tree/master/validations/cea/data/hp) |
| {ref}`HP 4 <sec:HP4>` | $\text{CH}_4 + \dfrac{2}{\phi}\text{O}_2$                                | $T_\text{initial} = 300\,\mathrm{K}$<br>$p = 1\,\mathrm{bar}$ | $0.5 \le \phi \le 4$ | NASA CEA       | [run_validation_HP_CEA_4](https://github.com/CombustionToolbox/combustion_toolbox/blob/master/validations/cea/run_validation_HP_CEA_4.m) | [./validations/cea/data/hp](https://github.com/CombustionToolbox/combustion_toolbox/tree/master/validations/cea/data/hp) |
| {ref}`HP 5 <sec:HP5>` | $\text{Natural gas} + \dfrac{2.05}{\phi}\text{Air}$           | $T_\text{initial} = 300\,\mathrm{K}$<br>$p = 1\,\mathrm{bar}$ | $0.5 \le \phi \le 4$ | NASA CEA       | [run_validation_HP_CEA_5](https://github.com/CombustionToolbox/combustion_toolbox/blob/master/validations/cea/run_validation_HP_CEA_5.m) | [./validations/cea/data/hp](https://github.com/CombustionToolbox/combustion_toolbox/tree/master/validations/cea/data/hp) |
| {ref}`TV 1 <sec:TV1>` | $\text{CH}_4 + \dfrac{2}{\phi}\text{Air}$ | $T = 3000\,\mathrm{K}$<br>$p = 1.0132\,\mathrm{bar}$ | $0.5 \le \phi \le 4$ | NASA CEA       | [run_validation_TV_CEA_1](https://github.com/CombustionToolbox/combustion_toolbox/blob/master/validations/cea/run_validation_TV_CEA_1.m) | [./validations/cea/data/tv](https://github.com/CombustionToolbox/combustion_toolbox/tree/master/validations/cea/data/tv) |
| {ref}`EV 1 <sec:EV1>` | $\text{CH}_4 + \dfrac{2}{\phi}\text{Air}$ | $T = 300\,\mathrm{K}$<br>$p = 1.0132\,\mathrm{bar}$ | $0.5 \le \phi \le 4$ | NASA CEA       | [run_validation_EV_CEA_1](https://github.com/CombustionToolbox/combustion_toolbox/blob/master/validations/cea/run_validation_EV_CEA_1.m) | [./validations/cea/data/ev](https://github.com/CombustionToolbox/combustion_toolbox/tree/master/validations/cea/data/ev) |

```{note}
- **Natural gas:** $0.85\text{CH}_4 + 0.1\text{C}_2\text{H}_6 + 0.05\text{CO}_2$
- **Air:** $3.73 \text{N}_2 + \text{O}_2 + 0.0447\text{Ar} + 0.00152 \text{CO}_2$
- **Ideal Air:** $3.76 \text{N}_2 + \text{O}_2$
```


````{hint}
To run all the validations contrasted with CEA at once, write at the prompt:
```matlab
run_validations_CEA
```
````

(sec:TP1)=
### TP 1 - C$_{6}$H$_{6}$ + Air


<p align="center">
    <img src="_static/img/run_validation_TP_CEA_1_molar.svg" width="1000">
    <img src="_static/img/run_validation_TP_CEA_1_properties.svg" width="1000">
</p>

```{eval-rst}
.. only:: latex

    .. image:: _static/img/run_validation_TP_CEA_1_molar.pdf
        :width: 1000px
        :align: center
    .. image:: _static/img/run_validation_TP_CEA_1_properties.pdf
        :width: 1000px
        :align: center
```

(sec:TP2)=
### TP 2 - C$_{6}$H$_{6}$ + O$_{2}$


<p align="center">
    <img src="_static/img/run_validation_TP_CEA_2_molar.svg" width="1000">
    <img src="_static/img/run_validation_TP_CEA_2_properties.svg" width="1000">
</p>

```{eval-rst}
.. only:: latex

    .. image:: _static/img/run_validation_TP_CEA_2_molar.pdf
        :width: 1000px
        :align: center
    .. image:: _static/img/run_validation_TP_CEA_2_properties.pdf
        :width: 1000px
        :align: center
```



(sec:TP3)=
### TP 3 - CH$_{3}$OH + Air


<p align="center">
    <img src="_static/img/run_validation_TP_CEA_3_molar.svg" width="1000">
    <img src="_static/img/run_validation_TP_CEA_3_properties.svg" width="1000">
</p>

```{eval-rst}
.. only:: latex

    .. image:: _static/img/run_validation_TP_CEA_3_molar.pdf
        :width: 1000px
        :align: center
    .. image:: _static/img/run_validation_TP_CEA_3_properties.pdf
        :width: 1000px
        :align: center
```

(sec:TP4)=
### TP 4 - CH$_{3}$OH + O$_{2}$

<p align="center">
    <img src="_static/img/run_validation_TP_CEA_4_molar.svg" width="1000">
    <img src="_static/img/run_validation_TP_CEA_4_properties.svg" width="1000">
</p>

```{eval-rst}
.. only:: latex

    .. image:: _static/img/run_validation_TP_CEA_4_molar.pdf
        :width: 1000px
        :align: center
    .. image:: _static/img/run_validation_TP_CEA_4_properties.pdf
        :width: 1000px
        :align: center
```


(sec:HP1)=
### HP 1 - C$_{2}$H$_{2}$ + Air


<p align="center">
    <img src="_static/img/run_validation_HP_CEA_1_molar.svg" width="1000">
    <img src="_static/img/run_validation_HP_CEA_1_properties.svg" width="1000">
</p>

```{eval-rst}
.. only:: latex

    .. image:: _static/img/run_validation_HP_CEA_1_molar.pdf
        :width: 1000px
        :align: center
    .. image:: _static/img/run_validation_HP_CEA_1_properties.pdf
        :width: 1000px
        :align: center
```

(sec:HP2)=
### HP 2 - C$_{2}$H$_{2}$ + O$_{2}$


<p align="center">
    <img src="_static/img/run_validation_HP_CEA_2_molar.svg" width="1000">
    <img src="_static/img/run_validation_HP_CEA_2_properties.svg" width="1000">
</p>

```{eval-rst}
.. only:: latex

    .. image:: _static/img/run_validation_HP_CEA_2_molar.pdf
        :width: 1000px
        :align: center
    .. image:: _static/img/run_validation_HP_CEA_2_properties.pdf
        :width: 1000px
        :align: center
```

(sec:HP3)=
### HP 3 - CH$_{4}$ + Air

<p align="center">
    <img src="_static/img/run_validation_HP_CEA_3_molar.svg" width="1000">
    <img src="_static/img/run_validation_HP_CEA_3_properties.svg" width="1000">
</p>

```{eval-rst}
.. only:: latex

    .. image:: _static/img/run_validation_HP_CEA_3_molar.pdf
        :width: 1000px
        :align: center
    .. image:: _static/img/run_validation_HP_CEA_3_properties.pdf
        :width: 1000px
        :align: center
```

(sec:HP4)=
### HP 4 - CH$_{4}$ + O$_{2}$


<p align="center">
    <img src="_static/img/run_validation_HP_CEA_4_molar.svg" width="1000">
    <img src="_static/img/run_validation_HP_CEA_4_properties.svg" width="1000">
</p>

```{eval-rst}
.. only:: latex

    .. image:: _static/img/run_validation_HP_CEA_4_molar.pdf
        :width: 1000px
        :align: center
    .. image:: _static/img/run_validation_HP_CEA_4_properties.pdf
        :width: 1000px
        :align: center
```

(sec:HP5)=
### HP 5 - Natural Gas + Air


<p align="center">
    <img src="_static/img/run_validation_HP_CEA_5_molar.svg" width="1000">
    <img src="_static/img/run_validation_HP_CEA_5_properties.svg" width="1000">
</p>

```{eval-rst}
.. only:: latex

    .. image:: _static/img/run_validation_HP_CEA_5_molar.pdf
        :width: 1000px
        :align: center
    .. image:: _static/img/run_validation_HP_CEA_5_properties.pdf
        :width: 1000px
        :align: center
```


(sec:TV1)=
### TV 1 - CH$_{4}$ + Air

<p align="center">
    <img src="_static/img/run_validation_TV_CEA_1_molar.svg" width="1000">
    <img src="_static/img/run_validation_TV_CEA_1_properties.svg" width="1000">
</p>

```{eval-rst}
.. only:: latex

    .. image:: _static/img/run_validation_TV_CEA_1_molar.pdf
        :width: 1000px
        :align: center
    .. image:: _static/img/run_validation_TV_CEA_1_properties.pdf
        :width: 1000px
        :align: center
```


(sec:EV1)=
### EV 1 - CH$_{4}$ + Air

<p align="center">
    <img src="_static/img/run_validation_EV_CEA_1_molar.svg" width="1000">
    <img src="_static/img/run_validation_EV_CEA_1_properties.svg" width="1000">
</p>

```{eval-rst}
.. only:: latex

    .. image:: _static/img/run_validation_EV_CEA_1_molar.pdf
        :width: 1000px
        :align: center
    .. image:: _static/img/run_validation_EV_CEA_1_properties.pdf
        :width: 1000px
        :align: center
```


## Shock wave calculations

Validations of the `ShockSolver` for different problem types with **NASA CEA** and **Caltech's SD-Toolbox** as reference. The problem types covered are:
- `SHOCK I` (planar shock waves)
- `SHOCK R` (reflected shock waves)
- `SHOCK OBLIQUE` (oblique shock waves)
- `SHOCK POLAR` (shock polar diagrams)
- `SHOCK PRANDTL MEYER` (Prandtl-Meyer expansion waves)

| Case                                   | Mixture      | Conditions                   | Reference code       | MATLAB script                             | Data source                     |
|---------------------------------------|-------------|-----------------------------|----------------------|-------------------------------------------|---------------------------------|
| {ref}`SHOCK I 1<sec:SHOCK_I1>`                 | Air + ions  | T = 300 K<br>p = 1 bar      | NASA CEA             | [run_validation_SHOCK_IONIZATION_CEA_1](https://github.com/CombustionToolbox/combustion_toolbox/blob/master/validations/cea/run_validation_SHOCK_IONIZATION_CEA_1.m)   | [./validations/cea/shocks](https://github.com/CombustionToolbox/combustion_toolbox/tree/master/validations/cea/data/shocks) |
| {ref}`SHOCK R 1<sec:SHOCK_R1>`                 | Air + ions  | T = 300 K<br>p = 1 bar      | NASA CEA             | [run_validation_SHOCK_R_IONIZATION_CEA_1](https://github.com/CombustionToolbox/combustion_toolbox/blob/master/validations/cea/run_validation_SHOCK_R_IONIZATION_CEA_1.m) | [./validations/cea/shocks](https://github.com/CombustionToolbox/combustion_toolbox/tree/master/validations/cea/data/shocks) |
| {ref}`SHOCK POLAR 1 <sec:SHOCK_POLAR_SDToolbox1>`   | Air (frozen) | T = 300 K<br>p = 1.01325 bar | SD-Toolbox + Cantera | [run_validation_SHOCK_POLAR_SDToolbox_1](https://github.com/CombustionToolbox/combustion_toolbox/blob/master/validations/sdtoolbox/run_validation_SHOCK_POLAR_SDToolbox_1.m)  | [./validations/sdtoolbox/data](https://github.com/CombustionToolbox/combustion_toolbox/tree/master/validations/sdtoolbox/data)  |
| {ref}`SHOCK PRANDTL MEYER 1 <sec:SHOCK_PRANDTL_MEYER1>` | Air + ions      | T = 3000 K<br>p = 1 bar | SD-Toolbox + Cantera | [run_validation_SHOCK_PRANDTL_MEYER_SDToolbox_1](https://github.com/CombustionToolbox/combustion_toolbox/blob/master/validations/sdtoolbox/run_validation_SHOCK_PRANDTL_MEYER_SDToolbox_1.m) | [./validations/sdtoolbox/data](https://github.com/CombustionToolbox/combustion_toolbox/tree/master/validations/sdtoolbox/data)  |
| {ref}`SHOCK PRANDTL MEYER 2 <sec:SHOCK_PRANDTL_MEYER2>` | Air (frozen)    | T = 3000 K<br>p = 1 bar | SD-Toolbox + Cantera | [run_validation_SHOCK_PRANDTL_MEYER_SDToolbox_2](https://github.com/CombustionToolbox/combustion_toolbox/blob/master/validations/sdtoolbox/run_validation_SHOCK_PRANDTL_MEYER_SDToolbox_2.m) | [./validations/sdtoolbox/data](https://github.com/CombustionToolbox/combustion_toolbox/tree/master/validations/sdtoolbox/data)  |


(sec:SHOCK_I1)=
### SHOCK I - Air with ionization

<p align="center">
    <img src="_static/img/run_validation_SHOCK_IONIZATION_CEA_1_properties_2.svg" width="1000">
    <img src="_static/img/run_validation_SHOCK_IONIZATION_CEA_1_properties_3.svg" width="1000">
</p>

```{eval-rst}
.. only:: latex

    .. image:: _static/img/run_validation_SHOCK_IONIZATION_CEA_1_properties_2.pdf
        :width: 1000px
        :align: center
    .. image:: _static/img/run_validation_SHOCK_IONIZATION_CEA_1_properties_3.pdf
        :width: 1000px
        :align: center
```


(sec:SHOCK_R1)=
### SHOCK R - Air with ionization

<p align="center">
    <img src="_static/img/run_validation_SHOCK_R_IONIZATION_CEA_1_properties_2.svg" width="1000">
    <img src="_static/img/run_validation_SHOCK_R_IONIZATION_CEA_1_properties_3.svg" width="1000">
</p>

```{eval-rst}
.. only:: latex

    .. image:: _static/img/run_validation_SHOCK_R_IONIZATION_CEA_1_properties_2.pdf
        :width: 1000px
        :align: center
    .. image:: _static/img/run_validation_SHOCK_R_IONIZATION_CEA_1_properties_3.pdf
        :width: 1000px
        :align: center
```

(sec:SHOCK_POLAR_SDToolbox1)=
### SHOCK POLAR 1 - Air with ionization

<p align="center">
    <img src="_static/img/run_validation_SHOCK_POLAR_SDToolbox_1_properties_1.svg" width="400">
    <img src="_static/img/run_validation_SHOCK_POLAR_SDToolbox_1_properties_2.svg" width="400">
</p>

```{eval-rst}
.. only:: latex

    .. image:: _static/img/run_validation_SHOCK_POLAR_SDToolbox_1_properties_2.pdf
        :width: 400px
        :align: center
```

(sec:SHOCK_PRANDTL_MEYER1)=
### SHOCK PRANDTL MEYER 1 - Air


<p align="center">
    <img src="_static/img/run_validation_SHOCK_PRANDTL_MEYER_SDToolbox_1_properties_1.svg" width="1000">
</p>


```{eval-rst}
.. only:: latex

    .. image:: _static/img/run_validation_SHOCK_PRANDTL_MEYER_SDToolbox_1_properties_1.pdf
        :width: 1000px
        :align: center
```

(sec:SHOCK_PRANDTL_MEYER2)=
### SHOCK PRANDTL MEYER 2 - Air (frozen)

<p align="center">
    <img src="_static/img/run_validation_SHOCK_PRANDTL_MEYER_SDToolbox_2_properties_1.svg" width="1000">
</p>


```{eval-rst}
.. only:: latex

    .. image:: _static/img/run_validation_SHOCK_PRANDTL_MEYER_SDToolbox_2_properties_1.pdf
        :width: 1000px
        :align: center
```

## Detonation wave calculations

Validations of the `DetonationSolver` for different problem types with **NASA CEA** as reference. The problem type covered is:
- `DET` (Chapman-Jouguet detonations)
<!-- - `DET_OVERDRIVEN` (Overdriven detonations)
- `DET_UNDERDRIVEN` (Underdriven detonations)
- `DET_REFLECTED` (Reflected detonations)
- `DET_OBLIQUE` (Oblique detonations)
- `DET_OVERDRIVEN_OBLIQUE` (Overdriven oblique detonations)
- `DET_UNDERDRIVEN_OBLIQUE` (Underdriven oblique detonations)
- `DET_POLAR` (Detonation shock polars) -->


| Case                    | Mixture definition                                                       | Conditions                                   | Equivalence ratio    | Reference code | MATLAB script                                                                                                                              | Data source                                                                                                                           |
| ----------------------- | ------------------------------------------------------------------------ | -------------------------------------------- | -------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| {ref}`DET 1 <sec:DET1>` | $\text{C}_2\text{H}_2 + \dfrac{2.5}{\phi}(\text{O}_2 + 3.76,\text{N}_2)$ | $T = 300\,\mathrm{K}$<br>$p = 1,\mathrm{bar}$ | $0.5 \le \phi \le 4$ | NASA CEA       | [run_validation_DET_CEA_1](https://github.com/CombustionToolbox/combustion_toolbox/blob/master/validations/cea/run_validation_DET_CEA_1.m) | [./validations/cea/detonations](https://github.com/CombustionToolbox/combustion_toolbox/tree/master/validations/cea/data/detonations) |
| {ref}`DET 2 <sec:DET2>` | $\text{C}_2\text{H}_2 + \dfrac{2.5}{\phi}\text{O}_2$                     | $T = 300\,\mathrm{K}$<br>$p = 1,\mathrm{bar}$ | $0.5 \le \phi \le 4$ | NASA CEA       | [run_validation_DET_CEA_2](https://github.com/CombustionToolbox/combustion_toolbox/blob/master/validations/cea/run_validation_DET_CEA_2.m) | [./validations/cea/detonations](https://github.com/CombustionToolbox/combustion_toolbox/tree/master/validations/cea/data/detonations) |
| {ref}`DET 3 <sec:DET3>` | $\text{CH}_4 + \dfrac{2}{\phi}(\text{O}_2 + 3.76,\text{N}_2)$            | $T = 300\,\mathrm{K}$<br>$p = 1,\mathrm{bar}$ | $0.5 \le \phi \le 4$ | NASA CEA       | [run_validation_DET_CEA_3](https://github.com/CombustionToolbox/combustion_toolbox/blob/master/validations/cea/run_validation_DET_CEA_3.m) | [./validations/cea/detonations](https://github.com/CombustionToolbox/combustion_toolbox/tree/master/validations/cea/data/detonations) |
| {ref}`DET 4 <sec:DET4>` | $\text{CH}_4 + \dfrac{2}{\phi}\text{O}_2$                                | $T = 300\,\mathrm{K}$<br>$p = 1,\mathrm{bar}$ | $0.5 \le \phi \le 4$ | NASA CEA       | [run_validation_DET_CEA_4](https://github.com/CombustionToolbox/combustion_toolbox/blob/master/validations/cea/run_validation_DET_CEA_4.m) | [./validations/cea/detonations](https://github.com/CombustionToolbox/combustion_toolbox/tree/master/validations/cea/data/detonations) |



(sec:DET1)=
### DET 1 - C$_{2}$H$_{2}$ + Air

<p align="center">
    <img src="_static/img/run_validation_DET_CEA_1_molar.svg" width="1000">
    <img src="_static/img/run_validation_DET_CEA_1_properties_1.svg" width="1000">
    <img src="_static/img/run_validation_DET_CEA_1_properties_2.svg" width="1000">
</p>

```{eval-rst}
.. only:: latex

    .. image:: _static/img/run_validation_DET_CEA_1_molar.pdf
        :width: 1000px
        :align: center
    .. image:: _static/img/run_validation_DET_CEA_1_properties_1.pdf
        :width: 1000px
        :align: center
    .. image:: _static/img/run_validation_DET_CEA_1_properties_2.pdf
        :width: 1000px
        :align: center
```

(sec:DET2)=
### DET 2 - C$_{2}$H$_{2}$ + O$_{2}$

<p align="center">
    <img src="_static/img/run_validation_DET_CEA_2_molar.svg" width="1000">
    <img src="_static/img/run_validation_DET_CEA_2_properties_1.svg" width="1000">
    <img src="_static/img/run_validation_DET_CEA_2_properties_2.svg" width="1000">
</p>

```{eval-rst}
.. only:: latex

    .. image:: _static/img/run_validation_DET_CEA_2_molar.pdf
        :width: 1000px
        :align: center
    .. image:: _static/img/run_validation_DET_CEA_2_properties_1.pdf
        :width: 1000px
        :align: center
    .. image:: _static/img/run_validation_DET_CEA_2_properties_2.pdf
        :width: 1000px
        :align: center
```

(sec:DET3)=
### DET 3 - CH$_{4}$ + Air

<p align="center">
    <img src="_static/img/run_validation_DET_CEA_3_molar.svg" width="1000">
    <img src="_static/img/run_validation_DET_CEA_3_properties_1.svg" width="1000">
    <img src="_static/img/run_validation_DET_CEA_3_properties_2.svg" width="1000">
</p>

```{eval-rst}
.. only:: latex

    .. image:: _static/img/run_validation_DET_CEA_3_molar.pdf
        :width: 1000px
        :align: center
    .. image:: _static/img/run_validation_DET_CEA_3_properties_1.pdf
        :width: 1000px
        :align: center
    .. image:: _static/img/run_validation_DET_CEA_3_properties_2.pdf
        :width: 1000px
        :align: center
```

(sec:DET4)=
### DET 4 - CH$_{4}$ + O$_{2}$

<p align="center">
    <img src="_static/img/run_validation_DET_CEA_4_molar.svg" width="1000">
    <img src="_static/img/run_validation_DET_CEA_4_properties_1.svg" width="1000">
    <img src="_static/img/run_validation_DET_CEA_4_properties_2.svg" width="1000">
</p>

```{eval-rst}
.. only:: latex

    .. image:: _static/img/run_validation_DET_CEA_4_molar.pdf
        :width: 1000px
        :align: center
    .. image:: _static/img/run_validation_DET_CEA_4_properties_1.pdf
        :width: 1000px
        :align: center
    .. image:: _static/img/run_validation_DET_CEA_4_properties_2.pdf
        :width: 1000px
        :align: center
```



## Rocket calculations

Validations of the `RocketSolver` for different problem types with **NASA CEA** as reference. The problem type covered is:
- `ROCKET IAC` (Infinite area chamber model)
- `ROCKET FAC` (Finite area chamber model)

| Case                                  | Propellants      | Conditions                                                                                                                                                                                               | Equivalence ratio    | Reference code | MATLAB script                                                                                                                                                                                                                                                                                          | Data source                                                                                                                 |
| ------------------------------------- | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------- |
| {ref}`ROCKET IAC 1 <sec:ROCKET_IAC1>` | LH$_2$ + LOX     | $T_\text{fuel} = 20.27\,\mathrm{K}$<br>$T_\text{oxid} = 90.17\,\mathrm{K}$<br>$p_\text{chamber} = 22,\mathrm{bar}$<br>$A_\text{exit}/A_\text{throat} = 3$                                                  | $0.5 \le \phi \le 4$ | NASA CEA       | [run_validation_ROCKET_CEA_17](https://github.com/CombustionToolbox/combustion_toolbox/blob/master/validations/cea/run_validation_ROCKET_CEA_17.m)                                                                                                                                                     | [./validations/cea/rocket](https://github.com/CombustionToolbox/combustion_toolbox/tree/master/validations/cea/data/rocket) |
| {ref}`ROCKET IAC 2 <sec:ROCKET_IAC2>` | LH$_2$ + LOX     | $T_\text{fuel} = 298.15\,\mathrm{K}$<br>$T_\text{oxid} = 90.17\,\mathrm{K}$<br>$p_\text{chamber} = 101.325,\mathrm{bar}$<br>$A_\text{exit}/A_\text{throat} = 8$                                            | $0.5 \le \phi \le 4$ | NASA CEA       | [run_validation_ROCKET_CEA_24](https://github.com/CombustionToolbox/combustion_toolbox/blob/master/validations/cea/run_validation_ROCKET_CEA_24.m)                                                                                                                                                     | [./validations/cea/rocket](https://github.com/CombustionToolbox/combustion_toolbox/tree/master/validations/cea/data/rocket) |
| {ref}`ROCKET FAC 1 <sec:ROCKET_FAC1>` | RP-1 + LOX       | $T_\text{fuel} = 298.15\,\mathrm{K}$<br>$T_\text{oxid} = 90.17\,\mathrm{K}$<br>$p_\text{chamber} = 22,\mathrm{bar}$<br>$A_\text{chamber}/A_\text{throat} = 2$<br>$A_\text{exit}/A_\text{throat} = [1:2.6]$ | $0.5 \le \phi \le 4$ | NASA CEA       | [run_validation_ROCKET_CEA_1](https://github.com/CombustionToolbox/combustion_toolbox/blob/master/validations/cea/run_validation_ROCKET_CEA_1.m)<br>[run_validation_ROCKET_CEA_16](https://github.com/CombustionToolbox/combustion_toolbox/blob/master/validations/cea/run_validation_ROCKET_CEA_16.m) | [./validations/cea/rocket](https://github.com/CombustionToolbox/combustion_toolbox/tree/master/validations/cea/data/rocket) |
| {ref}`ROCKET FAC 2 <sec:ROCKET_FAC2>` | LH$_2$ + LOX     | $T_\text{fuel} = 20.27\,\mathrm{K}$<br>$T_\text{oxid} = 90.17\,\mathrm{K}$<br>$p_\text{chamber} = 101.325,\mathrm{bar}$<br>$A_\text{chamber}/A_\text{throat} = 2$<br>$A_\text{exit}/A_\text{throat} = 8$   | $0.5 \le \phi \le 4$ | NASA CEA       | [run_validation_ROCKET_CEA_18](https://github.com/CombustionToolbox/combustion_toolbox/blob/master/validations/cea/run_validation_ROCKET_CEA_18.m)                                                                                                                                                     | [./validations/cea/rocket](https://github.com/CombustionToolbox/combustion_toolbox/tree/master/validations/cea/data/rocket) |
| {ref}`ROCKET FAC 3 <sec:ROCKET_FAC3>` | RP-1 + LOX       | $T_\text{fuel} = 298.15\,\mathrm{K}$<br>$T_\text{oxid} = 90.17\,\mathrm{K}$<br>$p_\text{chamber} = 101.325,\mathrm{bar}$<br>$A_\text{chamber}/A_\text{throat} = 2$<br>$A_\text{exit}/A_\text{throat} = 8$  | $0.5 \le \phi \le 4$ | NASA CEA       | [run_validation_ROCKET_CEA_20](https://github.com/CombustionToolbox/combustion_toolbox/blob/master/validations/cea/run_validation_ROCKET_CEA_20.m)                                                                                                                                                     | [./validations/cea/rocket](https://github.com/CombustionToolbox/combustion_toolbox/tree/master/validations/cea/data/rocket) |
| {ref}`ROCKET FAC 4 <sec:ROCKET_FAC4>` | LCH$_4$ + LOX    | $T_\text{fuel} = 111.66\,\mathrm{K}$<br>$T_\text{oxid} = 90.17\,\mathrm{K}$<br>$p_\text{chamber} = 101.325,\mathrm{bar}$<br>$A_\text{chamber}/A_\text{throat} = 2$<br>$A_\text{exit}/A_\text{throat} = 8$  | $0.5 \le \phi \le 4$ | NASA CEA       | [run_validation_ROCKET_CEA_21](https://github.com/CombustionToolbox/combustion_toolbox/blob/master/validations/cea/run_validation_ROCKET_CEA_21.m)                                                                                                                                                     | [./validations/cea/rocket](https://github.com/CombustionToolbox/combustion_toolbox/tree/master/validations/cea/data/rocket) |
| {ref}`ROCKET FAC 5 <sec:ROCKET_FAC5>` | LH$_2$ + LOX     | $T_\text{fuel} = 20.27\,\mathrm{K}$<br>$T_\text{oxid} = 90.17\,\mathrm{K}$<br>$p_\text{chamber} = 101.325,\mathrm{bar}$<br>$A_\text{chamber}/A_\text{throat} = 2$<br>$A_\text{exit}/A_\text{throat} = 8$   | $0.5 \le \phi \le 4$ | NASA CEA       | [run_validation_ROCKET_CEA_22](https://github.com/CombustionToolbox/combustion_toolbox/blob/master/validations/cea/run_validation_ROCKET_CEA_22.m)                                                                                                                                                     | [./validations/cea/rocket](https://github.com/CombustionToolbox/combustion_toolbox/tree/master/validations/cea/data/rocket) |
| {ref}`ROCKET FAC 6 <sec:ROCKET_FAC6>` | MMH + N$_2$O$_4$ | $T_\text{fuel} = 298.15\,\mathrm{K}$<br>$T_\text{oxid} = 300\,\mathrm{K}$<br>$p_\text{chamber} = 101.325,\mathrm{bar}$<br>$A_\text{chamber}/A_\text{throat} = 2$<br>$A_\text{exit}/A_\text{throat} = 8$ | $0.5 \le \phi \le 4$ | NASA CEA       | [run_validation_ROCKET_CEA_23](https://github.com/CombustionToolbox/combustion_toolbox/blob/master/validations/cea/run_validation_ROCKET_CEA_23.m)                                                                                                                                                     | [./validations/cea/rocket](https://github.com/CombustionToolbox/combustion_toolbox/tree/master/validations/cea/data/rocket) |



(sec:ROCKET_IAC1)=
### ROCKET IAC 1 - LH2 + LOX


<p align="center">
    <img src="_static/img/run_validation_ROCKET_CEA_17_molar.svg" width="1000">
    <img src="_static/img/run_validation_ROCKET_CEA_17_properties.svg" width="1000">
</p>

```{eval-rst}
.. only:: latex

    .. image:: _static/img/run_validation_ROCKET_CEA_17_molar.pdf
        :width: 1000px
        :align: center
    .. image:: _static/img/run_validation_ROCKET_CEA_17_properties.pdf
        :width: 1000px
        :align: center
```


(sec:rocket_iac2)=
### ROCKET IAC 2 - LH2 + LOX

<p align="center">
    <img src="_static/img/run_validation_ROCKET_CEA_24_molar.svg" width="1000">
    <img src="_static/img/run_validation_ROCKET_CEA_24_properties.svg" width="1000">
</p>

```{eval-rst}
.. only:: latex

    .. image:: _static/img/run_validation_ROCKET_CEA_24_molar.pdf
        :width: 1000px
        :align: center
    .. image:: _static/img/run_validation_ROCKET_CEA_24_properties.pdf
        :width: 1000px
        :align: center
```

(sec:ROCKET_FAC1)=
### ROCKET FAC 1 - RP1 + LOX

<p align="center">
    <img src="_static/gif/validation_rocket.gif" width="720">
</p>


(sec:ROCKET_FAC2)=
### ROCKET FAC 2 - LH2 + LOX

<p align="center">
    <img src="_static/img/run_validation_ROCKET_CEA_18_molar.svg" width="1000">
    <img src="_static/img/run_validation_ROCKET_CEA_18_properties.svg" width="1000">
</p>

```{eval-rst}
.. only:: latex

    .. image:: _static/img/run_validation_ROCKET_CEA_18_molar.pdf
        :width: 1000px
        :align: center
    .. image:: _static/img/run_validation_ROCKET_CEA_18_properties.pdf
        :width: 1000px
        :align: center
```

(sec:ROCKET_FAC3)=
### ROCKET FAC 3 - RP1 + LOX

<p align="center">
    <img src="_static/img/run_validation_ROCKET_CEA_20_molar.svg" width="1000">
    <img src="_static/img/run_validation_ROCKET_CEA_20_properties.svg" width="1000">
</p>

```{eval-rst}
.. only:: latex

    .. image:: _static/img/run_validation_ROCKET_CEA_20_molar.pdf
        :width: 1000px
        :align: center
    .. image:: _static/img/run_validation_ROCKET_CEA_20_properties.pdf
        :width: 1000px
        :align: center
```

(sec:ROCKET_FAC4)=
### ROCKET FAC 4 - LCH4 + LOX

<p align="center">
    <img src="_static/img/run_validation_ROCKET_CEA_21_molar.svg" width="1000">
    <img src="_static/img/run_validation_ROCKET_CEA_21_properties.svg" width="1000">
</p>

```{eval-rst}
.. only:: latex

    .. image:: _static/img/run_validation_ROCKET_CEA_21_molar.pdf
        :width: 1000px
        :align: center
    .. image:: _static/img/run_validation_ROCKET_CEA_21_properties.pdf
        :width: 1000px
        :align: center
```

(sec:ROCKET_FAC5)=
### ROCKET FAC 5 - LH2 + LOX

<p align="center">
    <img src="_static/img/run_validation_ROCKET_CEA_22_molar.svg" width="1000">
    <img src="_static/img/run_validation_ROCKET_CEA_22_properties.svg" width="1000">
</p>

```{eval-rst}
.. only:: latex

    .. image:: _static/img/run_validation_ROCKET_CEA_22_molar.pdf
        :width: 1000px
        :align: center
    .. image:: _static/img/run_validation_ROCKET_CEA_22_properties.pdf
        :width: 1000px
        :align: center
```

(sec:ROCKET_FAC6)=
### ROCKET FAC 6 - MMH + N2O4

<p align="center">
    <img src="_static/img/run_validation_ROCKET_CEA_23_molar.svg" width="1000">
    <img src="_static/img/run_validation_ROCKET_CEA_23_properties.svg" width="1000">
</p>

```{eval-rst}
.. only:: latex

    .. image:: _static/img/run_validation_ROCKET_CEA_23_molar.pdf
        :width: 1000px
        :align: center
    .. image:: _static/img/run_validation_ROCKET_CEA_23_properties.pdf
        :width: 1000px
        :align: center
```

## Exoplanet chemical equilibrium calculations

Validations of the `EquilibriumSolver` and `SolarAbundances` classes for different temperature and pressure profiles with **Thermochemical Equilibrium Abundances of chemical species (TEA)** software as reference. The problem type covered is:
- `TP` (defined temperature and pressure profiles)



| Case                             | Mixture / Scenario      | Temperature range                          | Pressure range                             | Reference code | MATLAB script              | Data source / URL |
|---------------------------------|------------------------|-------------------------------------------|-------------------------------------------|----------------|----------------------------|------------------|
| {ref}`TEA 1 <sec:TEA1>`         | See note$^1$   | $T \in [500, 5000]$ K                      | $p \in [10^{-5}, 10^{2}]$ bar              | TEA            | [run_validation_TP_TEA_1](https://github.com/CombustionToolbox/combustion_toolbox/blob/master/validations/tea/run_validation_TP_TEA_1.m) | [https://github.com/dzesmin/TEA/blob/master/doc/examples/quick_example/results/quick_example.tea](https://github.com/dzesmin/TEA/blob/master/doc/examples/quick_example/results/quick_example.tea) |
| {ref}`TEA 2 <sec:TEA2>`         | WASP-43b, $\text{metallicity} = 1$  | $T \in [958.36, 1811.89]$ K                | $p \in [2.4\!\times\!10^{-6}, 31.62]$ bar  | TEA            | [run_validation_TP_TEA_2](https://github.com/CombustionToolbox/combustion_toolbox/blob/master/validations/tea/run_validation_TP_TEA_2.m) | [https://github.com/dzesmin/RRC-BlecicEtal-2015a-ApJS-TEA/tree/master/Fig6/WASP43b-solar](https://github.com/dzesmin/RRC-BlecicEtal-2015a-ApJS-TEA/tree/master/Fig6/WASP43b-solar) |
| {ref}`TEA 3 <sec:TEA3>`         | WASP-43b, $\text{metallicity} = 10$ | $T \in [958.36, 1811.89]$ K                | $p \in [2.4\!\times\!10^{-6}, 31.62]$ bar  | TEA            | [run_validation_TP_TEA_3](https://github.com/CombustionToolbox/combustion_toolbox/blob/master/validations/tea/run_validation_TP_TEA_3.m) | [https://github.com/dzesmin/RRC-BlecicEtal-2015a-ApJS-TEA/tree/master/Fig6/WASP43b-10xsolar](https://github.com/dzesmin/RRC-BlecicEtal-2015a-ApJS-TEA/tree/master/Fig6/WASP43b-10xsolar) |
| {ref}`TEA 4 <sec:TEA4>`         | WASP-43b, $\text{metallicity} = 50$ | $T \in [958.36, 1811.89]$ K                | $p \in [2.4\!\times\!10^{-6}, 31.62]$ bar  | TEA            | [run_validation_TP_TEA_4](https://github.com/CombustionToolbox/combustion_toolbox/blob/master/validations/tea/run_validation_TP_TEA_4.m) | [https://github.com/dzesmin/RRC-BlecicEtal-2015a-ApJS-TEA/tree/master/Fig6/WASP43b-50xsolar](https://github.com/dzesmin/RRC-BlecicEtal-2015a-ApJS-TEA/tree/master/Fig6/WASP43b-50xsolar) |

> $^1$ Initial mixture: H  = 1.0000000000e+00, He = 8.5113803820e-02, C  = 2.6915348039e-04, N  = 6.7608297539e-05, O  = 4.8977881937e-04

(sec:TEA1)=
### TEA 1

<p align="left">
    <img src="_static/img/run_validation_TP_TEA_1_molar.svg" width="1000">
</p> 

```{eval-rst}
.. only:: latex

    .. image:: _static/img/run_validation_TP_TEA_1_molar.pdf
        :width: 1000px
        :align: center
```

(sec:TEA2)=
### WASP-43b metallicity 1

<p align="left">
    <img src="_static/img/run_validation_TP_TEA_2_molar.svg" width="1000">
</p> 

```{eval-rst}
.. only:: latex

    .. image:: _static/img/run_validation_TP_TEA_2_molar.pdf
        :width: 1000px
        :align: center
```

(sec:TEA3)=
### WASP-43b metallicity 10


<p align="left">
    <img src="_static/img/run_validation_TP_TEA_3_molar.svg" width="1000">
</p> 

```{eval-rst}
.. only:: latex

    .. image:: _static/img/run_validation_TP_TEA_3_molar.pdf
        :width: 1000px
        :align: center
```

(sec:TEA4)=
### WASP-43b metallicity 50


<p align="left">
    <img src="_static/img/run_validation_TP_TEA_4_molar.svg" width="1000">
</p>

```{eval-rst}
.. only:: latex

    .. image:: _static/img/run_validation_TP_TEA_4_molar.pdf
        :width: 1000px
        :align: center
```