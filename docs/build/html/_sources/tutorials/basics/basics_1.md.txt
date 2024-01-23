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