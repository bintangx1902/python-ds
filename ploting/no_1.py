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
    name_list.append(p['player1']) if p['point1'] > 0 else ''
    name_list.append(p['player2']) if p['point2'] > 0 else ''

name_copy = name_list.copy()
name_list = list(set(name_list))

""" uncomment this section if u want to know the how many players win and draw (in1) """
# for n in name_list:
#     print(f"{n} - {name_copy.count(n)}")


""" b question returning how many players in data """
def player():
    return len(name_list)


print(f"total players : {player()}")


def winner():
    play_point = []

    for name in name_list:
        point = 0
        # assume index 0
        for list_p in point_list:
            # assume index 1
            point += float(list_p['point1']) if list_p['player1'] == name else 0
            point += float(list_p['point2']) if list_p['player2'] == name else 0
        play_point.append(point)

    for index, value in enumerate(play_point):
        print(f"{name_list[index]} - points : {value}")


winner()
