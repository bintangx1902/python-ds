car_list = []


def append_data(name, color, engine, stock):
    key = ('name', 'color', 'engine', 'stock')
    value = (name, color, engine, stock)
    dict_data = dict(zip(key, value))
    car_list.append(dict_data)


with open('number/14.txt', 'r') as f:
    car_raw = f.read().splitlines()
    for raw in car_raw:
        x = raw.split('#')
        name = x[0]
        color = x[1]
        engine = x[2]
        stock = x[-1]
        append_data(name, color, engine, stock)


