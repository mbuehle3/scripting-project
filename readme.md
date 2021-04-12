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

Here is the website for installing [pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/index.html#getting-started) using either conda or pip.
Here is the website and instruction for installing [Basemap](https://anaconda.org/anaconda/basemap) with conda, and building from [source](https://matplotlib.org/basemap/users/installing.html).
When installing basemap from conda, there are many dependencies and it may take a while for conda to resolve the environment.

## Use

To load the module either put vertparse.py in your working directly or move your data to the data folder.
Importing the file is done using:

```[python]
import vertparse as vp
```

as vp is not necessary, but it saves some typing when calling functions.

To read in a dataset simply:

```[python]
data = 'path/to/your/data'
df = vp.read_VertData(data)
```

or if you don't want to save your data to an object

```[python]
df = vp.read_VertData('path/to/your/data')
```

To get a list of all availble functions in the VertParse module

```[python]
dir(vp)
```

The most useful function for parsing large datasets in VertParse is the .search_data() function.
This will allow you to search for a single keyword within a single column in the dataframe.
The funciton is really useful for sorting data by species, country, or state/province. 
To use it:

```[python]
specific_data = vp.search_data(df, 'column', 'keyword')
```

Once you are happy with your dataframe you can export it to a csv file using the write_VertData() function.

```[python]
vp.write_VertData(df)
```

If you want to coarsely visualize records with coordinate data you can pass a dataframe to the plot function.
Keep in mind that this function does not return an object

```[python]
vp.plot_VertData(df)
```

## Future Directions

In the future I am going to be expanding the output functionality to export a \LaTeX table formatted file.
Further, I am working on incoroporating an API so you can directly search VertNet using an API.
Finally, I want to include some more flexibility in the plotting function. 