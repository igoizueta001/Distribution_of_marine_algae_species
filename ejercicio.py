# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 09:47:35 2017

@author: Ioritz Goizueta
"""
#Brief explanation of the aim of this work:
    #We have been asked to represent a distribution map of a marine living organism using this software.
    #I have chosen two algae species: Cystoseira tamariscifolia and Saccorhiza ployschides.
    #The chosen species are seen to live together forming "asociations" along the North Atlantic Ocean and Mediterranean sea.
    #Thus, based on the occurrence data of the distribution of each species, this work aims to put together data of both species and check wheter their distribution overlaps or not.
    #This way, it will be seen in a simple way if one species need the other to appear in a place or they appear together due to the addequate environmental conditions of those habitats.

#Importing packages
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


#Adjusting map coordenates based on the species occurrence points (Saccorhiza polyschides, Cystoseira tamariscifolia) ustar las coordenadas del mapa a la localizacion de la especie
map = Basemap(projection='mill', resolution='l', llcrnrlon=-20, llcrnrlat=25, urcrnrlon=20, urcrnrlat=70)

# Setting and modifyng the map
# Much more at: http://matplotlib.org/basemap/api/basemap_api.html#module-mpl_toolkits.basemap
map.drawcoastlines(linewidth=0.5)
map.drawcountries(linewidth=0.5)
map.fillcontinents(color='0.9', alpha=0.5)
map.drawmapboundary()
map.drawmeridians(np.arange(0, 360, 30), labels=[True, True, True, True], linewidth=0.1)
map.drawparallels(np.arange(-90, 90, 30), labels=[True, True, True, True], linewidth=0.1)


# OBIS: http://www.iobis.org
#Importing Cystoseira's data
specieC = pd. read_table('proccessed_Cystoseira.txt' , sep=';' ,
                       header=0, na_values=' ')
print(specieC)
#Setting the coordenates of Cystoseira's distribution
lonC, latC = map(list(specieC['longitude']), list(specieC['latitude']))

#Importing Saccorhiza's data
specieS = pd. read_table('proccessed_Saccorhiza.txt' , sep=';' ,
                       header=0, na_values=' ')
print(specieS)
#Setting the coordenates of Saccorhiza's distribution
lonS, latS = map(list(specieS['longitude']), list(specieS['latitude']))


#Putting all together in a single map and saving it to a pdf
plt.figure()
map.drawcoastlines(linewidth=0.5)
map.drawcountries(linewidth=0.5)
map.fillcontinents(color='0.9', alpha=0.5)
map.drawmapboundary()
map.drawmeridians(np.arange(0, 360, 30), labels=[True, True, False, True], linewidth=0.1)
map.drawparallels(np.arange(-90, 90, 30), labels=[True, False, True, True], linewidth=0.1)
map.plot(lonS, latS, 'go', markersize=3, markeredgecolor='none', label='Saccorhiza polyschides')
map.plot(lonC, latC, 'c^', markersize=2.5, markeredgecolor='none', label='Cystoseira tamariscifolia')
plt.title('Distribution map\nMarine algae')
plt.legend(loc='lower right', fontsize='small')
plt.savefig("distribution_map.pdf")
