contact_dict = {"names": [], "telephones": []}

def show_contact():
    contact_size = len(contact_dict["names"])
    if contact_size > 0 :
        print("\nDaftar kontak:")
        for i in range(contact_size):
            print("Nama:", contact_dict["names"][i])
            print("No Telepon:", contact_dict["telephones"][i])
    else:
        print("Belum ada kontak yang didaftarkan")

def add_contact():
    name = str(input("Nama: "))
    while True:
        try:
            telephone = int(input("No Telepon: "))
            break
        except ValueError:
            print("Anda hanya bisa input angka untuk no telephone")

    contact_dict["names"].append(name)
    contact_dict["telephones"].append(telephone)

def func_contact_list_menu():
    print("Selamat datang!")

    while True:
        print("\n-- Menu --")
        print("1. Daftar Kontak")
        print("2. Tambah Kontak")
        print("3. Keluar")
        menu = int(input("Pilih menu: "))
        if menu == 1:
            show_contact()
        elif menu == 2:
            add_contact()
        elif menu == 3:
            break
        else:
            print("Menu tidak tersedia")

    print("Program selesai, sampai jumpa!")

func_contact_list_menu()
