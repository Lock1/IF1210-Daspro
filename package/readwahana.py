############################## Informasi Modul ##############################
## Modul readwahana
# Desainer
# Hizkia R. / 16519515 / 20 April 2020

# Coder
# Hizkia R. / 16519515 / 20 April 2020

# Tester
# Tanur Rizaldi Rahardjo / 16519525 / 20 April 2020


## Kamus
# pencarianDitemukan {Status apakah ada wahana didatabase}: boolean
# riwayatWahanaID {ID Wahana yang akan dicari}: string


## Spesifikasi


#############################################################################

####### Algoritma #######
from package.base import *

def cariDanPrintRiwayatWahana(penggunaan,riwayatWahanaID,N):
    pencarianDitemukan = False
    for i in range(N):
        if (penggunaan[i][2] == riwayatWahanaID):
            print("{:10} | {:17} | {:3}".format(penggunaan[i][1],penggunaan[i][0],penggunaan[i][2]))
            pencarianDitemukan = True
    return pencarianDitemukan

def riwayatWahana(penggunaan,N=Nmax):
    riwayatWahanaID = input("Masukkkan ID Wahana: ")
    pencarianDitemukan = cariDanPrintRiwayatWahana(penggunaan,riwayatWahanaID,N)
    if not pencarianDitemukan:
        print("Maaf, ID yang anda masukkan salah atau riwayat kosong")
    print()
