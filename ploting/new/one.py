import os

visitors = []


def input_visitor():
    day = int(input("Masukan jumlahh hari : "))
    for x in range(1, day + 1):
        visit = int(input(f"hari ke-{x} : "))
        visitors.append(visit)


input_visitor()


def counting():
    up = 0
    down = 0
    stats = ''
    for x in range(len(visitors)):
        if x != 0:
            if visitors[x] > visitors[x - 1]:
                up += 1
                stats = 'naik'
            elif visitors[x] < visitors[x - 1]:
                stats = 'turun'
                down += 1
            print(f"hari ke-{x + 1} : {visitors[x]}")
            print(f"status : {stats}")
        else:
            print(f"hari ke-{x + 1} : {visitors[x]}")

    print(f"pengunjung naik : {up}")
    print(f"pengunjung turun : {down}")


os.system('cls')
counting()

