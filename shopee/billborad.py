
"""
assume n=4
arr = [ 1 2 3 6]
make an arr
1 | 2 3 6 == 1 - 11/3 (1 - 3)
1 2 | 3 6 == 1.5 - 4.6 (2 - 2)
1 2 3 | 6 == 6 - 6 (3 - 1)


assume n = 5
arr = [ 1 3 2 2 2 ]
1 | 3 2 2 2 == 1 - 9/4 ( 1 - 4 )
1 3 | 2 2 2 == 2 - 5/3 (2 - 3)
1 3 2 | 2 2 == 2 - 2  (3 - 2)


get the same number
store the number data
break the looping

"""

"""
0
1
2
3
4
"""

n = int(input())
arr = list(map(int, input().split()))


def calculate():
    # num = 0
    lim = n + 1
    # unk = 1
    for x in range(1, n):
        a = sum(arr[0:x])
        b = sum(arr[x: lim])
        if a == b:
            return a

    return 0


print(calculate())
