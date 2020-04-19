############################## Informasi Modul ##############################
## Modul cariwahana
# Desainer
# Hizkia R. / 16519515 / 12 April 2020

# Coder
# Hizkia R. / 16519515 / 12 April 2020

# Tester
# Tanur Rizaldi Rahardjo / 16519525 / 17 April 2020


## Kamus
# batasTinggi {Batas tinggi}: integer
# batasUmur {Batas umur}: integer


## Spesifikasi


#############################################################################

####### Algoritma #######
# General interface agar pengguna tahu apa yang harus diinput
from package.base import *

def wahanaPrint(id,nama,harga):
    print("{:6} | {:30} | {:10}".format(id,nama,harga))

def cariDanPrintWahana(wahana,umurFind,fungsiCek,N):
    pencarianDitemukan = False
    for i in range(N):
        if (wahana[i][3] == umurFind) and fungsiCek(int(wahana[i][4]),170):
            wahanaPrint(wahana[i][0],wahana[i][1],wahana[i][2])
            pencarianDitemukan = True
    return pencarianDitemukan

def searchWahana(wahana,N):
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
    # Pencarian
    if (batasUmur == 1):
        umurFind = "anak-anak"
    elif (batasUmur == 2):
        umurFind = "dewasa"
    else:
        umurFind = "semua umur"

    if (batasTinggi == 1):
        pencarianDitemukan = cariDanPrintWahana(wahana,umurFind,(lambda a, b: a >= b),N)
    else:
        pencarianDitemukan = cariDanPrintWahana(wahana,umurFind,(lambda a, b: True),N)

    # Penulisan ketika tidak ada data yang ditemukan
    if not pencarianDitemukan:
        print("Tidak ada wahana yang sesuai dengan pencarian anda.")
    print()
