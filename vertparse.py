# To start, we are going to work on local vertnet files that have been downloaded. 
# Once that is figured out then I will move to figuring out how to access VertNet via an API

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

def write_VertData(VertDf):
    """
    Write the pandas dataframe to an external file. 
    Useful for exporting cleaned datafiles for easier file manipulation in excel or libreoffice
    """
    # print(sys.argvs[2])
    VertDf.to_csv('output.txt', header = True, index = False)
   
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

def get_genus(Vertdf,column ,genus):
    '''
    '''
    genus = Vertdf.loc[Vertdf[column] == genus]

    return genus


def get_catalog(VertDf):
    catalog = VertDf[['institutioncode','catalognumber']]
    museum_num = catalog.iloc[:,0].value_counts()
    return catalog, museum_num

def plot_VertData(VertDf, zoomscale=3):
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
    coord = get_coord(VertDf)
    miss = coord.iloc[:,1].isna().value_counts()
    total = len(VertDf)
    return miss, total

def get_countries(VertDf):
    country = VertDf[['country']]
    return country

def essential_data(VertDf,*argv):
    essential = pd.DataFrame()
    for arg in argv:
        essential[arg] = VertDf[arg]

    return essential

def basic_data(VertDf):
    list = ['institutioncode','catalognumber','scientificname','country','decimallatitude', 'decimallongitude']
    basic = pd.DataFrame()
    for item in list:
        basic[item] = VertDf[item]

    return basic

# def tex_table(VertDf):
    



if __name__ == '__main__':
    pass