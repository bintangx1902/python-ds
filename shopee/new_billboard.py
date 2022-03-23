def print_num(set1, set2):
    print(sum(set1)) if sum(set1) == sum(set2) else 0


def find_set(arr, n, set1, set2, sum1, sum2, pos):
    if (pos == n):
        if (sum1 == sum2):
            print_num(set1, set2)
            return True
        else:
            return False

    set1.append(arr[pos])

    res = find_set(arr, n, set1, set2,
                   sum1 + arr[pos], sum2, pos + 1)

    if res:
        return res

    # If not then backtrack by removing current
    # element from set1 and include it in set 2.
    set1.pop()
    set2.append(arr[pos])

    # Recursive call after including current
    # element to set 2 and removing the element
    # from set 2 if it returns False
    res = find_set(arr, n, set1, set2, sum1,
                   sum2 + arr[pos], pos + 1)

    set2.pop() if not res else res


def is_partition(arr, n):
    sums = 0

    for i in range(0, n):
        sums += arr[i]

    if (sums % 2 != 0):
        return False

    set1 = []
    set2 = []

    return find_set(arr, n, set1, set2, 0, 0, 0)


# Driver code
n = int(input())
arr = list(map(int, input().split()))

is_partition(arr, n)
