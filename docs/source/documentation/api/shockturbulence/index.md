# Shock-Turbulence Interaction module

In this section, you will find the documentation of the shock–turbulence interaction (STI) module, which implements Linear Interaction Analysis (LIA) to quantify turbulence amplification across a shock wave interacting with weak upstream turbulence.

The module supports vortical, entropic, and acoustic disturbances, as well as fully compressible turbulent fields, under the assumptions of linear perturbations, inviscid flow, and thermochemical equilibrium across a thin relaxation layer. The formulation is based on our recent work:

> _Cuadra, A. Williams, C. T., Di Renzo, M., Vera, M., & Huete, C. (2026). The role of compressibility and vibrational excitation in hypersonic shock-turbulence interactions. Journal of Fluid Mechanics, 1032, A13. [doi:10.1017/jfm.2026.11356](https://doi.org/10.1017/jfm.2026.11355)._

## ShockTurbulenceSolver

```{eval-rst}
.. currentmodule:: src.+combustiontoolbox.+shockturbulence

.. automodule:: src.+combustiontoolbox.+shockturbulence.@ShockTurbulenceSolver
   :show-inheritance:
   :members:
```

## ShockTurbulenceModel

```{eval-rst}
.. currentmodule:: src.+combustiontoolbox.+shockturbulence

.. automodule:: src.+combustiontoolbox.+shockturbulence.@ShockTurbulenceModel
   :show-inheritance:
   :members:
```

## ShockTurbulenceModelVortical

```{eval-rst}
.. currentmodule:: src.+combustiontoolbox.+shockturbulence

.. automodule:: src.+combustiontoolbox.+shockturbulence.@ShockTurbulenceModelVortical
    :show-inheritance:
    :members:
```

## ShockTurbulenceModelVorticalEntropic

```{eval-rst}
.. currentmodule:: src.+combustiontoolbox.+shockturbulence

.. automodule:: src.+combustiontoolbox.+shockturbulence.@ShockTurbulenceModelVorticalEntropic
    :show-inheritance:
    :members:
```

## ShockTurbulenceModelAcoustic

```{eval-rst}
.. currentmodule:: src.+combustiontoolbox.+shockturbulence

.. automodule:: src.+combustiontoolbox.+shockturbulence.@ShockTurbulenceModelAcoustic
    :show-inheritance:
    :members:
```

## ShockTurbulenceModelCompressible

```{eval-rst}
.. currentmodule:: src.+combustiontoolbox.+shockturbulence

.. automodule:: src.+combustiontoolbox.+shockturbulence.@ShockTurbulenceModelCompressible
    :show-inheritance:
    :members:
```
