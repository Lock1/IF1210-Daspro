# Modul fungsi cariwahana()
# Hizkia R. 16519515, 12 April 2020

# Kamus
# btsTinggi {Batas tinggi}: integer
# btsUmur {Batas umur}: integer

# General interface agar pengguna tahu apa yang harus diinput
from package.base import *

def wahanaprint(id,nama,harga):
    print("{:6} | {:20} | {:10}".format(id,nama,harga))

def cariwahana(wahana):
    # Menuliskan tampilan menu pencarian
    print("Jenis batasan umur : ")
    print("1. {:9} (<17 tahun)".format("Anak-anak"))
    print("2. {:9} (>=17 tahun)".format("Dewasa"))
    print("3. Semua umur")
    print()
    print("Jenis batasan tinggi badan :")
    print("1. Lebih dari 170 cm")
    print("2. Tanpa batasan")
    print()


    # Algoritma menyaring input
    btsUmur = xinput("Batasan umur pemain :")
    if (btsUmur not in ["1","2","3"]):
        while (btsUmur not in ["1","2","3"]):
            print("Batasan umur tidak valid!")
            btsUmur = xinput("Batasan umur pemain:")

    btsTinggi = xinput("Batasan tinggi badan :")
    if (btsTinggi not in ["1","2"]):
        while (btsTinggi not in ["1","2"]):
            print("Batasan tinggi tidak valid!")
            btsTinggi=xinput("Batasan tinggi pemain:")


    # Algoritma untuk menghasilkan hasil search sesuai pilihan kategori
    print("Hasil pencarian:")
    ketemu = False
    # Loop pencarian
    for i in range(99):
        if (btsUmur,btsTinggi) == ("1","1"):
            if wahana[3] == "anak-anak" and int(wahana[4]) >= 170:
                wahanaprint(wahana[0],wahana[1],wahana[2])
                ketemu = True

        elif (btsUmur,btsTinggi) == ("1","2"):
            if wahana[3] == "anak-anak":
                wahanaprint(wahana[0],wahana[1],wahana[2])
                ketemu = True

        elif (btsUmur,btsTinggi) == ("2","1"):
            if wahana[3] == "dewasa" and int(wahana[4]) >= 170:
                wahanaprint(wahana[0],wahana[1],wahana[2])
                ketemu = True

        elif (btsUmur,btsTinggi) == ("2","2"):
            if wahana[3] == "dewasa":
                wahanaprint(wahana[0],wahana[1],wahana[2])
                ketemu = True

        elif (btsUmur,btsTinggi) == ("3","1"):
            if int(wahana[4]) >= 170 and wahana[3] == "semua umur":
                wahanaprint(wahana[0],wahana[1],wahana[2])
                ketemu = True

        elif (btsUmur,btsTinggi) == ("3","2"):
            if wahana[3] == "semua umur":
                wahanaprint(wahana[0],wahana[1],wahana[2])
                ketemu = True
    # Penulisan ketika tidak ada data yang ditemukan
    if not ketemu:
        print("Tidak ada wahana yang sesuai dengan pencarian anda.")
        print()
