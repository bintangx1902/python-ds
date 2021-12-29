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


for x in col_data:
    print(x)


def sorting(klass):
    klass.sort(
        key=lambda e: (e['point'][0] * 3 + 1 * e['point'][2] - 0 * e['point'][1]) and e['point'][-2] - e['point'][-1])


# def selisih_gol() :
#     global klass
#     klass.sort(key=lambda goal:goal['point'][-2] - goal['point'][-1])
# def league_winner1():
#     for x in reversed(sorting()):
#         point = sum(x['point']) - x['point'][2] - x['point'][4]
#         return x['name']

# #get the fuckin data in point
# def points(point):
#     if point[-2] > point[-1]:
#         return True
#     return False


def bbs():
    n = len(arr)

    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also work but outer loop will repeat one time more than needed.

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element

            """ [. . . .6] > [. . . . .3] """
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# def league_winner2():
#    league = [x['name'] for x in reversed(sorting())]
#    for x in league :
#        print(x)
#    for x in reversed(sorting()) :
#        if x
#        print(x)
# global klass

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


def search():
    global klass
    x = 50
    for li in klass:
        point = 3 * li['point'][0] + li['point'][2] * 1
        print(point)
        if point <= x:
            print(f"{li} - total point : {point}")


# print(league_winner2())
print("")
sorting(klass)
data = []
panjang = len(klass)
for i, e in enumerate(klass):

    if i == panjang - 1:
        diff = klass[i]['point'][-2] - klass[i]['point'][-1]
        diff2 = klass[i - 1]['point'][-2] - klass[i - 1]['point'][-1]

        if diff > diff2:
            data.append(klass[i])
            data.append(klass[i - 1])

    else:
        diff = klass[i]['point'][-2] - klass[i]['point'][-1]
        diff2 = klass[i + 1]['point'][-2] - klass[i - 1]['point'][-1]

        if diff > diff2:
            data.append(klass[i])
            data.append(klass[i + 1])

for e in data:
    pointss = e['point'][0] * 3 + 1 * e['point'][2] - 0 * e['point'][1]
    print(f"{e} - point : {pointss}")

# for e in sorting():
#     data = []
#     pointss = e['point'][0] * 3 + 1 * e['point'][2] - 0 * e['point'][1]
#     print(f"{e} - point : {pointss}")
#     if e['point'][-2] > e['point'][-1]:
#         data.append(klass[])