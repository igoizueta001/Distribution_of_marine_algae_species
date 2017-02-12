# INSTRUCCION
# Es necesario instalar el paquete Basemap desde Anaconda Navigator
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# MODIFICABLE
# Debeis ajustar las coordenadas del mapa a la localizacion de la especie
# La ayuda esta en: http://matplotlib.org/basemap/api/basemap_api.html#module-mpl_toolkits.basemap
map = Basemap(projection='mill', resolution='l', llcrnrlon=-25, llcrnrlat=20, urcrnrlon=40, urcrnrlat=60)

# MODIFICABLE
# Opciones del mapa
# Muchas mas en: http://matplotlib.org/basemap/api/basemap_api.html#module-mpl_toolkits.basemap
map.drawcoastlines(linewidth=0.5)
map.drawcountries(linewidth=0.5)
map.fillcontinents(alpha=0.5)
map.drawmapboundary()
map.drawmeridians(np.arange(0, 360, 30), labels=[False, False, False, True], linewidth=0.1)
map.drawparallels(np.arange(-90, 90, 30), labels=[False, True, False, False], linewidth=0.1)

# INSTRUCCION
# Debeis descargaros un fichero csv con un conjunto de registros (records) de una especie
# desde la pagina del OBIS: http://www.iobis.org y leerla en un DataFrame de pandas
# Ese DataFrame se debe llamar specie
specie =

# Datos de latitud y longitud de la especie
lon, lat = map(list(specie['longitude']), list(specie['latitude']))

# MODIFICABLE
# Opciones de visualizacion de la especie
# Muchas mas en: http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot
map.plot(lon, lat, 'bo', markersize=7, markeredgecolor='none')

# INSTRUCCION
# Debeis guardar la figura a un archivo pdf
map.

# Se muestra el mapa por pantalla
plt.show()
