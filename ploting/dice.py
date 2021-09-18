import numpy as np
from matplotlib import pyplot as plt
import time


srt = time.time()
walks = [0]

for x in range(100):
    dice = np.random.randint(1, 7)
    step = walks[-1]

    if dice <= 2:
        step = max(0, step-1)
    elif dice <= 5:
        step += 1
    else:
        step += np.random.randint(1, 7)

    walks.append(step)


plt.plot(walks)
end = time.time()

print(f"Time To Execute this code is {end-srt}")
plt.show()
