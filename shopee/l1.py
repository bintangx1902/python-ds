import numpy

""""
common fact

a = 10
b = 15
"""

factor_list = []

number = list(map(int, input().split()))
a, b = number[0], number[1]

a_factor = []
for i in range(1, a+1):
    if a % i == 0:
        a_factor.append(i)

b_factor = []
for i in range(1, b+1):
    if b % i == 0:
        b_factor.append(i)

big = a_factor if a > b else b_factor
less = a_factor if a < b else b_factor

for index, val in enumerate(less):
    if val in big:
        factor_list.append(val)

print(factor_list)
print(len(factor_list))
