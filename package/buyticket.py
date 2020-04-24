############################## Informasi Modul ##############################
# Modul buytiket
# Desainer
# Kevin Domenico Tantiyo / 16519205 / 24 April 2020

# Coder
# Kevin Domenico Tantiyo / 16519205 / 24 April 2020

# Tester
# Tanur Rizaldi Rahardjo / 16519525 / 24 April 2020


## Kamus


## Spesifikasi


#############################################################################
####### Algoritma #######
from package.base import *
from datetime import date

def buyticket():
    #Penulisan interface
    print()
    rawPrint("Masukkan ID wahana: ")
    idWahana=input()
    rawPrint("Masukkan tanggal hari ini: ")
    tanggal=input()
    rawPrint=("Jumlah tiket yang dibeli: ")
    jumlahTiket=input()
    umur = (tanggal.year)-(username.Tanggal_Lahir.year)
    if (username.Tanggal_Lahir.date>=tanggal.date) and (username.Tanggal_Lahir.month>=tanggal.month):
        umur=umur
    else:
        umur=umur-1
    if (username.Tinggi_Badan<wahana.Batasan_tinggi) or (umur<wahana.Batasan_Umur)
        print("Anda tidak memenuhi persyaratan untuk memainkan wahana ini.")
        print("Silakan menggunakan wahana lain yang tersedia.")
    else:
        if (username.saldo<(wahana.Harga_Tiket*jumlahTiket)):
            print("Saldo Anda tidak cukup")
            print("Silakan mengisi saldo Anda")
        else:
            print("Selamat bersenang-senang di "+str(wahana.Nama_Wahana))
