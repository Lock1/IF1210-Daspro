############################## Informasi Modul ##############################
## Modul cariwahana
# Desainer
# Hizkia R. / 16519515 / 12 April 2020

# Coder
# Hizkia R. / 16519515 / 12 April 2020

# Tester
# Tanur Rizaldi Rahardjo / 16519525 / 17 April 2020

######### Kamus #########
### Argumen yang direquest oleh fungsi
# user      : 2D Matrix of string
# N         : Integer

### Kamus Internal
# batasTinggi        : Integer   {Batas tinggi}
# batasUmur          : Integer   {Batas umur}
# umurFind           : String
# N                  : Integer
# pencarianDitemukan : Boolean

###### Spesifikasi ######
# cariDanPrintWahana : (2D Matrix of string, String, Function, Integer) -> (Boolean)
# searchWahana       : (2D Matrix of string, Integer) -> ()
#############################################################################

############################### Algoritma ################################
from package.base import *

def cariDanPrintWahana(wahana,umurFind,fungsiCek,N=Nmax):
    pencarianDitemukan = False
    for i in range(N):
        if (wahana[i][3] == umurFind) and fungsiCek(int(wahana[i][4]),170):
            print("{:6} | {:30} | {:10}".format(wahana[i][0],wahana[i][1],wahana[i][2]))
            pencarianDitemukan = True
    return pencarianDitemukan

def searchWahana(wahana,N=Nmax):
    # General interface agar pengguna tahu apa yang harus diinput
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
    batasUmur = posIntInput("Batasan umur pemain : ")
    while (batasUmur not in [1,2,3]):
        print("Batasan umur tidak valid!")
        batasUmur = posIntInput("Batasan umur pemain: ")

    batasTinggi = posIntInput("Batasan tinggi badan : ")
    while (batasTinggi not in [1,2]):
        print("Batasan tinggi tidak valid! ")
        batasTinggi = posIntInput("Batasan tinggi pemain: ")
    print()

    # Algoritma untuk menghasilkan hasil search sesuai pilihan kategori
    print("Hasil pencarian:")
    # Pembuatan argumen search dengan input yang dimasukkan
    if (batasUmur == 1):
        umurFind = "anak-anak"
    elif (batasUmur == 2):
        umurFind = "dewasa"
    else:
        umurFind = "semua umur"

    # Pemanggilan fungsi cariDanPrintWahana dengan fungsi lambda
    if (batasTinggi == 1):
        pencarianDitemukan = cariDanPrintWahana(wahana,umurFind,(lambda a, b: a >= b))
    else:
        pencarianDitemukan = cariDanPrintWahana(wahana,umurFind,(lambda a, b: True))

    # Penulisan ketika tidak ada data yang ditemukan
    if not pencarianDitemukan:
        print("Tidak ada wahana yang sesuai dengan pencarian anda.")
    print()

########################### End of function ##############################
