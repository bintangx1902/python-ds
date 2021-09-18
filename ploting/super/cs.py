import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import time

srt = time.time()
file = pd.read_csv('../../datasets/netflix_data.csv')


frame = []
for frames in file:
    frame.append(frames)

frame_len = len(frame)

while frame_len != 0:  # 11
    frame_len -= 1  # 10 when the code is going to the bottom 'while ' will be checked again until 0 and its done
    varname = frame[frame_len]  # the tenth frame
    globals()[varname]: list = []  # tenth frame name as a list
    for dataset in file[frame[frame_len]]:  # for every data in frame[current len]
        globals()[varname].append(dataset)  # the frame name is becoming list using globals then we append the dataset

durations = np.array(duration)
year = np.array(release_year)
movies = np.array(mtype)

col = []
for mvs, lent in zip(movies, durations):

    if mvs == 'Movie' and lent != 0:
        if lent > 100:
            col.append('lime')
        elif lent == 0:
            col.append('pink')
        else:
            col.append('yellowgreen')
    else:
        col.append('black')


plt.scatter(durations, year, c=col)
plt.grid(True)
print(director)
end = time.time()
# plt.show()
print(f'Time needed to execute this code is {end - srt}')
