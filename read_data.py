# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
import rasterio
from matplotlib import pyplot as plt
# %matplotlib inline

# %%
dataset = rasterio.open('test/RAD_NL25_RAC_RT_1340.h5')

plt.imshow(dataset.read(1), cmap='pink')
plt.show()
