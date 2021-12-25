import requests
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import time

start = time.time()
raw = requests.get('https://services5.arcgis.com/VS6HdKS0VfIhv8Ct/arcgis/rest/services/COVID19_Indonesia_per_Provinsi'
                   '/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json').json()
datasets = pd.json_normalize(raw)
features = datasets['features']

# get the header
head_list = []
for dt in features:
    for head in dt:
        for header in head['attributes']:
            head_list.append(header)

head_list = list(set(head_list))
len_list = len(head_list)

while len_list != 0:
    len_list -= 1
    var_name = head_list[len_list]
    globals()[var_name]: list = []

    for feature in features:
        dataset = pd.DataFrame(feature).to_dict()
        data = dataset['attributes']
        for index in range(0, len(data)-1):
            # print(data[index][var_name])
            globals()[var_name].append(data[index][var_name])


plt.scatter(Provinsi, Kasus_Posi)
plt.grid(True)


end = time.time()
print(f"\n times need : {end - start}")
plt.show()
