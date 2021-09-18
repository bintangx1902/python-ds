import pandas as pd
from matplotlib import pyplot as p
import requests
import numpy as np

raw = requests.get('https://apiroom.pythonanywhere.com/api/room?format=json').json()
# raw = requests.get('https://apiroom.pythonanywhere.com/api/s-room?format=json').json()
# raw = requests.get('https://apiroom.pythonanywhere.com/api/icu?format=json').json()
data = pd.json_normalize(raw)
df = pd.DataFrame(data)

x_label, xRaw = df['id'].to_list(), df['id'].to_list()
y_label, yRaw = df['total_bed'].to_list(), df['total_bed'].to_list()
z_label, zRaw = df['bed_left'].to_list(), df['bed_left'].to_list()


def bb_sort(arr):
    swapped = True
    iterations = 0

    while swapped:
        swapped = False
        for raw_arr in range(len(arr) - iterations - 1):
            if arr[raw_arr] > arr[raw_arr+1]:
                # do swap
                arr[raw_arr], arr[raw_arr+1] = arr[raw_arr+1], arr[raw_arr]
                swapped = True
        iterations += 1
    return arr


def high_check(fnum, snum):
    if fnum > snum:
        return fnum
    return snum


xLen = len(x_label)+1
# checking y
yLen = len(y_label)-1
yMax = bb_sort(y_label)[yLen]
# checking z
zLen = len(z_label)-1
zMax = bb_sort(z_label)[zLen]
# v max point checking
vMax = high_check(yMax, zMax)
vMax += 200

fig = p.figure()
ax = fig.add_subplot(111)

p.axis([0, xLen, 0, vMax])

p.plot(xRaw, yRaw, 'bo--')
for nm in zip(xRaw, yRaw):
    ax.annotate('(%s, %s)' % nm, xy=nm, textcoords='data')

p.bar(xRaw, zRaw, color='green')
for br in zip(xRaw, zRaw):
    ax.annotate('(%s, %s)' % br, xy=br, textcoords='data')

p.legend(['total bed', 'bed left'])

p.grid()
p.show()
