# API Documentation

```{note}
Please note that the documentation is currently under development.
```

Here we can find the documentation for the routines implemented in the Combustion Toolbox (CT). The source code contains the following folders and files in the main directory:

```
.combustion_toolbox
|-- +combustiontoolbox
|-- databases
|-- examples
|-- gui
|-- installer
|-- utils
|-- validations
|-- run_test.m
|-- CODE_OF_CONDUCT.md
|-- CONTENTS.m
|-- CONTRIBUTING.md
|-- CONTRIBUTORS.md
|-- INSTALL.m
|-- LICENSE.md
`-- README.md
```

These top-layer folders contain the following:

* ```+combustiontoolbox```: contains functions for the different modules, including CT-EQUIL, CT-SD, CT-ROCKET, and CT-TURBULENCE, along with routines for initializing CT.
* ```databases```: encompasses all databases utilized by CT.
* ```examples```: contains examples showcasing the usage of CT modules.
* ```gui```: houses functions and assets required to generate the app (GUI), add-ons, and extend the functionality of the plain code to the GUI.
* ```installer```: hosts installation files (toolbox and royalty-free stand-alone version).
* ```utils```: accommodates utility functions with different purposes.
* ```validations```: includes routines used to validate CT with the results obtained with other codes, unit testing files for ensuring correct code functionality, and all graphs generated from these verification processes.

Regarding the files in the main source folder, we have the following: the file `run_test.m` runs the unit tests of CT. The file `CONTENTS.m` is a script that briefly describes the problems that can be solved with CT. The file `INSTALL.m` is a script that installs the CT code and the GUI. The file `LICENSE.md` contains the license of CT (GNU General Public License v3.0). Finally, the file `README.md` is the official description in the GitHub repository.


```{toctree}
    :caption: 'Contents:'
    :maxdepth: 2

common/index
databases/index
core/index
equilibrium/index
shockdetonation/index
rocket/index
turbulence/index
utils/index
```