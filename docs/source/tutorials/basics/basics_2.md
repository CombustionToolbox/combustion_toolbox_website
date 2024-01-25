# Accessing the databases

In the preceding section, we stated that to initialize the Combustion Toolbox (load databases, default parameters, etc.), we have to run the following command:

```matlab
self = App();
```

Now, let's delve into how we can access the databases incorporated within the Combustion Toolbox (CT). There are two main types of databases: `DB_master` and `DB`. The former comprises all data from from {cite:t}`Mcbride2002, burcat2005`, while the latter contains the same data in a more optimized format, ensuring faster data access. 

````{tip}
Distinguishing between `DB_master` and `DB` is crucial because the latter, due to the utilization of *griddedInterpolant* objects, has a significantly larger size (~36 MB). A streamlined version of `DB` can be generated to conserve memory and reduce loading time (~1 second for 3603 species) when initializing CT. To achieve this, execute:

```matlab
self.DB = generate_DB(self.DB_master, {'O2', 'N2'});
```

Subsequently, save the <tt>self.DB</tt> variable in the `databases` folder as <tt>DB.mat</tt> to be loaded in the remaining sessions.
````


## Finding specific chemical species

The thermodynamic data of the species, e.g., C<sub>gr</sub>, can be accessed as follows:

```matlab
self.DB.Cbgrb;
```

This command will yield information similar to the following:

```matlab
      FullName: 'C(gr)'
          name: 'Cbgrb'
      comments: 'Graphite. Ref-Elm. TRC(4/83) vc,uc,tc1000-1002.               '
     txFormula: 'C   1.00    0.00    0.00    0.00    0.00'
            mm: 12.0107
            hf: 0
            ef: 0
         phase: 1
             T: [200 229.1457 258.2915 287.4372 316.5829 345.7286 … ] (1×200 double)
       cPcurve: [1×1 griddedInterpolant]
       h0curve: [1×1 griddedInterpolant]
       s0curve: [1×1 griddedInterpolant]
       g0curve: [1×1 griddedInterpolant]
        ctTInt: 3
        tRange: {[200 600]  [600 2000]  [2000 6000]}
    tExponents: {[-2 -1 0 1 2 3 4 0]  [-2 -1 0 1 2 3 4 0]  [-2 -1 0 1 2 3 4 0]}
             a: {[1×8 double]  [1×8 double]  [1×8 double]}
             b: {[8.9439e+03 -72.9582]  [1.3984e+04 -44.7718]  [5.8481e+03 -23.5093]}
```

These details offer comprehensive insights into the thermodynamic properties of the specified species in the Combustion Toolbox database. We have the following fields:

* `FullName`: full name of the species.
* `name`: short name of the species as defined in the database.
* `comments`: comments about the species.
* `txFormula`: chemical formula of the species.
* `mm`: molar mass [g/mol].
* `hf`: standard enthalpy of formation [J/mol].
* `ef`: standard internal energy of formation [J/mol].
* `phase`: phase of the species (0: gas, 1: liquid or solid).
* `T`: temperature vector [K].
* `cPcurve`: *griddedInterpolant* object containing the standard specific heat capacity at constant pressure [J/mol-K].
* `h0curve`: *griddedInterpolant* object containing the standard enthalpy [J/mol].
* `s0curve`: *griddedInterpolant* object containing the standard entropy [J/mol-K].
* `g0curve`: *griddedInterpolant* object containing the standard Gibbs free energy [J/mol].
* `ctTInt`: number of temperature intervals.
* `tRange`: temperature intervals.
* `tExponents`: temperature exponents for the standard specific heat capacity at constant pressure, standard enthalpy, and standard entropy, respectively.
* `a`: coefficients of the polynomial.
* `b`: coefficients of the polynomial.

## Finding list of chemical species with given chemical elements

To find the list of species that contain only some chemical elements, e.g., O and H, we can use the following command:

`````{tab-set}
````{tab-item} NASA database

```matlab
list_species = find_products(self, {'O', 'H'})
```

which will yield the following output:


```matlab

list_species =

  1×15 cell array

  Columns 1 through 7

    {'HO2'}    {'H2O'}    {'H2O2'}    {'OH'}    {'H2Obcrb'}    {'H2ObLb'}    {'H2O2bLb'}

  Columns 8 through 15

    {'O'}    {'O2'}    {'O3'}    {'O2bLb'}    {'O3bLb'}    {'H'}    {'H2'}    {'H2bLb'}
```

```{note}
By default, the <tt>find_products.m</tt> function looks for species in the NASA database and does not consider ionized species. To search for species in Burcat's database and include ionized species, set `flag_burcat` and `flag_ion` options to `true`. Alternatively, we can modify the default value in the <tt>Species.m</tt> file. Chemical species from the Third Millennium database (Burcat) are indicated with the subscript `_M`.
```

````

````{tab-item} Third Millennium database (Burcat)

```matlab
list_species = find_products(self, {'O', 'H'}, 'flag_burcat', true)
```

which will yield the following output:


```matlab

list_species =

  1×25 cell array

  Columns 1 through 7

    {'HO2'}    {'H2O'}    {'H2O2'}    {'OH'}    {'H2Obcrb'}    {'H2ObLb'}    {'H2O2bLb'}

  Columns 8 through 14

    {'OH_M'}    {'HO2_M'}    {'HO3_M'}    {'H2O2_M'}    {'H2O3_M'}    {'HOOOH_M'}    {'O'}

  Columns 15 through 21

    {'O2'}    {'O3'}    {'O2bLb'}    {'O3bLb'}    {'O_M'}    {'O2_M'}    {'O3_M'}

  Columns 22 through 25

    {'O4_M'}    {'H'}    {'H2'}    {'H2bLb'}
```

```{note}
Chemical species from the Third Millennium database (Burcat) are indicated with the subscript `_M`. By default, the <tt>find_products.m</tt> function looks for species in the NASA database and does not consider ionized species. To search for species in Burcat's database, we have enabled the `flag_burcat` option, setting it to `true`. Alternatively, we can modify the default value in the <tt>Species.m</tt> file.
```

````

````{tab-item} Both and ionized species

```matlab
list_species = find_products(self, {'O', 'H'}, 'flag_burcat', true, , 'flag_ion', true)
```

which will yield the following output:


```matlab

list_species =

  1×52 cell array

  Columns 1 through 6

    {'HO2minus'}    {'H2Oplus'}    {'H3Oplus'}    {'OHplus'}    {'OHminus'}    {'HO2plus_M'}

  Columns 7 through 11

    {'HO2minus_M'}    {'HO3plus_M'}    {'HO3minus_M'}    {'H2O2plus_M'}    {'H2O3plus_M'}

  Columns 12 through 17

    {'H3O2plus_M'}    {'Oplus'}    {'Ominus'}    {'O2plus'}    {'O2minus'}    {'O3plus_M'}

  Columns 18 through 23

    {'O3minus_M'}    {'O4plus_M'}    {'O4minus_M'}    {'Hplus'}    {'Hminus'}    {'H2plus'}

  Columns 24 through 29

    {'H2minus'}    {'H2minus_M'}    {'H3plus_M'}    {'eminus'}    {'HO2'}    {'H2O'}

  Columns 30 through 36

    {'H2O2'}    {'OH'}    {'H2Obcrb'}    {'H2ObLb'}    {'H2O2bLb'}    {'OH_M'}    {'HO2_M'}

  Columns 37 through 43

    {'HO3_M'}    {'H2O2_M'}    {'H2O3_M'}    {'HOOOH_M'}    {'O'}    {'O2'}    {'O3'}

  Columns 44 through 51

    {'O2bLb'}    {'O3bLb'}    {'O_M'}    {'O2_M'}    {'O3_M'}    {'O4_M'}    {'H'}    {'H2'}

  Column 52

    {'H2bLb'}
```

```{note}
Chemical species from the Third Millennium database (Burcat) are indicated with the subscript `_M`. By default, the <tt>find_products.m</tt> function looks for species in the NASA database and does not consider ionized species. To search for species in Burcat's database and include ionized species, we have enabled the `flag_burcat` and `flag_ion` options, setting both to `true`. Alternatively, we can modify the default value in the <tt>Species.m</tt> file.
```

`````

```{tip}
The primary purpose of the <tt>find_products.m</tt> routine is to identify all potential chemical species within the database corresponding to a given set of input species. This is useful when we have a set of reactants and want to find all possible products after a chemical transformation.
```
