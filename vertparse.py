import sys
import csv
import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

def read_VertData(n):
    """
    Import a local VertNet formatted csv file. 
    """
    original_stdout = sys.stdout
    with open(n, 'r') as VertNetFile:
        input_parsed = pd.read_csv(VertNetFile, delimiter = '\t')
        return input_parsed
        # for record in input_parsed:
        #     # print(record)
        #     record_list.append(record)
def clean_VertData(VertDf):
    """
    Remove empty columns from the dataset and print to a smaller file.
    Returns a provided VertObject where columns with no data have been removed from the dataset. 
    Overwrites the object initially created using the read_VertData() function
    """
    data = VertDf.dropna(how='all', axis = 1 , inplace=False)
    return data

def write_VertData(VertDf,filename = 'output.txt'):
    """
    Write the pandas dataframe to an external file. 
    Useful for exporting cleaned datafiles for easier file manipulation in excel or libreoffice
    """
    # print(sys.argvs[2])
    VertDf.to_csv(filename, header = True, index = False)
   
def get_coord(VertDf):
    """
    Extract the coordinates for each record
    """
    coord = VertDf[['decimallatitude', 'decimallongitude','country']]
    return coord

def get_species(VertDf):
    """
    Returns a tuple with a list of species in VertDf, and the number of each species.
    """    
    species = VertDf['scientificname']
    species_num = species.value_counts()
    return species, species_num

def search_data(Vertdf,column ,keyword):
    """
    Search a specific column for a provided keyword.
    The returned object will contain only records that match the keyword provided
    
    """
    genus = Vertdf.loc[Vertdf[column] == keyword]

    return genus


def get_catalog(VertDf):
    """
    Extract the institution code and catalog number from a provided dataframe
    
    """

    catalog = VertDf[['institutioncode','catalognumber']]
    museum_num = catalog.iloc[:,0].value_counts()
    return catalog, museum_num

def plot_VertData(VertDf, zoomscale=3):
    """
    Plot a data frame using a blue circle on a world map.
    Zoomscale can be changed to zoom in more    
    """

    coord = get_coord(VertDf)
    zoom_scale = zoomscale
    bbox = [coord.iloc[:,0].max()+zoom_scale,coord.iloc[:,0].min()-zoom_scale,coord.iloc[:,1].max()+zoom_scale, coord.iloc[:,1].min()-zoom_scale]
    lons = coord.iloc[:,1]
    lats = coord.iloc[:,0]
    m = Basemap(llcrnrlat=bbox[1],urcrnrlat=bbox[0],llcrnrlon=bbox[3],urcrnrlon=bbox[2],lat_ts=10,resolution='i')
    m
    m.drawcountries(linewidth = 0.75)
    m.drawcoastlines(linewidth = 0.75)
    m.plot(lons,lats, 'bo', markersize = 5)
    plt.show()
    
def missing_coord(VertDf):
    """
    Calculate how many records are missing coordinate data
    
    """

    coord = get_coord(VertDf)
    miss = coord.iloc[:,1].isna().value_counts()
    total = len(VertDf)
    return miss, total

def get_countries(VertDf):
    """
    Extract countries from a dataframe
    
    """

    country = VertDf[['country']]
    country_count = country.value_counts()
    return country, country_count

def essential_data(VertDf,*argv):
    """
    Subsample user-defined columns in the dataframe.
    argv can be passed as a list (list = ['item1', 'item2])
    
    """

    essential = pd.DataFrame()
    for arg in argv:
        essential[arg] = VertDf[arg]

    return essential

def basic_data(VertDf):
    """
    Export a handful of columns that are generally useful for tables, and contain the most information
    
    """

    list = ['institutioncode','catalognumber','scientificname','country','decimallatitude', 'decimallongitude']
    basic = pd.DataFrame()
    for item in list:
        basic[item] = VertDf[item]

    return basic

# def tex_table(VertDf):
    



if __name__ == '__main__':
    pass