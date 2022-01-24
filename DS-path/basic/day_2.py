import numpy as np
from data.learn_list import *

""" 

day 2 record
learning about numpy arrays, in this case we learn about ndarray.
calculating data inside a list using standard mode and numpy calc
uncomment the print if u want to see the result

"""

# both list has a same length

""" standard lb to kg """
weight_kg = [x * .453592 for x in weight_lb]
height_m = [x * .0254 for x in height_in]
bmi = [weight_kg[x] / height_m[x] ** 2 for x in range(len(weight_lb) - 1)]

# print(f"{weight_kg} \n{height_m} \n{bmi}")

""" numpy is simple """
weight_kg = np.array(weight_lb) * .453592
height_m = np.array(height_in) * .0254
bmi = weight_kg / height_m ** 2
""" you can slice the numpy arrays like this """
sliced = bmi[100:111]

# print(f"{weight_kg} \n{height_m} \n{bmi}")

""" this provide how to filter the bmi score below 21 """
lite = bmi < 21
print(bmi[lite])

""" addition section """
a = list(range(2, 23)) + [False, True, False]
b = list(range(50, 71)) + [True, True, False]

""" standard -> you must iter 1 by 1 index """
c = [a[x] + b[x] for x in range(len(a))]
# print(c)

""" numpy logic is just like standard addition """
c = np.array(a) + np.array(b)
# print(c)
