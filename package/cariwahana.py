# Modul cariwahana
# Desainer
# Hizkia R. / 16519515 / 12 April 2020

# Coder
# Hizkia R. / 16519515 / 12 April 2020

# Tester
# Tanur Rizaldi Rahardjo / 16519525 / 17 April 2020


# Kamus
# batasTinggi {Batas tinggi}: integer
# batasUmur {Batas umur}: integer


# General interface agar pengguna tahu apa yang harus diinput
from package.base import *

def wahanaprint(id,nama,harga):
    print("{:6} | {:30} | {:10}".format(id,nama,harga))

def cariwahana(wahana,N):
    # Menuliskan tampilan menu pencarian
    print()
    print("Jenis batasan umur : ")
    print("1. {:9} (<17 tahun)".format("Anak-anak"))
    print("2. {:9} (>=17 tahun)".format("Dewasa"))
    print("3. Semua umur")
    print()
    print("Jenis batasan tinggi badan : ")
    print("1. Lebih dari 170 cm")
    print("2. Tanpa batasan")
    print()


    # Algoritma menyaring input
    batasUmur = intinput("Batasan umur pemain : ")
    if (batasUmur not in [1,2,3]):
        while (batasUmur not in [1,2,3]):
            print("Batasan umur tidak valid!")
            batasUmur = intinput("Batasan umur pemain: ")

    batasTinggi = intinput("Batasan tinggi badan : ")
    if (batasTinggi not in [1,2]):
        while (batasTinggi not in [1,2]):
            print("Batasan tinggi tidak valid! ")
            batasTinggi = intinput("Batasan tinggi pemain: ")
    print()

    # Algoritma untuk menghasilkan hasil search sesuai pilihan kategori
    print("Hasil pencarian:")
    pencarianDitemukan = False
    # Loop pencarian

    for i in range(N):
        if (batasUmur,batasTinggi) == (1,1):
            if (wahana[i][3] == "anak-anak") and (int(wahana[i][4]) >= 170):
                wahanaprint(wahana[i][0],wahana[i][1],wahana[i][2])
                pencarianDitemukan = True

        elif (batasUmur,batasTinggi) == (1,2):
            if (wahana[i][3] == "anak-anak"):
                wahanaprint(wahana[i][0],wahana[i][1],wahana[i][2])
                pencarianDitemukan = True

        elif (batasUmur,batasTinggi) == (2,1):
            if (wahana[i][3] == "dewasa") and (int(wahana[i][4]) >= 170):
                wahanaprint(wahana[i][0],wahana[i][1],wahana[i][2])
                pencarianDitemukan = True

        elif (batasUmur,batasTinggi) == (2,2):
            if (wahana[i][3] == "dewasa"):
                wahanaprint(wahana[i][0],wahana[i][1],wahana[i][2])
                pencarianDitemukan = True

        elif (batasUmur,batasTinggi) == (3,1):
            if (wahana[i][3] == "semua umur") and (int(wahana[i][4]) >= 170):
                wahanaprint(wahana[i][0],wahana[i][1],wahana[i][2])
                pencarianDitemukan = True

        elif (batasUmur,batasTinggi) == (3,2):
            if (wahana[i][3] == "semua umur"):
                wahanaprint(wahana[i][0],wahana[i][1],wahana[i][2])
                pencarianDitemukan = True

    # Penulisan ketika tidak ada data yang ditemukan
    if not pencarianDitemukan:
        print("Tidak ada wahana yang sesuai dengan pencarian anda.")
    print()
