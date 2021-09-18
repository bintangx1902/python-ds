import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import time


srt = time.time()
file = pd.read_csv('../datasets/netflix_data.csv')

frame = []
for fr in file:
    frame.append(fr)


frame_ = len(frame)


while frame_ != 0:
    frame_ -= 1
    var_name = frame[frame_]
    globals()[var_name]: list = []
    for dataset in file[frame[frame_]]:
        globals()[var_name].append(dataset)


durations = np.array(duration)
year = np.array(release_year)

col = []
for cc in durations:
    if cc // 2 == 0:
        col.append('black')
    elif 50 < cc < 100:
        col.append('green')
    elif 100 <= cc < 200:
        col.append('lime')
    elif cc > 300:
        col.append('gold')
    else:
        col.append('blue')

plt.scatter(year, durations, c=col)
plt.grid(True)

end = time.time()
plt.show()
print(f'Execution time is {end-srt}')
