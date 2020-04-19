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
import datetime
import ftplib
from pathlib import Path
import pandas as pd

# %%
now = datetime.datetime.utcnow()
today = now.strftime("%Y/%m/%d")
ftp_path = f'/download/nl_rdr_data_rtcor_5m/1.0/noversion/{today}'
data_dir = Path("data")

ftp = ftplib.FTP("data.knmi.nl") 
ftp.login() 
ftp.cwd(ftp_path)
ftp_files = ftp.nlst()
filename = sorted(ftp_files)[-1]
download_path = (data_dir/filename)
ftp.retrbinary("RETR " + filename, open(download_path,"wb").write)
ftp.quit()

# %%
t = pd.HDFStore("data/RAD_NL25_RAC_RT_1855.h5",'r')

# %%
list(t.walk())

# %%
# !pip install h5py

# %%
import h5py

h5 = h5py.File("data/RAD_NL25_RAC_RT_1855.h5",'r')

# %%
g = h5["image1/image_data"]
