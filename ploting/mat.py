data = [
    {"nim": "20188144", "hadir": [0, 1, 1, 1, 0, 0, 1]},
    {"nim": "20188122", "hadir": [1, 1, 1, 1, 0, 1, 1]},
    {"nim": "20188146", "hadir": [1, 1, 1, 1, 1, 0, 1]},
]


def report():
    for x in data:
        presence = x['hadir'].count(1)
        minimum = int(len(x['hadir']) * .75)
        if presence > minimum:
            print(f"{x} - allowed")
        else:
            print(f"{x} - disallowed")


def sorting():
    global data
    data.sort(key=lambda x: x["hadir"].count(0))
    return data


def top():
    for x in reversed(sorting()):
        print(x)


report()
top()
