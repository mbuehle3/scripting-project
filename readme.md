# VertParse Module

## Introdution

This python module is meant to help with processing local VertNet dataframes using python.
Currently, there are 174 columns in a VertNet dataframe, making it challenging to parse the data in programs like excel or Libreoffice.
For most records (extant reptile records at least) the majority of the 174 columns are not populated with data e.g. (earliestageorloweststage
or earliesteraorlowesterathem).
However, one of the challenges that VertNet faces in compiling data from natural history museums around the world, is that there is no standard museum catalog database.
As a result, there are data stored in separate fields that are the same thing.
To circumnvent this, VertNet has columns that are often redundant or concatenate together data from other columns (e.g. - scientificname is a concatenation of the genus and specificepithet columns).

## Dependencies

VertNet relies on pandas and Basemap.
Both can be installed using conda install or pip.

Website for installing [pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/index.html#getting-started)
Website and instruction for installing [Basemap](https://anaconda.org/anaconda/basemap) with conda, and building from [source](https://matplotlib.org/basemap/users/installing.html).
When installing from conda, there are many dependencies and it may take a while for conda to resolve the environment.
