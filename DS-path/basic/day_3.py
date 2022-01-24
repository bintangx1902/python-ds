import numpy as np
from data.learn_list import *

"""
Day 3 Learning 2d numpy array 
in the baseball list, first col-> height
second -> weight.

uncomment the print if want to check out the result
how to print the ndarray with commas for separate the value?
print(repr(var_name))

"""

# 3 col inside
baseball = np.array(baseball)
# print(baseball.shape)

""" 50th row """
print(baseball[49, :])

""" weight and height """
baseball_weight = baseball[:, 1]
baseball_height = baseball[:, 0]
# print(baseball_weight)
# print(baseball_height)


"""
the baseball list is [height, weight, bmi] 
we will convert height from inches to metres by multiply the number with 0.0254,
weight from lb to kg -> multiply the number with 0.453592, and BMI score is same 
"""

# convert array
convert = np.array([.0254, .453592, 1])

baseball_converted = baseball * convert
# print(baseball_converted)


"""
new section.
the value positioning is same like the first one, but in this new section,
the list is set to scientific number, and we gonna find the mean and median 
"""

baseball = np.array(baseball_)

# get the specific data like height
height = baseball[:, 0]
mean = np.mean(height)
median = np.median(height)

"""
new section
the baseball set like first
we gonna find standard derivation and correlation between height and weight
"""

baseball = np.array(baseball_float)

stddev = np.std(baseball[:, 0])
corr = np.corrcoef(baseball[:, 0], baseball[:, 1])
print(f"standard derivation : {stddev}")
print(f"correlation : {repr(corr)}")


