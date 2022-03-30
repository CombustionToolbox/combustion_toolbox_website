<p align="center">
    <img alt="UC3M" style="border-width:0" src="_static/img/logo.svg" width="1500"/></a>
</p>

<br> <center> <b> A MATLAB-GUI based open-source tool for solving gaseous combustion problems. </b> </center> <br>

<!-- There is also a (less complete) [Python version](https://github.com/AlbertoCuadra/Combustion-PyToolbox) -->

::::{grid} 1 2 2 3
:margin: 4 4 0 0
:gutter: 1

:::{grid-item-card} {octicon}`package` Robust modular kernel
:link: https://combustion-toolbox-website.readthedocs.io/en/latest/documentation/solver_chemical_equilibrium.html
`Robust`, `modular`, and `Fast` chemical equilibrium computations.
:::

:::{grid-item-card} {octicon}`device-desktop` Graphic User Interface
:link: https://github.com/AlbertoCuadra/combustion_toolbox/blob/master/Installer/Combustion%20Toolbox.mlappinstall
The code is also encapsulated in an `user-friendly` GUI with tons of capabilities.
:::

:::{grid-item-card} {octicon}`globe` Open source
:link: https://github.com/AlbertoCuadra/combustion_toolbox
The code/GUI is fully open source, GUI included!
:::

::::

<p align="center">
    <img src="_static/gif/example_HP.gif" width="383">
    <img src="_static/gif/example_HP_plain.gif" width="417">
</p>


# Start here!


::::{grid} 1 2 2 3
:margin: 4 4 0 0
:gutter: 1

:::{grid-item-card} {octicon}`tasklist` Tutorial
:link: https://combustion-toolbox-website.readthedocs.io/en/latest/tutorial.html

New to Combustion Toolbox?
:::

:::{grid-item-card} {octicon}`note` Examples
:link: https://combustion-toolbox-website.readthedocs.io/en/latest/examples.html

See examples of Combustion-Toolbox applications.
:::

:::{grid-item-card} {octicon}`repo` Documentation
:link: https://combustion-toolbox-website.readthedocs.io/en/latest/documentation/index.html

Let's check the documentation of almost (every) functions.
:::

::::


<!-- | Fast Chemical equilibrium computations 	| Modular construction 	| Open source 	|
| ----------- | ----------- | ----------- |
|  The kernel has been optimized ...	| All changes made to the kernel will be applied directly in the GUI	| The code/GUI is fully open source - compatible with MATLAB | -->

# Gallery

We have several examples of what Combustion Toolbox can do. Here we show a preview of the GUI and some results obtained from Combustion Toolbox.

<p align="center">
    <img src="_static/img/snapshot_1.svg" width="500">
</p>

**Figure 1:** *Snapshot of the GUI*.

<p align="center">
    <img src="_static/img/Hugoniot_benchmarking.svg" width="400">
</p>
    
**Figure 2:** *Hugoniot curves for different molecular gases at pre-shock temperature T1 = 300 K and pressure p1 = 1 atm \[numerical results obtained with Combustion Toolbox (lines) and contrasted with NASA’s Chemical Equilibrium with Applications (CEA) code excluding ionization (symbols)\]*.
    
<p align="center">
    <img src="_static/img/run_validation_DET_CEA_3_molar.svg" width="1200">
</p>

**Figure 3:** *Variation of molar fraction for a CJ detonation for lean to rich CH4-air mixtures at standard conditions (T1 = 300 K and pressure p1 = 1 atm); line: numerical results obtained with Combustion Toolbox; circles: NASA's Chemical Equilibrium with Applications code. The computational time was of 9.25 seconds using a Intel(R) Core(TM) i7-8700 CPU @ 3.20GHz for a set of 24 species considered and a total of 351 case studies.*

<p align="center">
    <img src="_static/img/polar_shock_full_and_frozen_both_air_complete.svg" width="1000">
</p>

**Figure 4:** *Pressure-deflection shock polar (left) and wave angle-deflection shock polar (right) for an air mixture (78.084% N2, 20.9476% O2, 0.9365% Ar, 0.0319% CO2) at pre-shock temperature T1 = 300 K and pressure p1 = 1 atm, and a range of preshock Mach numbers M1 = [2, 14]; line: considering dissociation, ionization, and recombination in multi-species mixtures; dashed: considering a thermochemically frozen air mixture.*

# Contributing

Please send feedback or inquiries to [acuadra@ing.uc3m.es](mailto:acuadra@ing.uc3m.es)

Thank you for testing Combustion Toolbox!

# Acknowledgements
* Combustion Toolbox's color palette is obtained from the following repository: Stephen (2021). ColorBrewer: Attractive and Distinctive Colormaps (https://github.com/DrosteEffect/BrewerMap), GitHub. Retrieved December 3, 2021.
* For validations, Combustion Toolbox uses CPU Info from the following repository: Ben Tordoff (2022). CPU Info (https://github.com/BJTor/CPUInfo/releases/tag/v1.3), GitHub. Retrieved March 22, 2022.

# Developers

* **[Alberto Cuadra-Lara](https://acuadralara.com/)** - *Core Developer and App designer*
* **César Huete** - *Developer*
* **Marcos Vera** - *Developer*

Grupo de Mecánica de Fluidos, Universidad Carlos III, Av. Universidad 30, 28911, Leganés, Spain

See also the list of [contributors](https://github.com/AlbertoCuadra/combustion_toolbox/blob/master/CONTRIBUTORS.md) who participated in this project.

# Citing Combustion Toolbox

```bibtex
@misc{combustiontoolbox,
    author = "Cuadra, A and Huete, C and Vera, M",
    title = "Combustion Toolbox: A MATLAB-GUI based open-source tool for solving combustion problems",
    year = 2022,
    note = "Version 0.9.1",
    doi = {https://doi.org/10.5281/zenodo.6396748}
}
```