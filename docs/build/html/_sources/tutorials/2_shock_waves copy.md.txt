# Shock waves

In this section, we will cover how to determine the pre- and post-shock states across planar and oblique shock waves using the {mat:class}`~src.+combustiontoolbox.+shockdetonation.@ShockSolver.ShockSolver` class. This class is part of the **CT-SD** module, which provides robust tools for analyzing shock wave phenomena under a wide range of physical assumptions and flow conditions.

Shock waves are discontinuities in pressure, density, temperature, and velocity that form in compressible flows when disturbances propagate faster than the local speed of sound. The CT-SD module solves the Rankine–Hugoniot (RH) jump conditions to determine post-shock properties based on the upstream flow state. Solutions can be obtained for arbitrary multi-component gas mixtures assuming calorically perfect, thermally perfect, or calorically imperfect gas behavior.

The solver handles a variety of canonical shock problems, including:

* **SHOCK_I** – Planar incident shock wave  
* **SHOCK_R** – Planar reflected shock wave  
* **SHOCK_OBLIQUE** – Oblique incident shock wave  
* **SHOCK_OBLIQUE_R** – Oblique incident and reflected states  
* **SHOCK_POLAR** – Shock polar diagrams (incident states)  
* **SHOCK_POLAR_R** – Shock polar diagrams including reflected states  
* **SHOCK_POLAR_LIMITRR** – Shock polar diagrams in the limit of regular reflection  

These cases can be solved using different formulations, depending on the available data (e.g., upstream Mach number, upstream velocity, deflection angle, or wave angle). For chemically reacting mixtures, the solver can seamlessly interface with the [CT-EQUIL module](./1_chemical_equilibrium.md) to compute thermodynamic state consistent with the chosen caloric model (calorically perfect, thermally perfect, or calorically imperfect gas).

The governing jump conditions for a steady, one-dimensional shock wave are:

```{eval-rst}
.. math::
    :nowrap:

    \begin{align}
    \rho_1 u_1 &= \rho_2 u_2, \\
    p_1 + \rho_1 u_1^2 &= p_2 + \rho_2 u_2^2, \\
    h_1 + \frac{u_1^2}{2} &= h_2 + \frac{u_2^2}{2},
    \end{align}
```
where $\rho$ is the density, $u$ is the velocity, $p$ is the pressure, and $h$ is the specific enthalpy of the gas. The subscripts 1 and 2 denote the upstream (pre-shock) and downstream (post-shock) states, respectively. For oblique shocks, these relations are applied to the **normal component** of the velocity relative to the shock front.

Whether for shock-tube modeling, high-enthalpy flows, or oblique shock analysis in inlets and nozzles, the CT-SD module offers a flexible and modular framework compatible with all gas models in the Combustion Toolbox.


```{toctree}
    :caption: Contents
    :maxdepth: 1
    :titlesonly:
    
shock_waves/shock_waves_1
shock_waves/shock_waves_2
```