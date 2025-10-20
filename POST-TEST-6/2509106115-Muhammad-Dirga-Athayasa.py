dataAkun = {
    "dirga": "115"
}

dataUang = [
    {"nama": "Rupiah", "kekuatan": "Lemah", "tahun": 2020}
]

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
            print("\nBerhasil Login!")
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
                    print("== TAMBAH DATA ==")
                    nama_uang = input("Nama Uang: ")
                    kekuatan_uang = input("Kekuatan Uang (kuat/sedang/lemah): ")
                    tahun_rilis = input("Tahun Rilis: ")

                    dataUang.append({
                        "nama": nama_uang,
                        "kekuatan": kekuatan_uang,
                        "tahun": tahun_rilis
                    })
                    print(f"Data uang '{nama_uang}' berhasil ditambahkan!")

                elif pilih == "2":
                    print("== DATABASE ==")
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

                elif pilih == "3":
                    print("== UPDATE DATA UANG ==")
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

                elif pilih == "4":
                    print("== HAPUS DATA ==")
                    for i, uang in enumerate(dataUang, start=1):
                        print(f"{i}. {uang['nama']}")

                    inputHapus = int(input("Pilih nomor data yang ingin dihapus: ")) - 1

                    if 0 <= inputHapus < len(dataUang):
                        hapus = dataUang.pop(inputHapus)
                        print(f"Data '{hapus['nama']}' berhasil dihapus.")
                    else:
                        print("Nomor data tidak valid!")

                elif pilih == "5":
                    print("Logout...")
                    break

                else:
                    print("Input salah! hanya bisa (1-5)")
        else:
            print("Username atau password salah!")

    elif inputMenuUtama == "3":
        print("Program Berhenti.")
        break

    else:
        print("Input salah! hanya bisa (1-3)")