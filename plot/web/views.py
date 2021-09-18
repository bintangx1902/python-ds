from django.shortcuts import render
import pandas as pd
import numpy as np
from matplotlib import pyplot as p
import matplotlib.pyplot as plt
import requests
from io import StringIO


def graph():

    def high_check(fnum, snum):
        if snum > fnum:
            return snum
        return fnum

    url = 'https://services5.arcgis.com/VS6HdKS0VfIhv8Ct/arcgis/rest/services/COVID19_Indonesia_per_Provinsi/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json'
    raw = requests.get(url).json()
    dataset = pd.json_normalize(raw)

    features = dataset['features']

    save_list = []
    prov_list = []
    pos_list = []

    for ftr in features:
        data = pd.DataFrame(ftr).to_dict()
        attr = data['attributes']
        for ids in attr:
            save = attr[ids]['Kasus_Semb']
            prov = attr[ids]['Provinsi']
            pos = attr[ids]['Kasus_Posi']

            pos_list.append(pos)
            prov_list.append(prov)
            save_list.append(save)

    save_list = np.array(save_list)
    pos_list = np.array(pos_list)

    x = np.arange(len(prov_list))
    width = 0.35

    fig, ax = p.subplots()

    bar1 = ax.bar(x - width / 2, save_list, width, label='Kasus Sembuh')
    bar2 = ax.bar(x + width / 2, pos_list, width, label='Kasus Positif')

    ax.set_ylabel('Jumlah Kasus')
    ax.set_title('Visualisasi data corona')
    ax.set_xticks(x)
    ax.set_xticklabels(prov_list, rotation=90)
    ax.legend()

    ax.bar_label(bar1, padding=3, rotation=45*2)
    ax.bar_label(bar2, padding=3, rotation=45*2)

    sl = np.array(save_list.copy()).tolist()
    pl = np.array(pos_list.copy()).tolist()
    sl.sort(reverse=False)
    pl.sort(reverse=False)
    yAxis = high_check(sl[-1], pl[-1])
    yAxis += 50000

    p.axis([-1, len(prov_list) + 1, 0, yAxis])

    fig.set_figheight(10)
    fig.set_figwidth(18)

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data


def home(request):
    context = {
        'graph': graph(),
    }
    return render(request, 'dash.html', context)
