import math, numpy as np
from scipy.linalg import inv


""" provide radians """
rad = math.radians(12)
print(rad)

""" provide value of phi """
print(math.pi)


""" matrix """
mtr = [
    [1, 3],
    [8, 4]
]
""" using inv from scipy """
sc_inv = inv(mtr)
print(sc_inv)

""" using numpy """
np_inv = np.linalg.inv(mtr)
print(np_inv)

# or

np_inv = np.dot(mtr, inv(mtr))
print(np_inv)
