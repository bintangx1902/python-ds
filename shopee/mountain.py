from itertools import groupby
from operator import itemgetter


case = int(input())

for x in range(case):
    n = int(input())
    arr = list(map(int, input().split()))

    """
    1st case
    assume n = 10
    arr =  [3 2 3 2 3 4 3 2 1 4]

    2nd case
    assume n = 10
    arr = [ 1 2 3 2 3 4 2 3 2 5 ] 

    3rd case
    assume n = 10
    arr = [ 10 9 8 7 6 5 4 3 2 1 ]
    """
    for idx, val in groupby(enumerate(arr), lambda m: m[0] - m[1]):
        print(list(map(itemgetter(1), val)))