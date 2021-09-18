import requests
import pandas as pd
import numpy as np
from matplotlib import pyplot as p


"""
a = pure
"""


url = 'https://ncov-rest-api.000webhostapp.com/ketersediaan_rumah_sakit2.json'
raw = requests.get(url).json()
dataset = pd.json_normalize(raw)

rsName = []
rsCode = []
rsClass = []
rsPlace = []
rsHotLine = []
rsCapacity = []
rsAvailable = []

for a in dataset['data']:
    for zero in range(len(a)):
        rsName.append(a[zero]['faskes'])
        rsCode.append(a[zero]['kode_faskes'])
        rsClass.append(a[zero]['kelas_rs'])
        rsPlace.append(a[zero]['wilayah'])
        rsHotLine.append(a[zero]['nomor_hotline_spgdt'])
        rsCapacity.append(int(a[zero]['kapasitas_vip']) + int(a[zero]['kapasitas_kelas_1']) +
                          int(a[zero]['kapasitas_kelas_2']) + int(a[zero]['kapasitas_kelas_3']) +
                          int(a[zero]['kapasitas_hcu']) + int(a[zero]['kapasitas_iccu']) +
                          int(a[zero]['kapasitas_icu_negatif_ventilator']) +
                          int(a[zero]['kapasitas_icu_negatif_tanpa_ventilator']) +
                          int(a[zero]['kapasitas_icu_tanpa_negatif_ventilator']) +
                          int(a[zero]['kapasitas_icu_tanpa_negatif_tanpa_ventilator']) +
                          int(a[zero]['kapasitas_isolasi_negatif']) + int(a[zero]['kapasitas_isolasi_tanpa_negatif']) +
                          int(a[zero]['kapasitas_nicu_covid']) + int(a[zero]['kapasitas_perina_covid']) +
                          int(a[zero]['kapasitas_picu_covid']) + int(a[zero]['kapasitas_ok_covid']) +
                          int(a[zero]['kapasitas_hd_covid']) + int(a[zero]['kapasitas_hd_covid'])
                          )
        rsAvailable.append(int(a[zero]['kosong_vip']) + int(a[zero]['kosong_kelas_1']) + int(a[zero]['kosong_kelas_2']) +
                           int(a[zero]['kosong_kelas_3']) + int(a[zero]['kosong_hcu']) + int(a[zero]['kosong_iccu']) +
                           int(a[zero]['kosong_icu_negatif_ventilator']) +
                           int(a[zero]['kosong_icu_negatif_tanpa_ventilator']) +
                           int(a[zero]['kosong_icu_tanpa_negatif_ventilator']) +
                           int(a[zero]['kosong_icu_tanpa_negatif_tanpa_ventilator']) +
                           int(a[zero]['kosong_isolasi_negatif']) + int(a[zero]['kosong_isolasi_tanpa_negatif']) +
                           int(a[zero]['kosong_nicu_covid']) + int(a[zero]['kosong_perina_covid']) +
                           int(a[zero]['kosong_picu_covid']) + int(a[zero]['kosong_ok_covid']) +
                           int(a[zero]['kosong_hd_covid'])
                           )

xLen = []

for let in range(len(rsName)):
    xLen.append(let)

fig, ax = p.subplots()

scat1 = ax.scatter( rsAvailable, xLen, label='data')
ax.set_xticklabels(rsAvailable)
ax.set_yticklabels(rsName)
p.show()

