# Framework initialization
To begin, start MATLAB and navigate to the folder where you have downloaded the Combustion Toolbox. To include files in `PATH`, run this command in the command window:
```matlab
INSTALL()
```

First, using the Combustion Toolbox, you have to initialize the tool (load databases, set default variables, etc.). To do that, type the following at the prompt:
```matlab
self = App()
```

If files contained in the Combustion Toolbox are correctly defined, you should see something like this:
```matlab
self = 

  struct with fields:

            E: [1×1 struct]
            S: [1×1 struct]
            C: [1×1 struct]
         Misc: [1×1 struct]
           PD: [1×1 struct]
           PS: [1×1 struct]
           TN: [1×1 struct]
    DB_master: [1×1 struct]
           DB: [1×1 struct]
```

This `self` variable encapsulates essential shared data necessary for calculations and typically serves as the first argument in most CT routines. Thus, the data passed between the functions has been organized in a hierarchical tree structure (except for the GUI, which is based on OOP) as shown in Fig.1, namely:
   * `self (App)`: parent node; contains all the data of the code, e.g., databases, input values, and results.
   * `Constants (C)`: contains constant values.
   * `Elements (E)`: contains data of the chemical elements in the problem (names and indices for fast data access).
   * `Species (S)`: contains data of the chemical species in the problem (names and indices for fast data access), as well as lists (cells) with the species for complete combustion.
   * `Problem Description (PD)`: contains data of the problem to solve, e.g., initial mixture (composition, temperature, pressure), problem type, and its configuration.
   * `Problem Solution (PS)`: contains results (mixtures).
   * `Tuning Properties (TN)`: contains parameters that control the numerical error of the algorithms implemented in the different modules.
   * `Miscellaneous (Misc)`: contains values that configure the auto-generated plots and export setup, as well as flags.
   * `Database master (DB_master)`: a structured thermochemical database including data from {cite:t}`Mcbride2002, burcat2005`.
   * `Database (DB)`: a structured thermochemical database with *griddedInterpolant* objects (see MATLAB built-in function <tt>griddedInterpolant.m</tt>) that contain piecewise cubic Hermite interpolating polynomials (PCHIP) {cite:p}`fritsch1980` for faster data access. 

   <br>
   
<p align="center">
    <img src="../../_static/img/cuadra2022/sketch_tree_structure.svg" width="250">
</p>

```{eval-rst}
.. only:: latex

    .. image:: ../../_static/img/cuadra2022/sketch_tree_structure.pdf
        :width: 150px
        :align: center
```

**Figure 1:** *Combustion Toolbox hierarchical data tree structure, where* <tt> `App.m` </tt> *is the initialization function.*