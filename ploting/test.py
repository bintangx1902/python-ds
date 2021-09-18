from numba import njit, jit
import numpy as np
import time

x = np.arange(100).reshape(10, 10)


@njit(fastmath=True, parallel=True)
def n_jitter():
    len1 = np.random.randint(100, 1000, 2000)
    res = []
    for i in len1:
        i *= 133
        res.append(i)
    return res


@jit(nopython=True)
def jitter():
    len1 = np.random.randint(100, 1000, 2000)
    res = []
    for i in len1:
        i *= 133
        res.append(i)
    return res


start = time.time()
n_jitter()
end = time.time()
print(f'time taken {(end-start)}')

start = time.time()
jitter()
end = time.time()
print(f'time taken {(end-start)}')
