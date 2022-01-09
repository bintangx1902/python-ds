col_data = []


def append_data(nim, presence):
    global col_data
    key = ("nim", "presence")
    value = (nim, presence)
    dict_data = dict(zip(key, value))
    col_data.append(dict_data)


with open('number/8.txt', 'r') as f:
    data = f.read().splitlines()

for x in data:
    raw_data = x.split()
    nim = raw_data[0]
    presence = [int(p) for p in raw_data[1:]]
    append_data(nim, presence)


def report():
    for x in col_data:
        presence = x['presence'].count(1)
        minimum = int(len(x['presence']) * .75)
        if presence > minimum:
            print(f"{x} - allowed")
        else:
            print(f"{x} - disallowed")


def sorting():
    global data
    col_data.sort(key=lambda x: x["presence"].count(0))
    return data


def top():
    for x in reversed(sorting()):
        print(x)


if __name__ == '__main__':
    while True:
        print("1. report of college student \n2. most laziest student \n3. exit")
        menu = int(input(">>> "))

        if menu == 1:
            report()
        elif menu == 2:
            top()
        elif menu == 3:
            break
        else:
            print("give the same input menus ! ")
