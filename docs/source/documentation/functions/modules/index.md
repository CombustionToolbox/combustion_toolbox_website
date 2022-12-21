# Modules

Combustion Toolbox has implemented three different modules: `CT-EQUIL`, `CT-SD`, and `CT-ROCKET`. The core module, CT-EQUIL, minimizes the Gibbs/Helmholtz free energy of the system using Lagrange multipliers combined with a multidimensional Newton-Raphson method, upon the condition that the mixture properties are defined by two functions of state (e.g., enthalpy and pressure). CT-SD solves processes that involve strong changes in dynamic pressure, such as steady state shock and detonation waves in either normal or oblique stream configurations within the limits of regular shock reflections. Finally, CT-ROCKET estimates rocket propellant performance under ideal conditions. Additionally, this folder includes the initialization routines for the main variable `self`. 


```{toctree}
    :caption: 'Contents:'
    :maxdepth: 2
    :titlesonly:

modules_self
ct_equil/index
ct_sd/index
ct_rocket/index
```