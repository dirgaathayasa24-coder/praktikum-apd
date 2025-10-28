dataAkun = {
    "sepul": "123",     
    "dirga": "115"    
}

dataUang = [
    {"nama": "Rupiah", "kekuatan": "Lemah", "tahun": 2020}
]

statusLogin = None  


def tampilkan_data():
    """Menampilkan semua data uang"""
    if not dataUang:
        print("Belum ada data uang.")
    else:
        for i, uang in enumerate(dataUang, start=1):
            print(f"""
_____________________________
| Data uang ke-{i}
| Nama Uang     : {uang['nama']}
| Kekuatan Uang : {uang['kekuatan']}
| Tahun Rilis   : {uang['tahun']}
-----------------------------""")

def tambah_data(nama, kekuatan, tahun):
    """Menambahkan data uang baru"""
    dataUang.append({"nama": nama, "kekuatan": kekuatan, "tahun": tahun})
    print(f"Data uang '{nama}' berhasil ditambahkan!")

def ubah_data():
    """Prosedur untuk mengubah data"""
    try:
        for i, uang in enumerate(dataUang, start=1):
            print(f"{i}. {uang['nama']}")
        pilihUang = int(input("Pilih nomor data yang ingin diupdate: ")) - 1

        if 0 <= pilihUang < len(dataUang):
            nama_baru = input("Masukkan nama uang baru: ")
            kekuatan_baru = input("Masukkan kekuatan uang baru: ")
            tahun_baru = input("Masukkan tahun rilis baru: ")

            dataUang[pilihUang] = {
                "nama": nama_baru,
                "kekuatan": kekuatan_baru,
                "tahun": tahun_baru
            }
            print("Data berhasil diupdate!")
        else:
            print("Nomor data tidak valid!")
    except ValueError:
        print("Input harus berupa angka!")


def hapus_data():
    """Prosedur untuk menghapus data"""
    try:
        for i, uang in enumerate(dataUang, start=1):
            print(f"{i}. {uang['nama']}")
        inputHapus = int(input("Pilih nomor data yang ingin dihapus: ")) - 1

        if 0 <= inputHapus < len(dataUang):
            hapus = dataUang.pop(inputHapus)
            print(f"Data '{hapus['nama']}' berhasil dihapus.")
        else:
            print("Nomor data tidak valid!")
    except ValueError:
        print("Input harus berupa angka!")

def menu_keuangan():
    """Fungsi rekursif untuk menampilkan menu keuangan berulang"""
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

    nama_uang = kekuatan_uang = tahun_rilis = ""

    if pilih == "1":
        print("== TAMBAH DATA ==")
        nama_uang = input("Nama Uang: ")
        kekuatan_uang = input("Kekuatan Uang (kuat/sedang/lemah): ")
        tahun_rilis = input("Tahun Rilis: ")
        tambah_data(nama_uang, kekuatan_uang, tahun_rilis)

    elif pilih == "2":
        tampilkan_data()

    elif pilih == "3":
        ubah_data()

    elif pilih == "4":
        hapus_data()

    elif pilih == "5":
        print("Logout...\n")
        return  

    else:
        print("Input salah! hanya bisa (1-5)")

    menu_keuangan()

while True:
    print("""
--------------------------------
- 1. Register                  -
- 2. Login                     -
- 3. KELUAR                    -
--------------------------------
""")
    inputMenuUtama = input("Pilih (1-3): ")

    if inputMenuUtama == "1":
        print("=== REGISTRASI ===")
        registUsername = input("Input username : ")
        registPassword = input("Input password : ")

        if registUsername in dataAkun:
            print("Username sudah terdaftar!")
        else:
            dataAkun[registUsername] = registPassword
            print("Berhasil register!")

    elif inputMenuUtama == "2":
        print("=== LOGIN ===")
        inputUsername = input("Username anda : ")
        inputPassword = input("Password anda : ")

        if inputUsername in dataAkun and dataAkun[inputUsername] == inputPassword:
            statusLogin = inputUsername
            print(f"\nBerhasil Login sebagai '{statusLogin}'!")

            if statusLogin == "admin":
                print("Selamat datang, ADMIN.")
                menu_keuangan()
            else:
                print("Selamat datang, Pengguna biasa.")
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

        else:
            print("Username atau password salah!")

    elif inputMenuUtama == "3":
        print("Program Berhenti.")
        break

    else:
        print("Input salah! hanya bisa (1-3)")