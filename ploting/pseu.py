from time import sleep
n = 15
m = 10

for i in range(2, 6):
    print(f"i is : {i}")
    j = i
    while j <= 3:
        print(f"j is : {j}")
        k = j
        while True:
            print(f"k is : {k}")
            n += m
            print(n)
            k += 1
            if k > 3:
                break
        j += 1


print(f"final n is : {n}")
