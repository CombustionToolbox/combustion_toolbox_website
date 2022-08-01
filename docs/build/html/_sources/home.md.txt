<p align="center">
    <img alt="UC3M" style="border-width:0" src="_static/img/logo.svg" width="1500"/></a>
</p>

<br> <center> <b> A MATLAB-GUI based open-source tool for solving gaseous combustion problems. </b> </center> <br>

::::{grid} 1 2 2 3
:margin: 4 4 0 0
:gutter: 1

:::{grid-item-card} {octicon}`package` Robust modular kernel
:link: https://combustion-toolbox-website.readthedocs.io/en/latest/documentation/solver_chemical_equilibrium.html
`Robust`, `modular`, and `fast` chemical equilibrium computations.
:::

:::{grid-item-card} {octicon}`device-desktop` Interactive App
:link: https://github.com/AlbertoCuadra/combustion_toolbox/archive/refs/heads/master.zip
The code is encapsulated in an `user-friendly` GUI with tons of capabilities.
:::

:::{grid-item-card} {octicon}`globe` Open source
:link: https://github.com/AlbertoCuadra/combustion_toolbox
Completely open source, GUI included!<br>
{bdg-light}`Github` {bdg-info}`GPLv3`
:::

::::

# Combustion Toolbox in action

<p align="center">
    <img src="_static/gif/example_HP_GUI.gif" width="352">&nbsp;&nbsp;&nbsp;
    <img src="_static/gif/example_HP.gif" width="381">
</p>

# Combustion Toolbox capabilities

::::{grid} 1 2 2 2
:margin: 4 4 0 0
:gutter: 1

:::{grid-item-card} {octicon}`cpu` Robust chemical equilibrium computations
:link: https://combustion-toolbox-website.readthedocs.io/en/latest/documentation/solver_chemical_equilibrium.html
{bdg-light}`TP` {bdg-light}`HP` {bdg-light}`SP` {bdg-light}`TV` {bdg-light}`EV` {bdg-light}`SV` {bdg-light}`frozen` {bdg-light}`plasma state`

:::

:::{grid-item-card} {octicon}`device-desktop` Interactive App
:link: https://github.com/AlbertoCuadra/combustion_toolbox/archive/refs/heads/master.zip
Over 10K lines of code encapsulated in an `user-friendly` GUI with tons of capabilities.
{bdg-light}`Toolbox` {bdg-light}`Standalone`
:::

:::{grid-item-card} {octicon}`tab` Shocks and detonations pre- and post-shock states 
:link: https://combustion-toolbox-website.readthedocs.io/en/latest/documentation/solver_shocks_detonations.html
{bdg-light}`Incident` {bdg-light}`Reflected` {bdg-light}`Oblique` {bdg-light}`Shock polars` {bdg-light}`Regular Reflections` 
:::

:::{grid-item-card} {octicon}`globe` Open source
:link: https://github.com/AlbertoCuadra/combustion_toolbox
Completely open source, GUI included!
{bdg-light}`Github` {bdg-light}`FileExchange` {bdg-light}`Zenodo` {bdg-info}`GPLv3`
:::

::::

::::{grid} 1 2 2 3
:margin: 4 4 0 0
:gutter: 1

:::{grid-item-card} {octicon}`rocket` Rocket propellant performance
:link: https://combustion-toolbox-website.readthedocs.io/en/latest/documentation/solver_rocket.html
{bdg-light}`Infinite-Chamber-Area` {bdg-light}`Finite-Chamber-Area`
:::

:::{grid-item-card} {octicon}`server` Extensive database with NASA’s 9-coefficient polynomial fits up to 20000 K
:link: https://combustion-toolbox-website.readthedocs.io/en/latest/documentation/db.html
{bdg-light}`NASA` {bdg-light}`Burcat` {bdg-light}`ATcT`
:::

:::{grid-item-card} {octicon}`verified` Excellent agreement with `NASA's CEA`, `CANTERA`, `Caltech's SD-Toolbox`, and `TEA`.
:link: https://combustion-toolbox-website.readthedocs.io/en/latest/validations.html
:::

:::{grid-item-card} {octicon}`graph` Predefined plots
:link: https://combustion-toolbox-website.readthedocs.io/en/latest/documentation/index.html
:::

:::{grid-item-card} {octicon}`download` Export results
:link: https://combustion-toolbox-website.readthedocs.io/en/latest/documentation/index.html
{bdg-light}`spreadsheet` {bdg-light}`.mat`
:::

:::{grid-item-card} {octicon}`versions` Compatible
:link: https://github.com/AlbertoCuadra/combustion_toolbox
{bdg-light}`windows` {bdg-light}`linux` {bdg-light}`mac`
:::

::::

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

# Gallery

We have several examples of what Combustion Toolbox can do. Here we show some results obtained from Combustion Toolbox.

<p align="center">
    <img src="_static/gif/example_DET.gif" width="800">
</p>

**Figure 1:** *Performance test, 100 Chapman-Jouguet pre-detonation and post-detonation states for a lean to rich CH4-air mixtures at standard conditions (T1 = 300 K and pressure p1 = 1 bar). The computational time was of 2.86 seconds using a Intel(R) Core(TM) i7-8700 CPU @ 3.20GHz for a set of 24 species considered.*

<p align="center">
    <img src="_static/img/Hugoniot_benchmarking.svg" width="450">
</p>
    
**Figure 2:** *Hugoniot curves for different molecular gases at pre-shock temperature T1 = 300 K and pressure p1 = 1 atm \[numerical results obtained with Combustion Toolbox (lines) and contrasted with NASA’s Chemical Equilibrium with Applications (CEA) code excluding ionization (symbols)\]*.
    
<p align="center">
    <img src="_static/img/run_validation_DET_CEA_3_molar.svg" width="1200">
</p>

**Figure 3:** *Variation of molar fraction for a CJ detonation for lean to rich CH4-air mixtures at standard conditions (T1 = 300 K and pressure p1 = 1 atm); line: numerical results obtained with Combustion Toolbox; circles: NASA's Chemical Equilibrium with Applications code. The computational time was of 6.68 seconds using a Intel(R) Core(TM) i7-8700 CPU @ 3.20GHz for a set of 26 species considered and a total of 351 case studies.*

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

If you use Combustion Toolbox in a publication, please cite it using the following reference:


* *Cuadra, A., Huete, C., & Vera, M. (2022). Combustion Toolbox: A MATLAB-GUI based open-source tool for solving gaseous combustion problems. (v0.9.92). Zenodo. https://doi.org/10.5281/zenodo.5554911.*

It can be handy the BibTeX format:

```bibtex
@misc{combustiontoolbox,
    author = "Cuadra, A and Huete, C and Vera, M",
    title = "Combustion Toolbox: A MATLAB-GUI based open-source tool for solving gaseous combustion problems",
    year = 2022,
    note = "Version 0.9.92",
    doi = {https://doi.org/10.5281/zenodo.5554911}
}
```