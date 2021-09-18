import requests
from matplotlib import pyplot as p
import pandas as pd
import numpy as np

raw = requests.get('https://services5.arcgis.com/VS6HdKS0VfIhv8Ct/arcgis/rest/services/COVID19_Indonesia_per_Provinsi'
                   '/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json').json()
dataset = pd.json_normalize(raw)
ftr = dataset['features']

save_list = []
fid_list = []
pos_list = []


for data in ftr:
    pure = pd.DataFrame(data).to_dict()
    datas = pure['attributes']
    for ids in range(0, len(datas)-1):
        fid = np.array(datas[ids]['FID']).tolist()
        pos = np.array((datas[ids]['Kasus_Posi'])).tolist()
        save = np.array(datas[ids]['Kasus_Semb']).tolist()

        fid_list.append(fid)
        pos_list.append(pos)
        save_list.append(save)


pl = pos_list.copy()
fl = fid_list.copy()
sl = save_list.copy()

"""
Checking High Num
"""


def hnum(fnum, snum):
    if fnum > snum:
        return fnum
    return snum


"""
Part of Axis
"""

xAxis = len(fid_list)+1
sl.sort(reverse=False)
yMax = sl[-1]
pl.sort(reverse=False)
zMax = pl[-1]
hAxis = hnum(yMax, zMax)
hAxis += 10000

p.axis([0, xAxis, 0, hAxis])


"""
displaying data
"""
p.plot(fid_list, save_list, 'bo')
p.bar(fid_list, pos_list, color='red')

p.grid()
p.show()
