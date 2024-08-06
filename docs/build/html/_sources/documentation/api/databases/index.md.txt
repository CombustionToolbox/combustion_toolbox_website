# Databases

Combustion Toolbox generates its own databases using an up-to-date version of NASA's 9-coefficient polynomial fits {cite:p}`Mcbride2002`. This information is stored in the `Database` abstract class. Three main databases are used in the code:
- `NasaDatabase`: contains data extracted from NASA's database {cite:p}`Mcbride2002`.
- `BurcatDatabase`: extracts data from the Third Millennium database {cite:p}`burcat2005`.
- `SolarAbundances`: stores the solar abundances of the elements {cite:p}`asplund2009`.

## Database

```{eval-rst}
.. currentmodule:: src.+combustiontoolbox.+databases

.. automodule:: src.+combustiontoolbox.+databases.@Database
   :show-inheritance:
   :members:
```

## NasaDatabase

```{eval-rst}
.. currentmodule:: src.+combustiontoolbox.+databases

.. automodule:: src.+combustiontoolbox.+databases.@NasaDatabase
   :show-inheritance:
   :members:
```

## BurcatDatabase

```{eval-rst}
.. currentmodule:: src.+combustiontoolbox.+databases

.. automodule:: src.+combustiontoolbox.+databases.@BurcatDatabase
   :show-inheritance:
   :members:
```

## SolarAbundances

```{eval-rst}
.. currentmodule:: src.+combustiontoolbox.+databases

.. automodule:: src.+combustiontoolbox.+databases.@SolarAbundances
   :show-inheritance:
   :members:
```