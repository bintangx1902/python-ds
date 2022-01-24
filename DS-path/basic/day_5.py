from matplotlib import pyplot as plt
from data.learn_list import *

"""
day 5 learning about scatter plot
"""

plt.scatter(pop, life_exp)
plt.show()

"""
new section i provide a histogram plot on life_exp
and im gonna test with 5 bins and 20 bins
"""

plt.hist(life_exp)
plt.show()

""" 5 bins """
plt.hist(life_exp, bins=5)
plt.show()
plt.clf()

""" 20 bins """
plt.hist(life_exp, bins=20)
plt.show()
plt.clf()

""" 15 bins comparing the life_exp and life_exp 1950 """
plt.hist(life_exp, bins=15)
plt.show()
plt.clf()

plt.hist(life_exp_50, bins=15)
plt.show()
plt.clf()

""" plot customization """
plt.scatter(gdp_cap, life_exp)
plt.xscale('log')

""" 
use of labels 
use customization before show the plot
"""
xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
title = 'World Development in 2007'

plt.xlabel(xlab)
plt.ylabel(ylab)
plt.title(title)

plt.show()
