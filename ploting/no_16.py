col_data = []


def append_data(name, point):
    key = ("name", "point")
    value = (name, point)
    dict_data = dict(zip(key, value))
    col_data.append(dict_data)


with open('number/16.txt', 'r') as f:
    data = f.read().splitlines()

for d in data:
    raw = d.split()
    name = raw[0]
    point = [int(x) for x in raw[1:]]
    append_data(name, point)


def point(point_1, point_2):
    first = point_1[0]*3 + point_1[2]*1 - point_1[1]*0
    second = point_1[0]*3 + point_1[2]*1 - point_1[1]*0
    if first > second:
        return True
    elif first == second:
        goal_1 = point_1[-2] - point_1[-1]
        goal_2 = point_2[-2] - point_2[-1]
        if goal_1 > goal_2:
            return True
    return False


def sort_data(arr):
    n = len(col_data)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            a = arr[j]['point']
            b = arr[j+1]['point']
            if point(a, b):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


print("real data is :")
for x in col_data:
    print(x)

sort_data(col_data)
print("sorterd data is :")
for x in reversed(col_data):
    print(x)

# def sorting(col_data):
#     col_data.sort(
#         key=lambda e: (e['point'][0] * 3 + 1 * e['point'][2] - 0 * e['point'][1]) and e['point'][-2] - e['point'][-1])


# def selisih_gol() :
#     global col_data
#     col_data.sort(key=lambda goal:goal['point'][-2] - goal['point'][-1])
# def league_winner1():
#     for x in reversed(sorting()):
#         point = sum(x['point']) - x['point'][2] - x['point'][4]
#         return x['name']

# #get the fuckin data in point
# def points(point):
#     if point[-2] > point[-1]:
#         return True
#     return False

#
# def bbs():
#     n = len(col_data)
#
#     # Traverse through all array elements
#     for i in range(n - 1):
#         # range(n) also work but outer loop will repeat one time more than needed.
#
#         # Last i elements are already in place
#         for j in range(0, n - i - 1):
#
#             # traverse the array from 0 to n-i-1
#             # Swap if the element found is greater
#             # than the next element
#
#             """ [. . . .6] > [. . . . .3] """
#             if col_data[j] > col_data[j + 1]:
#                 col_data[j], col_data[j + 1] = col_data[j + 1], col_data[j]


# def league_winner2():
#    league = [x['name'] for x in reversed(sorting())]
#    for x in league :
#        print(x)
#    for x in reversed(sorting()) :
#        if x
#        print(x)
# global col_data

# jazz = []

# #assume n = 7
#  for fuck in reversed(sorting()):
#     n = len(sorting())
#     nx = len(fuck['point'])
#     for i in range(0, nx-1):
#         for j in range(0, nx-i-1):
#             if fuck['point'][j] > fuck['point'][j+1]:
#                 pass

# for fuck in reversed(sorting()):
# league = [x['name'] for x in reversed(sorting())]
# return league

#
# def search():
#     global col_data
#     x = 50
#     for li in col_data:
#         point = 3 * li['point'][0] + li['point'][2] * 1
#         print(point)
#         if point <= x:
#             print(f"{li} - total point : {point}")


# print(league_winner2())
# print("")
# sorting(col_data)
# data = []
# panjang = len(col_data)
# for i, e in enumerate(col_data):
#
#     if i == panjang - 1:
#         diff = col_data[i]['point'][-2] - col_data[i]['point'][-1]
#         diff2 = col_data[i - 1]['point'][-2] - col_data[i - 1]['point'][-1]
#
#         if diff > diff2:
#             data.append(col_data[i])
#             data.append(col_data[i - 1])
#
#     else:
#         diff = col_data[i]['point'][-2] - col_data[i]['point'][-1]
#         diff2 = col_data[i + 1]['point'][-2] - col_data[i - 1]['point'][-1]
#
#         if diff > diff2:
#             data.append(col_data[i])
#             data.append(col_data[i + 1])
#
# for e in data:
#     pointss = e['point'][0] * 3 + 1 * e['point'][2] - 0 * e['point'][1]
#     print(f"{e} - point : {pointss}")

# for e in sorting():
#     data = []
#     pointss = e['point'][0] * 3 + 1 * e['point'][2] - 0 * e['point'][1]
#     print(f"{e} - point : {pointss}")
#     if e['point'][-2] > e['point'][-1]:
#         data.append(col_data[])