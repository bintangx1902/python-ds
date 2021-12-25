l = [-3,-3,0,0]
n = 3


def sorter(l, n):
    new_list = []
    a1, a2, a3 = l[len(l) - 3], l[len(l) - 2], l[len(l) - 1]
    print(a1, a2, a3)
    for i in range(0, n):
        a1, a2, a3 = a2, a3, a1+a2+a3
        print(a3)
        new_list.append(a3)
    return new_list


print(sorter(l, n))
