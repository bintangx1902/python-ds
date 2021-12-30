import os

with open('number/31.txt', 'r') as f:
    data = f.read().splitlines()

col_data = []

for x in data:
    raw_list = []
    raw = x.replace(".", "").replace(",", "").split()
    for i in raw:
        if i.isdigit():
            i = int(i)
        raw_list.append(i)
    col_data.append(raw_list)


""" print this to get the value for 'b' answer """
def total_num():
    num = 0
    for raw_data in col_data:
        for num_data in raw_data:
            if isinstance(num_data, int):
                num += num_data
    return num


def sorting(list_name: list):
    list_name.sort(reverse=True, key=lambda u: u['count'])
    return list_name


def append_data(word, count, list_name: list):
    key = ("word", "count")
    value = (word, count)
    dict_data = dict(zip(key, value))
    list_name.append(dict_data)


def freq_shown():
    kata, setter = [], []
    for list_data in col_data:
        for word in list_data:
            kata.append(word)

    word_copy = kata.copy()
    kata = list(set(kata))
    for kanji in kata:
        # print(f"kanji : {kanji} - {word_copy.count(kanji)}")
        append_data(kanji, word_copy.count(kanji), setter)
    return setter


""" use this to print the value to get the 'c' answer """
def high_freq():
    for active in sorting(freq_shown()):
        return active


