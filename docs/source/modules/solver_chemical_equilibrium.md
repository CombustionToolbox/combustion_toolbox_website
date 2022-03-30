# Chemical equilibrium

In this section, you will find the documentation of the kernel of the code, which is used to obtain the chemical equilibrium composition for a desired thermochemical transformation, e.g., constant enthalpy and pressure. It also includes routines to compute chemical equilibrium assuming a complete combustion and the calculation of the thermodynamic derivates. The code stems from the minimization of the free energy of the system by using Lagrange multipliers combined with a Newton-Raphson method, upon condition that initial gas properties are defined by two functions of states. e.g., temperature and pressure.


<!-- <div class="note">
<b>Note</b><br>The kernel of the code is based on Gordon, S., & McBride, B. J. (1994). NASA reference publication, 1311.
</div> -->

```{note}
   The kernel of the code is based on Gordon, S., & McBride, B. J. (1994). NASA reference publication, 1311.
```

***

```{eval-rst}
.. collapse:: Routines

   .. automodule:: src.solver.chemical_equilibrium
      :members:
```