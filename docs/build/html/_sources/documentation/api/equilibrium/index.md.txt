# Thermochemical equilibrium module

In this section, you will find the documentation of the kernel of the code, which is used to obtain the chemical equilibrium composition for a desired thermochemical transformation, e.g., constant enthalpy and pressure. It also includes routines to compute chemical equilibrium assuming a complete combustion and the calculation of the thermodynamic derivates. The code stems from the minimization of the free energy of the system by using Lagrange multipliers combined with a Newton-Raphson method, upon condition that initial gas properties are defined by two functions of states, e.g., temperature and pressure.

## EquilibriumSolver

```{eval-rst}
.. currentmodule:: src.+combustiontoolbox.+equilibrium

.. automodule:: src.+combustiontoolbox.+equilibrium.@EquilibriumSolver
   :show-inheritance:
   :members:
```