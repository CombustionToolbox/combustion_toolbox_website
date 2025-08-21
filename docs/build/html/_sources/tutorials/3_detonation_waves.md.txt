# Detonation waves

In this section, we will cover how to compute the pre- and post-detonation states for a variety of planar and oblique detonation configurations using the {mat:class}`~src.+combustiontoolbox.+shockdetonation.@DetonationSolver.DetonationSolver` class. This class is part of the **CT-SD** module and provides a robust framework for modeling detonation wave phenomena in chemically reactive gas mixtures.

Detonation waves are self-sustained shock-induced combustion waves, characterized by a leading shock front tightly coupled to an exothermic reaction zone. The CT-SD module computes the post-detonation state by solving the conservation equations across the wave along with thermochemical equilibrium calculations using the [CT-EQUIL module](./1_chemical_equilibrium.md). The solver supports both ideal Chapman–Jouguet detonations and more general overdriven and underdriven configurations.

The following canonical detonation problems are available:

* **DET** – Chapman–Jouguet detonation  
* **DET_R** – Reflected Chapman–Jouguet detonation  
* **DET_OBLIQUE** – Oblique detonation wave  
* **DET_POLAR** – Detonation polar diagrams  
* **DET_OVERDRIVEN** – Overdriven detonation  
* **DET_OVERDRIVEN_R** – Overdriven reflected detonation  
* **DET_UNDERDRIVEN** – Underdriven detonation  
* **DET_UNDERDRIVEN_R** – Underdriven reflected detonation  

The chemical composition of detonation products is computed at equilibrium using the CT-EQUIL module, and the thermodynamic state is determined by solving the governing conservation laws across a one-dimensional steady detonation wave:

```{eval-rst}
.. math::
    :nowrap:

    \begin{align}
    \rho_1 u_1 &= \rho_2 u_2, \\\\
    p_1 + \rho_1 u_1^2 &= p_2 + \rho_2 u_2^2, \\\\
    h_1 + \frac{u_1^2}{2} &= h_2 + \frac{u_2^2}{2},
    \end{align}
```
where $\rho$ is the density, $u$ is the velocity, $p$ is the pressure, and $h$ is the specific enthalpy of the gas. Subscripts 1 and 2 denote the upstream (pre-detonation) and downstream (post-detonation) states. For oblique detonations, the jump conditions are applied to the normal component of the flow velocity relative to the wave front.

Whether for theoretical analysis, propulsion applications, or detonation structure studies, the CT-SD module offers a flexible, modular solution fully integrated into the Combustion Toolbox framework.


```{toctree}
    :caption: Contents
    :maxdepth: 1
    :titlesonly:

detonation_waves/detonation_waves_1
``` 

