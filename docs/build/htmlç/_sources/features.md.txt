# Features

Combustion Toolbox is a a MATLAB-GUI based tool for solving gaseous combustion problems.
Features
  - The code stems from the minimization of the free energy of the system by using Lagrange multipliers combined with a Newton-Raphson method, upon condition that initial gas properties are defined by two functions of states (e.g., temperature and pressure)
  - When temperature is not externally imposed, the code retrieves a routine also based on Newton-Raphson method to find the equilibrium temperature
  - Solve processes that involve strong changes in the dynamic pressure, such as detonations and shock waves in the steady state
  - Find the equilibrium conditions of the different phenomena undergoing behind the shock: molecular vibrational excitation up to dissociation, and electronic excitation up to ionization, thereby providing the `properties of the gas in plasma state` within the temperature range given by the NASA’s 9-coefficient polynomial fits.
  - The corresponding thermodynamic properties of the species are modelled with `NASA’s 9-coefficient polynomial fits`, which ranges `up to 20000 K`, and the ideal gas equation of state
  - Results are in `excellent agreement with NASA’s Chemical Equilibrium with Applications (CEA) program`, CANTERA and Caltech’s Shock and Detonation Toolbox
  - All the routines and computations are encapsulated in a more comprehensive and user-friendly GUI
  - The code is in it’s transition to Python
  - Display predefined plots (e.g., molar fraction vs equilence ratio)
  - Export results in a spreadsheet (requires Excel)
  - Export results as a .mat format
* `Chemical equilibrium problems`
  - TP: Equilibrium composition at defined temperature and pressure
  - HP: Adiabatic temperature and composition at constant pressure
  - SP: Isentropic compression/expansion to a specified pressure
  - TV: Equilibrium composition at defined temperature and constant volume
  - EV: Adiabatic temperature and composition at constant volume
  - SV: Isentropic compression/expansion to a specified volume
* `Shock calculations:`
  - Pre-shock and post shock states
  - Equilibrium or frozen composition
  - Incident or reflected shocks
  - Chapman-Jouguet detonations and overdriven detonations
  - Reflected detonations
  - Oblique shocks/detonations
  - Shock polar for incident and reflected states
  - Hugoniot curves
  - Ideal jump conditions for a given adiabatic index and pre-shock Mach number
* `Rocket propellant performance assuming:`
  - Infinite-Area-Chamber model (IAC)
  - Finite-Area-Chamber model (FAC) - under development -
* All the routines and computations are encapsulated in a more comprehensive and `user-friendly GUI`
* The code `is in it’s transition to Python`
* Export results in a spreadsheet
* Export results as a .mat format
* `Display predefined plots` (e.g., molar fraction vs equilence ratio)


This project is also part of the PhD of [Alberto Cuadra-Lara](https://www.acuadralara.com/).


```{note}
The first final version v1.0.0 is expected to be released in April 2022. Check out the  upcoming features of [Combustion Toolbox v1.0.0](https://github.com/AlbertoCuadra/combustion_toolbox/projects/2).
```