############################## Informasi Modul ##############################
# Modul readtiket
# Desainer
# Kevin Domenico Tantiyo / 16519205 / 18 April 2020

# Coder
# Kevin Domenico Tantiyo / 16519205 / 18 April 2020

# Tester
#


## Kamus


## Spesifikasi


#############################################################################

####### Algoritma #######
from package.base import *

def cariDanPrintTiket(tiket,wahana,findUsername,N):
    pencarianDitemukan = False
    wahanaIDList = ["" for i in range(N)]
    wahanaTiketList = ["" for i in range(N)]
    j = 0
    for i in range(N):
        if (tiket[i][0] == findUsername):
            if (not pencarianDitemukan):
                print("Riwayat:")
            wahanaIDList[j] = tiket[i][1]
            wahanaTiketList[j] = tiket[i][2]
            pencarianDitemukan = True
            j += 1
    while (j >= 0):
        (isWahanaExist, wahanaIndex) = isExistOnDatabase(wahana,0,wahanaIDList[j],N,False,True)
        if isWahanaExist:
            print("{:6} | {:30} | {}".format(wahanaIDList[j],wahana[wahanaIndex][1],wahanaTiketList[j]))
        j -= 1
    return pencarianDitemukan

def adminReadTicket(tiket,wahana,N=Nmax):
    findUsername = input("Masukkan username: ")
    searchFound = cariDanPrintTiket(tiket,wahana,findUsername,N)
    if not searchFound:
        print("Pencarian tidak ditemukan")
    print()
