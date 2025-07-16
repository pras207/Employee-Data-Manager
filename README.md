# Employee-Data-Manager

Employee-Data-Manager adalah aplikasi sederhana berbasis Python untuk mengelola data karyawan di sebuah perusahaan. Aplikasi ini dapat digunakan untuk menambah, melihat, mengubah, menghapus, dan mencari data karyawan melalui input oleh user yang dapat digunakan secara mudah dan dapat digunakan oleh seluruh kalangan mau itu karyawan ataupun non karyawan. Data karyawan disini disimpan dalam bentuk list of dictionary di dalam program.

## Fitur

- **Menambah Data Karyawan**  
  Pengguna dapat menambahkan data karyawan baru, termasuk nama, alamat, agama, dan email. Email akan divalidasi agar sesuai dengan format yang benar.

- **Melihat Data Karyawan**  
  Menampilkan seluruh data karyawan yang tersimpan dalam bentuk tabel menggunakan library `tabulate`.

- **Update Data Karyawan**  
  Memungkinkan pengguna untuk mengubah data karyawan berdasarkan ID. Pengguna dapat memilih data mana saja yang ingin diubah.

- **Hapus Data Karyawan**  
  Menghapus data karyawan berdasarkan ID dengan konfirmasi sebelum penghapusan.

- **Mencari Data Karyawan**  
  Mencari data karyawan berdasarkan nama atau ID.

## Instalasi

1. Pastikan Python sudah terpasang di komputer Anda (minimal Python 3).
2. Install dependensi `tabulate` dengan perintah:
   ```
   pip install tabulate
   ```
3. Download file `Employee-Data-Manager-AlifiaAdiPrasetyo.py`.

## Cara Menggunakan

1. Jalankan program:
   ```
   python Employee-Data-Manager-AlifiaAdiPrasetyo.py
   ```
2. Pilih menu yang tersedia:
   - 1: Menambah Data Karyawan
   - 2: Lihat Data Karyawan
   - 3: Update Data Karyawan
   - 4: Hapus Data Karyawan
   - 5: Mencari Data Karyawan
   - 6: Keluar Dari Program

3. Ikuti petunjuk pada layar untuk setiap menu.

## Validasi Email

Aplikasi ini melakukan validasi input email agar sesuai dengan format yang benar, misalnya: `nama@example.com`.

## Library Pihak Ketiga

- [tabulate](https://pypi.org/project/tabulate/) digunakan untuk menampilkan data dalam format tabel di terminal.

## Catatan

- Semua data tersimpan hanya selama program berjalan (tidak tersimpan secara permanen).
- Program berjalan pada terminal atau command prompt.
- Program menggunakan bahasa Indonesia untuk seluruh antarmuka dan pesan.

## Lisensi

Proyek ini dibuat untuk pembelajaran dan penggunaan pribadi.
