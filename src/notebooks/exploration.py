#%%
from matplotlib import pyplot as plt
import pandas as pd
import netCDF4

from IPython import InteractiveShell 
InteractiveShell.ast_node_interactivity = 'all

#%%


url='http://geoport-dev.whoi.edu/thredds/dodsC/HUDSON_SVALLEY/5951adc-a1h.nc'
vname = 'Tx_1211'
station = 0
nc = netCDF4.Dataset(url)
times = nc.variables['time']
h = nc.variables[vname]
jd = netCDF4.num2date(times[:],times.units)

