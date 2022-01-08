point_list = []


def append_data(p1, p2, p1p, p2p):
    key = ('player1', 'player2', 'point1', 'point2')
    value = (p1, p2, p1p, p2p)
    dict_data = dict(zip(key, value))
    point_list.append(dict_data)


with open('number/1.txt', 'r') as f:
    raw = f.read().splitlines()

for x in raw:
    splits = x.split()
    name1 = splits[0]
    name2 = splits[1]
    points = splits[-1].split('-')
    point1 = eval(points[0])
    point2 = eval(points[1])
    append_data(name1, name2, point1, point2)


name_list = []

for p in point_list:
    name_list.append(p['player1'])
    name_list.append(p['player2'])

name_copy = name_list.copy()
name_list = list(set(name_list))


# for n in name_list:
#     print(f"{n} - {name_copy.count(n)}")
print(name_copy.count('morphy'))
