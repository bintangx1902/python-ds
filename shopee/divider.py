raw = list(map(int, input().split()))
value_set = list(map(int, input().split()))

"""
n = 4
1-3
2-2
3-1
"""


def calculate():
    n, k = raw
    lim = n + 1

    number = []
    for zz in range(n - 1):
        a = sum(value_set[0: zz + 1]) * len(value_set[0: zz + 1])
        b = sum(value_set[zz + 1: lim]) * len(value_set[zz + 1: lim])
        number.append((a + b))

    number.sort()
    return number[0]


def calc_speed():
    n, k = raw
    number = 0
    lim = n + 1

    for zz in range(n - 1):
        a = sum(value_set[0: zz + 1]) * len(value_set[0:zz + 1])
        b = sum(value_set[zz + 1: lim]) * len(value_set[zz + 1:lim])
        if not number:
            number = a + b
        else:
            if not number < (a + b):
                number = a + b

    return number


print(calc_speed())
