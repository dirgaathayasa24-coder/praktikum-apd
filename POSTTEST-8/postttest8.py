from prettytable import PrettyTable

dataAkun = {
    "sepul": "123",
    "dirga": "115"
}

dataUang = [
    {"nama": "Rupiah", "kekuatan": "Lemah", "tahun": 2020}
]

statusLogin = None

def register():
    print("=== REGISTRASI ===")
    username = input("Input username : ")
    password = input("Input password : ")

    if username in dataAkun:
        print("Username sudah terdaftar!")
    else:
        dataAkun[username] = password
        print("Berhasil register!")

def login():
    print("=== LOGIN ===")
    username = input("Username anda : ")
    password = input("Password anda : ")

    if username in dataAkun and dataAkun[username] == password:
        print(f"\nBerhasil Login sebagai '{username}'!")
        return username
    else:
        print("Username atau password salah!")
        return None

def tampilkan_data():
    if not dataUang:
        print("Belum ada data uang.")
    else:
        tabel = PrettyTable()
        tabel.field_names = ["No", "Nama Uang", "Kekuatan Uang", "Tahun Rilis"]
        for i, uang in enumerate(dataUang, start=1):
            tabel.add_row([i, uang["nama"], uang["kekuatan"], uang["tahun"]])
        print(tabel)

def tambah_data(nama, kekuatan, tahun):
    dataUang.append({"nama": nama, "kekuatan": kekuatan, "tahun": tahun})
    print(f"Data uang '{nama}' berhasil ditambahkan!")

def ubah_data():
    try:
        tampilkan_data()
        pilih = int(input("Pilih nomor data yang ingin diupdate: ")) - 1
        if 0 <= pilih < len(dataUang):
            nama = input("Masukkan nama uang baru: ")
            kekuatan = input("Masukkan kekuatan uang baru: ")
            tahun = input("Masukkan tahun rilis baru: ")
            dataUang[pilih] = {"nama": nama, "kekuatan": kekuatan, "tahun": tahun}
            print("Data berhasil diupdate!")
        else:
            print("Nomor data tidak valid!")
    except ValueError:
        print("Input harus berupa angka!")

def hapus_data():
    try:
        tampilkan_data()
        pilih = int(input("Pilih nomor data yang ingin dihapus: ")) - 1
        if 0 <= pilih < len(dataUang):
            hapus = dataUang.pop(pilih)
            print(f"Data '{hapus['nama']}' berhasil dihapus.")
        else:
            print("Nomor data tidak valid!")
    except ValueError:
        print("Input harus berupa angka!")

def menu_admin():
    while True:
        print("""
=== KEUANGAN DUNIA ===
---------------------
1. TAMBAH DATA UANG
2. TAMPILKAN DATA UANG
3. UBAH DATA UANG
4. HAPUS DATA UANG
5. LOGOUT
=====================
""")
        pilih = input("PILIH: ")
        if pilih == "1":
            nama = input("Nama Uang: ")
            kekuatan = input("Kekuatan Uang: ")
            tahun = input("Tahun Rilis: ")
            tambah_data(nama, kekuatan, tahun)
        elif pilih == "2":
            tampilkan_data()
        elif pilih == "3":
            ubah_data()
        elif pilih == "4":
            hapus_data()
        elif pilih == "5":
            print("Logout...\n")
            break
        else:
            print("Input salah! hanya bisa (1-5)")

def menu_pengguna():
    while True:
        print("""
=== MENU PENGGUNA ===
---------------------
1. TAMBAH DATA UANG
2. LIHAT DATA UANG
3. LOGOUT
=====================
""")
        pilih = input("PILIH: ")
        if pilih == "1":
            nama = input("Nama Uang: ")
            kekuatan = input("Kekuatan Uang: ")
            tahun = input("Tahun: ")
            tambah_data(nama, kekuatan, tahun)
        elif pilih == "2":
            tampilkan_data()
        elif pilih == "3":
            print("Logout...")
            break
        else:
            print("Input salah!")

while True:
    print("""
--------------------------------
- 1. Register                  -
- 2. Login                     -
- 3. KELUAR                    -
--------------------------------
""")
    pilihan = input("Pilih (1-3): ")

    if pilihan == "1":
        register()
    elif pilihan == "2":
        user = login()
        if user:
            if user == "admin":
                print("Selamat datang, ADMIN.")
                menu_admin()
            else:
                print("Selamat datang, Pengguna biasa.")
                menu_pengguna()
    elif pilihan == "3":
        print("Program Berhenti.")
        break
    else:
        print("Input salah! hanya bisa (1-3)")