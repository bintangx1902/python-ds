import numpy as np
from numba import njit, jit
import time

number = list(map(int, input().split()))
a, b = number


def calculate():
    big = a if a > b else b
    n = 0
    for i in range(1, big):
        if b % i == 0 and a % i == 0:
            n += 1
    return n


@jit(nopython=True)
def calculate_jit():
    big = a if a > b else b
    n = 0
    for i in range(1, big):
        if b % i == 0 and a % i == 0:
            n += 1
    return n


@njit(fastmath=True)
def calculate_njit():
    big = a if a > b else b
    n = 0
    for i in range(1, big):
        if b % i == 0 and a % i == 0:
            n += 1
    return n


start = time.time()
a = calculate()
print(a)
end = time.time()
print(f"time needed : {end - start}")

start = time.time()
a = calculate_jit()
print(a)
end = time.time()
print(f"time needed : {end - start}")

start = time.time()
a = calculate_njit()
print(a)
end = time.time()
print(f"time needed : {end - start}")
