raw = list(map(int, input().split()))
values_set = list(map(int, input().split()))

"""
case 1

3 3
1 3 4

1 - 3 - 4 === 3,1
1,3 - 3,4 === 2,2
1,3,4 === 1,3

find avg = 1 3 4 3.5 2.67
output total n in avg >= 3
3 4 3.5
3


case 2
6 3

1 1 4 5 1 4

1 1 4 5 1 4 === 6, 1 = 0
1,1 - 1,4 - 4,5 - 5,1 - 1,4 === 5,2 =1 
1,1,4 - 1,4,5 - 4,5,1 - 5,1,4 === 4,3 =2
1,1,4,5 -  1,4,5,1 - 4,5,1,4 === 3,4 =3
1,1,4,5,1 - 1,4,5,1,4 === 2,5 =4
1,1,4,5,1,4 === 1,6 =5

4 - 5 - 4 ==3
4.5 - 3 == 2
3.3 - 3.3 - 3.3 ===3
4.67 
3

output = 10
"""
import time


def calculate():
    count = 0
    if raw[0] == len(values_set):
        n, k = raw
        lim = n + 1
        dun = 1
        for x in range(n):
            # assume x = 0
            if x == 0:
                for idx, val in enumerate(values_set):
                    if val >= k:
                        count += 1
            # x >=1
            dun += 1
            for dumb in range(lim - dun):
                count += 1 if sum(values_set[dumb: dumb + dun]) / len(values_set[dumb: dumb + dun]) >= k else 0

    return count


start = time.time()
print(calculate())
end = time.time()
print(f"time needed : {end - start}")
