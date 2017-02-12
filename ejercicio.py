# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 09:47:35 2017

@author: Ioritz Goizueta
"""

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


# OBIS: http://www.iobis.org y leerla en un DataFrame de pandas
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


# MODIFICABLE
# Opciones de visualizacion de la especie
# Muchas mas en: http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot
map.plot(lon, lat, 'bo', markersize=7, markeredgecolor='none')

# INSTRUCCION
# Debeis guardar la figura a un archivo pdf
map.

# Se muestra el mapa por pantalla
plt.show()
