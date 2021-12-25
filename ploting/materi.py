data = []


class AddData:
    def append_data(nik, nama, alamat, ttl, jalur_pen):
        global data
        key = ("nik", "nama", "tempat tanggal lahir", "jalur pendaftaran")
        value = (nik, nama, alamat, ttl)
        dict_data = dict(zip(key, value))
        data.append(dict_data)

    def insert_data():
        global data
        count = 1
        jalur = ["Mandiri", "Prestasi", "PMDK"]
        nik = int(input("Masukan NIK : "))
        nama = input("Masukan Nama : ")
        alamat = input("Masukan alamat : ")
        ttl = input("Masukan Tempat tanggal lahir : ")
        for i in jalur:
            print(f"[{count}] {i}")
            count += 1
        nik_list = []
        for x in range(len(data)):
            saved_nik = data[x]['nik']
            nik_list.append(saved_nik)
        while True:
            if nik in nik_list:
                print("NIK sudah di gunakan !")
                nik = input("Masukan ulang NIK : ")
            else:
                break

        jalur_pendaftaran = int(input("Masukan Pilihan jalur anda : "))
        if jalur_pendaftaran == 1:
            jalur_pendaftaran = jalur[0]
        elif jalur_pendaftaran == 2:
            jalur_pendaftaran = jalur[1]
        elif jalur_pendaftaran == 3:
            jalur_pendaftaran = jalur[2]
        else:
            print("Masukan angka yg tertera pada menu ! ")
            insert_data()

        AddData.append_data(nik, nama, alamat, ttl, jalur_pendaftaran)

def show_data():
        global data
        if len(data) == 0:
            print("Belum ada data ! ")
        else:
            for value in range(len(data)):
                print(f"[{value}] {data[value]}")


def edit_data():
    global data
    show_data()
    ask = input("Data mana yang ingin di ubah ? ")
    if ask.lower() == "nik":
        input1 = int(input("Cari NIK: "))
        input2 = int(input("Masukan NIK baru : "))
        for d in data:
            d.update((k, input2) for k, v in d.items() if v == input1)
    elif ask.lower() == 'nama':
        input1 = input("Cari Nama : ")
        input2 = input("Masukan nama baru : ")
        for d in data:
            d.update((k, input2) for k, v in d.items() if v == input1)
    else:
        print("DAta yang dimasukan salah !")
        edit_data()


def delete_data():
    global data
    show_data()
    ask = int(input("masukan nik -nya : "))
    if ask > len(data):
        print("ID salah")
    else:
        data.remove(data[ask])


def show_menu():
    print("[1] Show data \n[2] insert data \n[3] edit data \n[4] delete data \n[5] exit")
    menu = int(input(">>> "))

    if menu == 1:
        show_data()
    elif menu ==2:
        AddData.insert_data()
    elif menu == 3:
        edit_data()
    elif menu == 4:
        delete_data()
    elif menu == 5:
        print("Goodbye")
        exit()
    else:
        print(" Masukan sesuai pilihan yang ada ")
        show_menu()


if __name__ == '__main__':
    while True:
        show_menu()