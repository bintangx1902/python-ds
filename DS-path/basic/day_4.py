import numpy as np
from data.learn_list import *


"""
day 3 learn
using the other list as slice indexing

positions = ['GK', 'M', 'A', 'D', ...]
heights = [191, 184, 185, 180, ...]
"""

height = np.array(height)
position = np.array(position)

gk_height = height[position == 'GK']
print(gk_height)

other = height[position != 'GK']
print(other)

"""
new section we learn about plot the data with matplotlib 
use plt.show() to show up the plot
"""

from matplotlib import pyplot as plt

plt.plot(year, population)
plt.show()

plt.plot(gdp_cap, life_exp)
plt.show()

"""
same data but we will use the scatter plot and use x-axis as logarithmic scale
"""

plt.scatter(gdp_cap, life_exp)
plt.xscale('log')
plt.show()
