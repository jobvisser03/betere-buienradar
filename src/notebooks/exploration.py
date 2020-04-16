#%%
from matplotlib import pyplot as plt
import pandas as pd
import netCDF4

from IPython import InteractiveShell 
InteractiveShell.ast_node_interactivity = 'all'
import os 
os.chdir('.')
#%%
# url='ftp://data.knmi.nl/download/Actuele10mindataKNMIstations/1/noversion/2020/04/16/KMDS__OPER_P___10M_OBS_L2_0000.nc'
url='../../data/KMDS__OPER_P___10M_OBS_L2_0020.nc'
vname = 'ta' #Air Temperature 1 Min Average
station = 1
nc = netCDF4.Dataset(url)
times = nc.variables['time']
h = nc.variables[vname]
jd = netCDF4.num2date(times[:],times.units)
jd

# %%
hs = pd.Series(h[:,station],index=jd)

# %%
nc.dimensions
# h[:,]

# %%
times[:]
times.units

# %% 

# %%
