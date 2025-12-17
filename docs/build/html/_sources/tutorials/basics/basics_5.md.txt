# Defining the caloric gas model

Thermodynamic property calculations in the Combustion Toolbox depend on the **caloric gas model** used to describe the variation of specific heats and chemical effects. This behavior is controlled through the {mat:class}`~src.+combustiontoolbox.+core.@CaloricGasModel.CaloricGasModel` enumeration class, which provides the following options:

- **Calorically perfect gas** — {mat:attr}`~src.+combustiontoolbox.+core.@CaloricGasModel.CaloricGasModel.perfect`. Assumes constant specific heats.
- **Thermally perfect gas** — {mat:attr}`~src.+combustiontoolbox.+core.@CaloricGasModel.CaloricGasModel.thermallyPerfect`. Assumes temperature-dependent specific heats.
- **Calorically imperfect gas** — {mat:attr}`~src.+combustiontoolbox.+core.@CaloricGasModel.CaloricGasModel.imperfect`. Assumes temperature-dependent properties and chemical equilibrium (**default**).

## Selecting a caloric gas model

A caloric gas model is defined by selecting one of the enumeration values:

```matlab
caloricGasModel = CaloricGasModel.perfect;
caloricGasModel = CaloricGasModel.thermallyPerfect;
caloricGasModel = CaloricGasModel.imperfect;
```

## Modifying caloric model

An existing caloric gas model can be modified using the provided setter methods:

```matlab
caloricGasModel = caloricGasModel.setPerfect();
caloricGasModel = caloricGasModel.setThermallyPerfect();
caloricGasModel = caloricGasModel.setImperfect();
```

## Using the caloric gas model in solvers

The caloric gas model is passed directly to solvers, such as the {mat:class}`~src.+combustiontoolbox.+shockdetonation.@ShockSolver.ShockSolver`, using the `caloricGasModel` option.

```matlab
solver = ShockSolver( 'problemType', 'SHOCK_I', 'caloricGasModel', CaloricGasModel.imperfect);
```

This allows the same physical problem to be solved using different thermodynamic assumptions.

## Checking the caloric gas model

To check which caloric model is currently selected, use the is* methods provided by the
{mat:class}~src.+combustiontoolbox.+core.@CaloricGasModel.CaloricGasModel enumeration:

```matlab
isPerfect          = caloricGasModel.isPerfect();
isThermallyPerfect = caloricGasModel.isThermallyPerfect();
isImperfect        = caloricGasModel.isImperfect();
```

These methods return a logical value (`true`/`false`) and are useful for branching logic or reporting.

## Legacy compatibility

For compatibility with legacy solver flags, the static method {mat:func}`~src.+combustiontoolbox.+core.@CaloricGasModel.CaloricGasModel.fromFlag`
can be used:

```matlab
caloricGasModel = CaloricGasModel.fromFlag(FLAG_TCHEM_FROZEN, FLAG_FROZEN);
```



