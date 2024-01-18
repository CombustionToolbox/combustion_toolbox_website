# Installation

## Downloading the Code

You can download the Combustion Toolbox from several sources:

::::{grid} 1 2 2 3
:margin: 4 4 0 0
:gutter: 1
                
:::{grid-item-card} <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16" width="200px" height="200px"> <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path> </svg> GitHub
:link: https://github.com/AlbertoCuadra/combustion_toolbox
:::

:::{grid-item-card} <div class="matlab"></div> MATLAB FileExchange
:link: https://in.mathworks.com/matlabcentral/fileexchange/101088-combustion-toolbox?requestedDomain=
:::

:::{grid-item-card} <div class="zenodo"></div> Zenodo
:link: https://doi.org/10.5281/zenodo.5554911
:::

::::

## Installing the Code

To install the Combustion Toolbox, you can use the provided `INSTALL.m` file. Here's how to install the toolbox:

1. Navigate to the directory where you downloaded the code.
2. Run the `INSTALL.m` file using the following command in the MATLAB Command Window:

```matlab
INSTALL()
```

3. This will add the necessary folders to the MATLAB path and also install the Combustion Toolbox GUI. You can now use the Combustion Toolbox in your MATLAB code.

If you wish to install the GUI only, you can run the following command:
```matlab
INSTALL('install', 'gui')
```

Alternatively, you can execute the `combustion_toolbox_app.mlappinstall` file in the MATLAB Command Window to install the GUI, which will be available through the MATLAB Apps Toolbar.

The standalone version can be installed by running `combustion_toolbox_standalone_installer.exe` in the installer folder. This royalty-free version requires MATLAB Runtime framework (automatically installed during installation, **requires an internet connection**).

## Using the Combustion Toolbox

The Combustion Toolbox can be used in two ways:

* Using the MATLAB's desktop environment to obtain all the versatility of the plain code.
* Using the Graphical User Interface (GUI) and forget about code.
  
To use the Combustion Toolbox in the MATLAB desktop environment, you can call the functions from your MATLAB code directly, e.g., `App()`.

To use the GUI, simply type `combustion_toolbox` or `combustion_toolbox_app` in the MATLAB Command Window, or click on the app icon in the MATLAB apps toolbar. This will open the Combustion Toolbox GUI, which provides a user-friendly interface for accessing and using the package.

```{note}
If you encounter any issues during the installation process or while using the Combustion Toolbox, please refer to the "Issues" section of the GitHub repository or contact us directly at [acuadra@ing.uc3m.es](mailto:acuadra@ing.uc3m.es) for assistance.
```