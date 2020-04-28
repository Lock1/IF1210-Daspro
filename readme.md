# Tugas Besar - Dasar Pemrograman
**TBA**

### Tentang Program
- **Seluruh file** yang dikumpulkan telah diupload (Laporan, video, dan deliverable lainnya) pada folder [deliverable](/deliverable/).
- Versi **1.0** dapat didownload pada bagian [release](https://github.com/Lock1/tbdaspro/releases/tag/v1.0). **v1.0** memiliki *source code* yang **sama persis** dengan deliverable yang dikirim pada pengumpulan tugas besar. 
- Program utama bernama **Willy.py**
- Semua modul selain base, load, dan login pada package bersifat **opsional**.
- Jika salah satu modul dan kode pada program utama memanggil fungsi yang terkait dihapus, program tetap dapat berjalan secara normal untuk fungsi lain.
- Dikarenakan beberapa kelompok lain yang menggunakan *global variable*, program ini didesain untuk **tidak** menggunakan variabel global.
- Program didesain untuk bersifat *modular* dan *maintainable* sehingga tidak akan digunakan variabel global jika tidak diperlukan.
- Sebagian besar program tidak mengikuti asumsi kevalidan input, banyak *exception handler* dengan blok `try-except` yang digunakan untuk menghandle situasi yang dapat menyebabkan program keluar.

### Sistem Penyimpanan Database
- Database yang digunakan dalam format **.csv**.
- Program tidak menggunakan **library CSV** untuk membaca dan menulis database.
- Dikarenakan program tidak menggunakan library csv, user diharapkan membuat file database baru hanya menggunakan text editor untuk mencegah permasalahan.
- Untuk kasus file database yang dibuat oleh Excel dan program lain, sebagian besar program dapat berjalan secara normal.
- Jika file error, terkadang Excel dan program lain menyisipkan *invisible character* yang dapat mengganggu pembacaan fungsi load dan save.

### Array Statis - Dinamis dan String
- Seluruh Array yang digunakan statis dengan panjang maksimum **Nmax** pada config.ini
- Untuk permasalahan `string + "\n"` dianggap dinamis, pada bahasa yang memiliki sistem string adalah char of array biasanya digunakan **Null-terminated string**, dalam kasus hal tersebut dapat gunakan karakter *null* (`\0`) sebagai penanda atau mark terminasi.
- Python tidak mensupport perilaku string sebagai array of char dalam penggunaan umum.
- Karena kendala batasan waktu, akhirnya digunakan hal tersebut (`string + "\n"`) untuk workaround sementara.
- Jika memang diharuskan, seluruh string pada program dapat diimplementasikan sebagai array of char dan membuat implementasi sendiri sistem I/O untuk menghandle tipe data array of char.
- Program mengusahakan untuk **tidak** menggunakan *built-in python string method*.

### Versi dan fitur
- Dikarenakan keterbatasan waktu deadline, untuk beberapa fitur tambahan mungkin hanya ada ketika setelah tugas besar terkumpul.
- Beberapa fitur yang mungkin ditambahkan adalah modularisasi lanjut beberapa fungsi, memperjelas argumen call fungsi, dan perbaikan sistem config.ini.
- Versi 1.0 menandai ketika program telah selesai menjalani **pengumpulan laporan** yang berarti telah menjalani proses debug minimum, pemberian komentar pada sebagian besar kode, dan kode yang masih rumit.
- Diharapkan ketika versi 1.0 minimal program dapat berjalan dengan normal dalam konstrain yang diberikan oleh spesifikasi tugas.

## Snapshot
**Load File** \
![Load File](/package/images/loadfile.gif) \
**Main Menu** \
![Main Menu](/package/images/mainmenu.gif)

## Informasi Dasar
Data | Isi
---- | ---
Tahun Ajaran    | 2020
Tanggal Mulai   | 4 April 2020
Tanggal Selesai | 27 April 2020
Kelas           | 05
Dosen           | Dicky Prima Satya
Asisten         | Yoel Susanto - 13517014
Kelompok        | 13

**Anggota Kelompok**
NIM      | Nama
---      | ----
16519125 | Finna Alivia Nabila
16519205 | Kevin Domenico Tantiyo
16519515 | Hizkia Raditya Pratama Roosadi
16519525 | Tanur Rizaldi Rahardjo

**Dependencies**
Komponen | Menggunakan
-------- | -----------
Python   | 3.7.2
Library  | hashlib

**Database (Default)**
Database | Menggunakan
-------- | -----------
Nmax     | 100
Mark     | "\~\~\~"

## Modul
**Status : Done** :white_check_mark: \
**16 / 16**
Modul | Status
----- | ------
Load               | :white_check_mark:
Login              | :white_check_mark:
Save               | :white_check_mark:
Sign Up            | :white_check_mark:
Pencarian Pemain   | :white_check_mark:
Pencarian Wahana   | :white_check_mark:
Pembelian Tiket    | :white_check_mark:
Menggunakan Tiket  | :white_check_mark:
Refund             | :white_check_mark:
Kritik & Saran     | :white_check_mark:
Baca Kritik        | :white_check_mark:
Tambah Wahana      | :white_check_mark:
Top Up             | :white_check_mark:
Baca Riwayat       | :white_check_mark:
Baca Tiket         | :white_check_mark:
Exit               | :white_check_mark:

### Bonus
**Status : Done** :white_check_mark: \
**4 / 4**
Modul | Status
----- | ------
Hash & Salt        | :white_check_mark:
Upgrade Gold       | :white_check_mark:
Best Wahana        | :white_check_mark:
Laporan Kehilangan | :white_check_mark:

## Laporan dan Finishing
**Status : Done**
To Do | Status
----- | ------
Debug              | :white_check_mark:
Pemberian Komentar | :white_check_mark:
Pembersihan kode   | :white_check_mark:
Laporan            | :white_check_mark:
Demonstrasi        | :white_check_mark:
