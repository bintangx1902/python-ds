# import os
#
# klass = [
#     {"name": "BhayangkaraFC", "point": [11, 10, 13, 22, 10]},
#     {"name": "Persib", "point": [14, 8, 12, 24, 9]},
#     {"name": "Arema", "point": [9, 14, 11, 38, 17]},
#     {"name": "Bali", "point": [10, 8, 16, 30, 10]},
#     {"name": "PSIS", "point": [8, 7, 19, 35, 16]},
#     {"name": "Persebaya", "point": [15, 10, 9, 29, 30]},
#
# ]
#
#
# def sorting():
#     global klass
#     klass.sort(key=lambda e: sum(e['point']) - e['point'][2] - e['point'][4])
#     return klass
#
#
# def league_winner1():
#     for x in reversed(sorting()):
#         point = sum(x['point']) - x['point'][2] - x['point'][4]
#         return x['name']
#
#
# def league_winner2():
#     league = [x['name'] for x in reversed(sorting())]
#     return league
#
#
# def search():
#     global klass
#     x = 50
#     for li in klass:
#         point = sum(li['point']) - li['point'][2] - li['point'][4]
#         if point <= x:
#             print(f"{li} - total point : {point}")
#
#
# if __name__ == '__main__':
#
#     """ python 3.10 """
#     while True:
#         print("1. show league winner \n2. search club point less then equal to 50 \n3. exit")
#         menu = int(input(">>> "))
#         match menu:
#             case 1:
#                 print(league_winner1())
#                 print(league_winner2())
#                 with open('test.txt', 'w') as f:
#                     f.write(f"Winner no 1 : {league_winner1()} \nlist of winner : {league_winner2()}")
#                 os.system('cls')
#             case 2:
#                 search()
#                 with open('test.txt', 'w') as f:
#                     f.write(f"under point \n{search()}")
#                 os.system('cls')
#             case 3:
#                 break
#             case _:
#                 print("Give input as menu! ")
# # list_mobil = [
# #     {'type': "avanza_s", "color": "red", "engine": "petrol", "stock": 10},
# #     {'type': "avanza_q", "color": "red", "engine": "petrol", "stock": 5},
# #     {'type': "kijang_v", "color": "blue", "engine": "diesel", "stock": 3},
# #     {'type': "kijang_s", "color": "black", "engine": "diesel", "stock": 5},
# #     {'type': "kijang_q", "color": "red", "engine": "diesel", "stock": 4},
# # ]
# #
# #
# # def stock_mobil():
# #     global list_mobil
# #     stock = 0
# #     for x in list_mobil:
# #         availability = x['stock']
# #         stock += availability
# #
# #     return stock
# #
# #
# # def tampil_warna():
# #     global list_mobil
# #     col_list = [x['color'] for x in list_mobil]
# #     for f in col_list:
# #         print(f)
# #
# #
# # if __name__ == '__main__':
# #     while True:
# #         print("1. show stock mobil \n2. show available car color \n3. exit")
# #         menu = int(input("masukan menu : "))
# #
# #         if menu == 1:
# #             print(stock_mobil())
# #             with open('test.txt', 'w') as f:
# #                 f.write(f"Stock mobil : {stock_mobil()}")
# #         elif menu == 2:
# #             tampil_warna()
# #         elif menu == 3:
# #             break
# #         else:
# #             print("masukan menu yang tersedia")
# #
# #
# #             """oke sudah selesai"""
col_data = []


def append_data(nim, presence):
    global col_data
    key = ("nim", "presence")
    value = (nim, presence)
    dict_data = dict(zip(key, value))
    col_data.append(dict_data)


with open('test.txt', 'r') as f:
    data = f.read().splitlines()

for x in data:
    raw_data = x.split()
    nim = raw_data[0]
    presence = [p for p in raw_data[1:]]
    append_data(nim, presence)


for col in col_data:
    print(col)