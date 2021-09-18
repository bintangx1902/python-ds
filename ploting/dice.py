import numpy as np
from matplotlib import pyplot as plt
import time


srt = time.time()
all_walk = []

for i in range(100):
    random_walk = [0]

    for x in range(1000):
        step = random_walk[-1]
        dice = np.random.randint(1, 7)

        if dice <= 2:
            step -= 1
        elif dice <= 5:
            step += 1
        else:
            step += np.random.randint(1, 7)

        if np.random.rand() < 0.001:
            step = 0

        random_walk.append(step)

    all_walk.append(random_walk)

aw = np.array(all_walk)
awt = aw.transpose()

plt.clf()
plt.plot(awt)
end = time.time()
plt.show()
print(f"Time To Execute this code is {end-srt}")
plt.show()
