import matplotlib.pyplot as plt
import numpy as np
from day_5 import pop, life_exp
from day_4 import gdp_cap

"""
Day 6 learning provide x ticks using label and value for readable plot
and also double the population using numpy 
"""

pop = np.array(pop)
life_exp = np.array(life_exp)
gdp_cap = np.array(gdp_cap)
pop *= 2

plt.scatter(x=gdp_cap, y=life_exp, s=pop)

""" the customization """
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

plt.show()
