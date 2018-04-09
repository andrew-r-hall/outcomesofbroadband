import numpy as np
import pandas as pd
import zipcode as zip

#data = pd.read_csv('appendix-table-d.csv')

def gen_city_zip():
    zips = {}
    for i in range(99999):
        z = zip.isequal(format(i,'05d'))
        if z is not None:
            zips[z.city] = format(i,'05d')

    return(zips)
