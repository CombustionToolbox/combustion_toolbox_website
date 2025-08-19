# GUI

Routines to generate the app, add-ons, assets, and all the necessary functions to be compatible with the plain code and extend its functionality.

## Combustion Toolbox GUI

:::{figure} ../../_static/img/cuadra2022/gui_cuadra2024_labels_1.svg
:name: gui_cuadra2024_labels_1
:width: 500px
:align: center

Post-process of results using the GUI of the adiabatic combustion for a lean-to-rich acetylene ($\text{C}_2\text{H}_2$)-air mixture at standard conditions ($T_1 = 300$ K and $p_1 = 1$ bar); labels: name of the different components of the GUI. In particular, the numerical results correspond to $\phi = 0.5$ (selected case in the tree component) [part 1].
:::

:::{figure} ../../_static/img/cuadra2022/gui_cuadra2024_labels_2.svg
:name: gui_cuadra2024_labels_2
:width: 500px
:align: center

Post-process of results using the GUI of the adiabatic combustion for a lean-to-rich acetylene ($\text{C}_2\text{H}_2$)-air mixture at standard conditions ($T_1 = 300$ K and $p_1 = 1$ bar); labels: name of the different components of the GUI. In particular, the numerical results correspond to $\phi = 0.5$ (selected case in the tree component) [part 2].
:::

:::{figure} ../../_static/img/cuadra2022/gui_cuadra2024_labels_34_vertical.svg
:name: gui_cuadra2024_labels_34_vertical
:width: 500px
:align: center
Post-process of results using the GUI of the adiabatic combustion for a lean-to-rich acetylene ($\text{C}_2\text{H}_2$)-air mixture at standard conditions ($T_1 = 300$ K and $p_1 = 1$ bar); labels: name of the different components of the GUI. In particular, the numerical results correspond to $\phi = 0.5$ (selected case in the tree component) [part 3].
:::


<!-- :::{dropdown} Routines
```{eval-rst}
.. autoclass:: src.gui.combustion_toolbox
   :members:
```
::: -->

<!-- ## Utility functions

A collection of functions for Combustion Toolbox GUI.

***

:::{dropdown} Routines
```{eval-rst}
.. automodule:: src.gui.utils
   :members:
```
::: -->

## Add-ons

The Add-ons included in CT are:
* ```uielements```: to select and analyse the species in the database. The species from Third Millenium Database {cite:p}`burcat2005` are denoted with suffix _M (see Fig. 1).
* ```uipreferences```: to set all the preferences of Combustion Toolbox (see Fig. 2).
* ```uifeedback```: to report bug/inquiries of Combustion Toolbox (see Fig. 3).
* ```uivalidations```: to reproduce all the validations of Combustion Toolbox (see Fig. 4).
* ```uiabout```: to know who are the developers and get useful links (see Fig. 5).

<br>

:::{figure} ../../_static/img/cuadra2022/gui_uielements.svg
:name: fig_gui_uielements
:width: 800px
:align: center
Add-on uielements.
:::

:::{figure} ../../_static/img/cuadra2022/gui_uipreferences.svg
:name: fig_gui_uipreferences
:width: 800px
:align: center
Add-on uipreferences.
:::

:::{figure} ../../_static/img/cuadra2022/gui_uifeedback.svg
:name: fig_gui_uifeedback
:width: 400px
:align: center
Add-on uifeedback.
:::

:::{figure} ../../_static/img/cuadra2022/gui_uivalidation.svg
:name: fig_gui_uivalidation
:width: 800px
:align: center
Add-on uivalidation.
:::

:::{figure} ../../_static/img/cuadra2022/gui_uiabout.svg
:name: fig_gui_uiabout
:width: 800px
:align: center
Add-on uiabout.
:::
