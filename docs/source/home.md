<!-- Logo -->
<p class= "only-light" align="center">
    <img alt="UC3M" style="border-width:0" src="_static/img/logo.svg" width="1500"/>
</p>

<p class= "only-dark" align="center">
    <img alt="UC3M" style="border-width:0" src="_static/img/logo_dark.svg" width="1500"/>
</p>

<!-- Intro -->
<br> <center> <b> A MATLAB-GUI based open-source tool for solving gaseous combustion problems </b> </center> <br>
    

<p class= "only-light" align="center">
    <img alt="CT layout" style="border-width:0" src="_static/img/cuadra2022/modules_CT.svg" width="400"/>
</p>

<p class= "only-dark" align="center">
    <img alt="CT layout" style="border-width:0" src="_static/img/cuadra2022/modules_CT_dark_v2.svg" width="400"/>
</p>


<!-- Grid -->
::::{grid} 1 1 1 3
:margin: 4 4 0 0
:gutter: 1

:::{grid-item-card} {octicon}`package` Robust modular kernel
:link: https://combustion-toolbox-website.readthedocs.io/en/latest/documentation/api/equilibrium/index.html
`Robust`, `object-oriented`, and `fast` chemical equilibrium computations.
:::

:::{grid-item-card} {octicon}`device-desktop` Interactive App
:link: https://github.com/AlbertoCuadra/combustion_toolbox/archive/refs/heads/master.zip
The code is encapsulated in a `user-friendly` GUI with tons of capabilities.
:::

:::{grid-item-card} {octicon}`globe` Open source
:link: https://github.com/AlbertoCuadra/combustion_toolbox
Completely open source, GUI included!<br>
{bdg-light}`GitHub` {bdg-info}`GPLv3`
:::

::::

# Combustion Toolbox in action

<p align="center">
    <img src="_static/gif/example_det_overdriven_gui.gif" width="345">&nbsp;
    <img src="_static/gif/example_det_overdriven.gif" width="360">
</p>

# Combustion Toolbox capabilities

::::{grid} 1 2 2 2
:margin: 4 4 0 0
:gutter: 1

:::{grid-item-card} {octicon}`cpu` Robust chemical equilibrium computations
:link: https://combustion-toolbox-website.readthedocs.io/en/latest/documentation/api/equilibrium/index.html

{bdg-light}`TP` {bdg-light}`HP` {bdg-light}`SP` {bdg-light}`TV` {bdg-light}`EV` {bdg-light}`SV` {bdg-light}`frozen` {bdg-light}`plasma state`

:::

:::{grid-item-card} {octicon}`device-desktop` Interactive App
:link: https://github.com/AlbertoCuadra/combustion_toolbox/archive/refs/heads/master.zip
Over 10K lines of code encapsulated in a `user-friendly` GUI with tons of capabilities.
{bdg-light}`Toolbox` {bdg-light}`Standalone (royalty-free)`
:::

:::{grid-item-card} {octicon}`tab` Shocks and detonations pre- and post-shock states 
:link: https://combustion-toolbox-website.readthedocs.io/en/latest/documentation/api/shockdetonation/index.html
{bdg-light}`Incident` {bdg-light}`Reflected` {bdg-light}`Oblique` {bdg-light}`Shock polar` {bdg-light}`Detonations polar` {bdg-light}`Regular Reflections` 
:::

:::{grid-item-card} {octicon}`globe` Open source
:link: https://github.com/AlbertoCuadra/combustion_toolbox
Completely open source, GUI included!
{bdg-light}`GitHub` {bdg-light}`FileExchange` {bdg-light}`Zenodo` {bdg-info}`GPLv3`
:::

::::

::::{grid} 1 2 2 3
:margin: 4 4 0 0
:gutter: 1

:::{grid-item-card} {octicon}`rocket` Rocket propellant performance
:link: https://combustion-toolbox-website.readthedocs.io/en/latest/documentation/api/rocket/index.html
{bdg-light}`Infinite-Chamber-Area` {bdg-light}`Finite-Chamber-Area`
:::

:::{grid-item-card} {octicon}`server` Extensive database with NASA’s 9-coefficient polynomial fits up to 20000 K
:link: https://combustion-toolbox-website.readthedocs.io/en/latest/documentation/api/databases/index.html
{bdg-light}`NASA` {bdg-light}`Burcat` {bdg-light}`ATcT`
:::

:::{grid-item-card} {octicon}`verified` Excellent agreement with `NASA's CEA`, `Cantera`, `Caltech's SD-Toolbox`, and `TEA`
:link: https://combustion-toolbox-website.readthedocs.io/en/latest/validations.html
:::

:::{grid-item-card} {octicon}`graph` Predefined plots
:link: https://combustion-toolbox-website.readthedocs.io/en/latest/documentation/api/utils/index.html#display-functions
:::

:::{grid-item-card} {octicon}`download` Export results
:link: https://combustion-toolbox-website.readthedocs.io/en/latest/documentation/api/utils/index.html#export-functions
{bdg-light}`.xls` {bdg-light}`.mat`
:::

:::{grid-item-card} {octicon}`versions` Compatible
:link: https://github.com/AlbertoCuadra/combustion_toolbox
{bdg-light}`Windows` {bdg-light}`Linux` {bdg-light}`Mac`
:::

::::

Combustion Toolbox {cite:p}`cuadra2024a_preprint` is a GUI-based thermochemical code written in MATLAB with an equilibrium kernel based on the mathematical formulation set forth by NASA in its CEA code {cite:p}`gordon1994`. The thermodynamic properties of the gaseous species are modeled with the ideal gas equation of state (EoS), and an up-to-date version of NASA's 9-coefficient polynomial fits from {cite:p}`Mcbride2002,burcat2005,ruscic2005`. CT is a new object-oriented thermochemical code written from scratch in a modular architectural format composed of three main modules: CT-EQUIL, CT-SD, and CT-ROCKET. 

* **CT-EQUIL:** computes the composition at the equilibrium of multi-component gas mixtures that undergo canonical thermochemical transformations from an initial state (reactants), defined by its initial composition, temperature, and pressure, to a final state (products), defined by a set of chemical species (in gaseous---included ions---or pure condensed phase) and two thermodynamic state functions, such as enthalpy and pressure, e.g., for isobaric combustion processes.
* **CT-SD:** solves steady-state shock and detonation waves in either normal or oblique incidence.
* **CT-ROCKET:** computes the theoretical performance of rocket engines under highly idealized conditions.

Even though all modules are enclosed in a user-friendly GUI, they can also be accessed from MATLAB's command line (in plain code mode). 

There is a fourth closed-source (i.e., proprietary) module, CT-EXPLO, that estimates the theoretical properties of high explosive mixtures and multi-component propellants with non-ideal EoS. Although still under development, CT-EXPLO is distributed in its current form as the thermochemical module of SimEx {cite:p}`simex2022` subject to a proprietary license. Further details on this module will be provided elsewhere. 

This MATLAB-GUI thermochemical code represents the core of an ongoing research work the has been used to investigate a series of problems during the last few years {cite:p}`Cuadra2020,huete2021,simex2022,cuadra2023_aiaa`.

# Start here!


::::{grid} 1 2 2 3
:margin: 4 4 0 0
:gutter: 1

:::{grid-item-card} {octicon}`tasklist` Tutorials
:link: https://combustion-toolbox-website.readthedocs.io/en/latest/tutorials.html

New to Combustion Toolbox?
:::

:::{grid-item-card} {octicon}`note` Examples
:link: https://combustion-toolbox-website.readthedocs.io/en/latest/examples.html

See how the toolbox can be used in practical scenarios.
:::

:::{grid-item-card} {octicon}`repo` API Documentation
:link: https://combustion-toolbox-website.readthedocs.io/en/latest/documentation/api/index.html

Let's check the documentation of almost (every) functions.
:::

::::

# Gallery

Here we show some results obtained using the Combustion Toolbox.

<p class= "only-light" align="center">
    <img alt="TP with condensed species" style="border-width:0" src="_static/img/cuadra2022/TP_scoggins2015_wide.svg" width="1200"/>
</p>

<p class= "only-dark" align="center">
    <img alt="TP with condensed species" style="border-width:0" src="_static/img/cuadra2022/TP_scoggins2015_wide_dark.svg" width="1200"/>
</p>

**Figure 1:** *Variation of the molar fractions $X_j$ for a TP transformation of a Silica-Phenolic mixture at atmospheric pressure $(p = 1$ atm$)$ with $T \in [200, 5000]$; line: numerical results obtained with CT; symbols: numerical results obtained with NASA's CEA {cite:p}`gordon1994`.*

<p class= "only-light" align="center">
    <img alt="Hugoniot curves" style="border-width:0" src="_static/img/Hugoniot_benchmarking.svg" width="500"/>
</p>

<p class= "only-dark" align="center">
    <img alt="Hugoniot curves" style="border-width:0" src="_static/img/Hugoniot_benchmarking_dark.svg" width="500"/>
</p>

**Figure 2:** *Hugoniot curves for different molecular gases at pre-shock temperature $T_1 = 300$ K and pressure $p_{1} = 1$ atm \[numerical results obtained with Combustion Toolbox (lines) and contrasted with NASA’s Chemical Equilibrium with Applications (CEA) code {cite:p}`gordon1994` excluding ionization (symbols)\]*.

<p class= "only-light" align="center">
    <img alt="Chapman-Jouguet detonation" style="border-width:0" src="_static/img/run_validation_DET_CEA_3_molar.svg" width="1200"/>
</p>

<p class= "only-dark" align="center">
    <img alt="Chapman-Jouguet detonation" style="border-width:0" src="_static/img/run_validation_DET_CEA_3_molar_dark.svg" width="1200"/>
</p>

**Figure 3:** *Variation of molar fraction for a CJ detonation for lean to rich CH4-air mixtures at standard conditions $(T_1 = 300$ K and pressure $p_1 = 1$ atm$)$; line: numerical results obtained with Combustion Toolbox; circles: NASA's Chemical Equilibrium with Applications code {cite:p}`gordon1994`. The computational time was of 6.68 seconds using a Intel(R) Core(TM) i7-8700 CPU @ 3.20GHz for a set of 26 species considered and a total of 351 case studies.*

<p class= "only-light" align="center">
    <img alt="Shock polar diagrams" style="border-width:0" src="_static/img/cuadra2022/shock_polar_all_4.svg" width="1000"/>
</p>

<p class= "only-dark" align="center">
    <img alt="Shock polar diagrams" style="border-width:0" src="_static/img/polar_shock_full_and_frozen_both_air_complete_dark.svg" width="1000"/>
</p>

**Figure 4:** *Pressure-deflection (a) and wave angle-deflection (b) shock polar diagrams for air (79\% N2, 21\% O2) at pre-shock temperature $T_1 = 300$ K and pressure $p_1 = 1$ atm, and a range of pre-shock Mach numbers M1 between 2 and 14; line: calorically imperfect gas with ionization/dissociation; dashed: calorically imperfect gas with frozen chemistry; circles: results obtained with Cantera {cite:p}`cantera` within Caltech’s SD-Toolbox {cite:p}`Browne2008SDT, Browne2008`; diamonds: maximum deflection angle* $\theta_{\rm max}$.

# Contributing

Please send feedback or inquiries to [acuadra@ing.uc3m.es](mailto:acuadra@ing.uc3m.es)

Thank you for testing the Combustion Toolbox!

# Acknowledgements
* Combustion Toolbox's color palette is obtained from the following repository: Stephen (2021). ColorBrewer: Attractive and Distinctive Colormaps (https://github.com/DrosteEffect/BrewerMap), GitHub. Retrieved December 3, 2021.
* For validations, Combustion Toolbox uses CPU Info from the following repository: Ben Tordoff (2022). CPU Info (https://github.com/BJTor/CPUInfo/releases/tag/v1.3), GitHub. Retrieved March 22, 2022.
* Combustion Toolbox's splash screen is based on a routine from the following repository: Ben Tordoff (2022). SplashScreen (https://www.mathworks.com/matlabcentral/fileexchange/30508-splashscreen), MATLAB Central File Exchange. Retrieved October 15, 2022.
* Combustion Toolbox's periodic table layout is based in the following repository: Bruno Salcedo (2018). latex-periodic-table (https://github.com/brunosalcedo/latex-periodic-table), Github. Retrieved October 15, 2022.

# People

* **[Alberto Cuadra-Lara](https://acuadralara.com/)** - *Lead developer*
* **César Huete** - *Advisor*
* **Marcos Vera** - *Advisor*

Grupo de Mecánica de Fluidos, Universidad Carlos III, Av. Universidad 30, 28911, Leganés, Spain

See also the list of [contributors](https://github.com/AlbertoCuadra/combustion_toolbox/blob/master/CONTRIBUTORS.md) who participated in this project.

# Citing Combustion Toolbox

If you use the Combustion Toolbox in a publication, please cite it using the following references:

* *Cuadra, A., Huete, C., & Vera, M. (2024). Combustion Toolbox: An open-source thermochemical code for gas- and condensed-phase problems involving chemical equilibrium. [arXiv:2409.15086](https://doi.org/10.48550/arXiv.2409.15086).*
* *Cuadra, A., Huete, C., & Vera, M. (2024). Combustion Toolbox: A MATLAB-GUI based open-source tool for solving gaseous combustion problems. Version 1.1.3. Zenodo. [doi:10.5281/zenodo.5554911](https://doi.org/10.5281/zenodo.5554911).*

It can be handy the BibTeX format:

```bibtex
@article{cuadra2024a_preprint,
    title         = {{Combustion Toolbox: An open-source thermochemical code for gas- and condensed-phase problems involving chemical equilibrium}},
    author        = {Cuadra, A. and Huete, C. and Vera, M.},
    journal       = {{arXiv preprint arXiv:2409.15086}},
    year          = {2024},
    eprint        = {2409.15086},
    archivePrefix = {arXiv},
    primaryClass  = {physics.chem-ph},
    doi           = {10.48550/arXiv.2409.15086}
}

@misc{combustiontoolbox,
    author  = "Cuadra, A. and Huete, C. and Vera, M.",
    title   = "{Combustion Toolbox: A MATLAB-GUI based open-source tool for solving gaseous combustion problems}",
    year    = 2024,
    note    = "Version 1.1.3",
    doi     = {https://doi.org/10.5281/zenodo.5554911}
}
```