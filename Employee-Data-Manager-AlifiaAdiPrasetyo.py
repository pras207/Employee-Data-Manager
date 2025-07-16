import re
from tabulate import tabulate

# Data karyawan perusahaan yang sudah ada di sebuah perusahaan
data_perusahaan_karyawan = [
    {"ID": 1, "Nama": "Alifia Prasetyo", "Alamat": "Jln.Asep Berlian No.14", "Agama": "Islam", "Email": "alifiakeren123@example.com"},
    {"ID": 2, "Nama": "Luthfi Surya", "Alamat": "Jln.Merdeka Asri No.56", "Agama": "Islam", "Email": "muhammadluthfi@example.com"},
    {"ID": 3, "Nama": "Amelia Yulia", "Alamat": "Gg.Mekarsari No.154", "Agama": "Kristen", "Email": "amelsukses@example.com"},
    {"ID": 4, "Nama": "Reza Bagus", "Alamat": "Jln.Nusantara No.218", "Agama": "Buddha", "Email": "rezaqwerty12@gmail.com"},
    {"ID": 5, "Nama": "Refalo Ria", "Alamat": "Jln.Haji Mekar No.10", "Agama": "Kristen", "Email": "olafer192@example.com"},
    {"ID": 6, "Nama": "Gina Indah", "Alamat": "Gg.Fitra Sari No.54", "Agama": "Islam", "Email": "gina21cantik@gmail.com"},
    {"ID": 7, "Nama": "Fitra Vaci", "Alamat": "Jln.Ahmad Kusuma No.76", "Agama": "Islam", "Email": "fitrajs@gmail.com"},
    {"ID": 8, "Nama": "Vavian Okeri", "Alamat": "Jln.Rima Kadi No.14", "Agama": "Katolik", "Email": "Vaviansk109@gmail.com"},
    {"ID": 9, "Nama": "James Axelod", "Alamat": "Jln.Jiwaraga No.216", "Agama": "Kristen", "Email": "James278@example.com"},
    {"ID": 10, "Nama": "Fajar Ramadhan", "Alamat": "Jln.Givari  No.18", "Agama": "Islam", "Email": "FjrR432@gmail.com"},
    {"ID": 11, "Nama": "Muhammad Ardiansyah", "Alamat": "Jln.Haji Nifa No.76", "Agama": "Islam", "Email": "MHMDAR56@example.com"},
    {"ID": 12, "Nama": "Abi Syahli", "Alamat": "Gg.Jaka No.89", "Agama": "Islam", "Email": "ASYAHLI@gmail.com"},
    {"ID": 13, "Nama": "Nur Alamsyah", "Alamat": "Jln.Burang No.728", "Agama": "Islam", "Email": "NURalamsyah@gmail.com"},
    {"ID": 14, "Nama": "Mulyadi", "Alamat": "Jln.Vicars No.11", "Agama": "Islam", "Email": "MULDI21@example.com"},
    {"ID": 15, "Nama": "Annisa Melati", "Alamat": "Gg.Kirana No.89", "Agama": "Islam", "Email": "Melati671@gmail.com"},
    {"ID": 16, "Nama": "Siti Afisah", "Alamat": "Jln.Ghijaka No.19", "Agama": "Islam", "Email": "Sitiafish@example.com"},
    {"ID": 17, "Nama": "Ahmad Iqbal", "Alamat": "Jln.Ilsam No.78", "Agama": "Islam", "Email": "AHMADiqbal98@gmail.com"},
    {"ID": 18, "Nama": "Vicky Uris", "Alamat": "Jln.Jiuwar No.172", "Agama": "Kristen", "Email": "VCYuris09@example.com"},
]

# Untuk memvalidasi email user 
# Ringkasan untuk pola dibawah: pola = r"^[\w\.-]+@[\w\.-]+\.\w+$"
# ^ : Untuk mengawali string
# [\w\.-]+ : Username seperti (huruf,angka,titik,dash "-")
# @ : Untuk mewajibkan user menggunakan "@"
# [\w\.-]+ : Domain name, untuk mengidentifikasi alamat suatu situs web
# \. : Titik literal
# \w+ : Ekstensi domain atau bagian akhir dari alamat domain yang menunjukan lokasi situs tersebut
# $ : Akhir string
def validasi_email(email):
    pola = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pola, email)

# Untuk menambahkan otomatis nomer data baru
def menambah_id_baru():
    if not data_perusahaan_karyawan:
        return 1
    return max(k["ID"] for k in data_perusahaan_karyawan) + 1

# Untuk menampilkan data yang sudah ditambahkan 
def tampilkan_data(data):
    if not data:
        print("Tidak ada data untuk ditampilkan.\n")
        return
    
    tabel_untuk_data = []
    for k in data:
        tabel_untuk_data.append([
            k["ID"],
            k["Nama"],
            k["Alamat"],
            k["Agama"],
            k["Email"]
        ])
    headers = ["ID", "Nama", "Alamat", "Agama", "Email"]
    print(tabulate(tabel_untuk_data, headers=headers, tablefmt="grid"))
    print()

# Opsi untuk user, ingin kembali ke menu utama atau tidak
def lanjut_atau_keluar():
    while True:
        pilihan = input("Apakah anda ingin kembali ke menu utama? (y/n) ").lower()
        if pilihan == 'y':
            return
        elif pilihan == 'n':
            print("======== Terima kasih, sampai jumpa lagi! ========")
            exit()
        else:
            print("Mohon masukkan 'y' atau 'n' saja.")

# Untuk memvalidasi konfirmasi user
def konfirmasi_user(pesan):
    while True:
        jawaban = input(pesan + "(y/n): ").lower()
        if jawaban == 'y':
            return True
        elif jawaban == 'n':
            return False
        else:
            print("Tolong hanya masukkan 'y' atau 'n' saja.")

# Mencari karyawan berdasarkan nama atau ID yang sudah ada di list dict diatas
def cari_karyawan():
    keyword = input("Masukkan Nama atau ID: ").strip()
    hasil = []
    if keyword.isdigit():
        hasil = [k for k in data_perusahaan_karyawan if k["ID"] == int(keyword)]
    else:
        hasil = [k for k in data_perusahaan_karyawan if keyword.lower() in k["Nama"].lower()]

    if hasil:
        print("\n======== Hasil Pencarian ========")
        tampilkan_data(hasil)
    else: 
        print("Karyawan tidak ditemukan!")

# Menambahkan data yang akan di input oleh user.
def create():
    print("\n======== TAMBAH DATA KARYAWAN ========")
    nama = input("Nama: ")
    alamat = input("Alamat: ")
    agama = input("Agama: ")
    while True:
        email = input("Email: ")
        if validasi_email(email):
            break
        else:
            print("Format email tidak valid! Tolong gunakan format seperti nama@example.com")
    

# Menampilkan ringkasan data yang user ingin ditambahkan 
    print("\n======== KONFIRMASI DATA ========")
    print(f"Nama   : {nama}")
    print(f"Alamat : {alamat}")
    print(f"Agama  : {agama}")
    print(f"Email  : {email}")

    konfirmasi = input("Apakah anda yakin menyimpan data ini? (y/n): ").strip().lower()
    if konfirmasi == 'y':
        karyawan_baru = {
            "ID": menambah_id_baru(),
            "Nama": nama,
            "Alamat": alamat,
            "Agama": agama,
            "Email": email
        }
        data_perusahaan_karyawan.append(karyawan_baru)
        print("Karyawan berhasil ditambahkan!\n")
    else:    
        print("Penambahan dibatalkan.\n")

# Opsi untuk user membaca data yang sudah ada.
def read():
    print("\n======== DAFTAR KARYAWAN ========")
    
    if not data_perusahaan_karyawan:
        print("Tidak ada data untuk ditampilkan.\n")
        return
    tabel_untuk_data = []
    for karyawan in data_perusahaan_karyawan:
        tabel_untuk_data.append([
            karyawan["ID"],
            karyawan["Nama"],
            karyawan["Alamat"],
            karyawan["Agama"],
            karyawan["Email"]
        ])
    headers = ["ID", "Nama", "Alamat", "Agama", "Email"]
    print(tabulate(tabel_untuk_data, headers=headers, tablefmt="grid"))
    print()

# Opsi untuk user ketika ingin update sebuah email yang sudah ada maupun baru dibuat
def update():
    while True:
        print("\n======== UPDATE DATA KARYAWAN ========")
        id_update = input("Masukkan ID karyawan yang ingin diubah: ")

        ditemukan = False
        for karyawan in data_perusahaan_karyawan:
            if str (karyawan["ID"]) == id_update:
               ditemukan = True
               print("\nData telah ditemukan: ")
               tampilkan_data([karyawan])

               nama_baru = input("Nama baru (tekan ENTER jika tidak ingin diubah): ")
               alamat_baru = input("Alamat baru (tekan ENTER jika tidak ingin diubah): ")
               agama_baru = input("Agama baru (tekan ENTER jika tidak ingin diubah): ")
               while True:
                   email_baru = input("Email baru (tekan ENTER jika tidak ingin diubah): ")
                   if email_baru == "":
                    break
                   elif validasi_email(email_baru):
                    break
                   else:
                       print("Format email tidak valid! Tolong gunakan format seperti nama@example.com")

               if konfirmasi_user ("\nApakah kamu yakin ingin Update data ini?"):
                    if nama_baru: karyawan["Nama"] = nama_baru
                    if alamat_baru: karyawan["Alamat"] = alamat_baru
                    if agama_baru: karyawan["Agama"] = agama_baru
                    if email_baru: karyawan["Email"] = email_baru
                    print("Data telah berhasil di-Update!\n")
                    return
               else:
                   print("Update telah dibatalkan.\n")
                   if konfirmasi_user("Apakah anda ingin mencoba update data lagi? "):
                       break
                   else:
                       lanjut_atau_keluar()
                       return
        if not ditemukan:
            print("Karyawan dengan ID tersebut tidak ditemukan.\n")
            if konfirmasi_user("Apakah anda ingin mencoba memasukan ID lain? "):
                continue
            else:
                lanjut_atau_keluar
                return
               

# Opsi untuk user ketika ingin menghapus sebuah data yang sudah ada maupun yang baru ditambahkan
def delete():
    while True:
        print("\n======== HAPUS DATA KARYAWAN ========")
        hapus_id = input("Masukkan ID karyawan yang ingin dihapus: ")

        ditemukan = False
        for i, karyawan in enumerate(data_perusahaan_karyawan):
            if str(karyawan["ID"]) == hapus_id:
               print("\nData yang akan dihapus:")
               tampilkan_data([karyawan])

               if konfirmasi_user ("Apakah anda yakin ingin menghapus data ini? "):
                   del data_perusahaan_karyawan[i]
                   print("Data karyawan berhasil di hapus\n")
               else:
                   print("Penghapusan telah dibatalkan.\n")
                   if konfirmasi_user("Apakah anda ingin mencoba menghapus data lain? "):
                       break
                   else:
                       lanjut_atau_keluar()
                       return
               ditemukan = True
               break
    
        if not ditemukan:
            print("ID yang kamu masukkan tidak ada.\n")
            if konfirmasi_user("Apakah anda mencoba memasukan ID lain? "):
                continue
            else:
                lanjut_atau_keluar()
                return


# Menu Utama 
def main():
    while True:
        print("======== SELAMAT DATANG DI DATA KARYAWAN! ========")
        print("1. Menambah Data Karyawan")
        print("2. Lihat Data Karyawan")
        print("3. Update Data Karyawan")
        print("4. Hapus Data Karyawan")
        print("5. Mencari Data Karyawan")
        print("6. Keluar Dari Program")

        pilihan = input("Pilih Menu (1 - 6): ")
        print()

        if pilihan == "1":
            if konfirmasi_user ("Apakah anda yakin ingin menambah data? "):
                create()
            else:
                print("Anda telah membatalkan penambahan data. \n")
                lanjut_atau_keluar()
        elif pilihan == "2":
            if konfirmasi_user ("Apakah anda ingin melihat data? "):
                read()
            else:
                print("Anda telah membatalkan melihat data.\n")
                lanjut_atau_keluar()
        elif pilihan == "3":
            if konfirmasi_user ("Apakah anda yakin ingin Update data? "):
                update()
            else:
                print("Anda telah membatalkan untuk Update data.\n")
                lanjut_atau_keluar()
        elif pilihan == "4":
            if konfirmasi_user ("Apakah anda yakin ingin menghapus data? "):
                delete()
            else:
                print("Anda telah membatalkan penghapusan data,\n")
            lanjut_atau_keluar()
        elif pilihan == "5":
            if konfirmasi_user ("Apakah anda yakin ingin mencari data karyawan? "):
                cari_karyawan()
            else:
                print("\nAnda telah membatalkan untuk mencari data.")
                lanjut_atau_keluar()
        elif pilihan == "6":
            if konfirmasi_user ("Apakah anda benar benar ingin keluar dari program ini? "):
                print ("======== Terima kasih, Silahkan kembali lagi lain waktu ya! ========")
                break
            else:
                print("Anda telah membatalkan keluar dari program. Kembali ke menu utama.\n")
        else:
            print("Pilihan kamu gak valid. Coba masukkan berdasarkan nomer (1-6)!\n")

# Menjalankan program
main()