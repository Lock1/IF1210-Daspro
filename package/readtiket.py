############################## Informasi Modul ##############################
# Modul readtiket
# Desainer
# Kevin Domenico Tantiyo / 16519205 / 24 April 2020

# Coder
# Kevin Domenico Tantiyo / 16519205 / 24 April 2020

# Tester
# Finna Alivia Nabila / 16519125 / 26 April 2020

######### Kamus #########
### Argumen yang direquest oleh fungsi

### Kamus Internal
# findUsername  : String
# searchFound   : Boolean

###### Spesifikasi ######
# cariDanPrintTiket : (2D Matrix of strings, 2D Matrix of strings, String, Integer) -> ()
# adminReadTicket   : (2D Matrix of strings, 2D Matrix of strings, Integer) -> ()
#############################################################################

############################### Algoritma ################################
from package.base import *

def cariDanPrintTiket(tiket,wahana,findUsername,N):
    pencarianDitemukan = False
    # Penyimpanan sementara
    wahanaIDList = ["" for i in range(N)]
    wahanaTiketList = ["" for i in range(N)]
    j = 0
    # Pencarian tiket dengan username "findUsername" pada database tiket
    for i in range(N):
        if (tiket[i][0] == findUsername):
            if (not pencarianDitemukan):
                print("Riwayat:")
            wahanaIDList[j] = tiket[i][1]
            wahanaTiketList[j] = tiket[i][2]
            pencarianDitemukan = True
            j += 1
    # Pengeprintan terbalik dengan pada array sementara
    while (j >= 0):
        (isWahanaExist, wahanaIndex) = isExistOnDatabase(wahana,0,wahanaIDList[j],N,False,True)
        if isWahanaExist:
            print("{:6} | {:30} | {}".format(wahanaIDList[j],wahana[wahanaIndex][1],wahanaTiketList[j]))
        j -= 1
    return pencarianDitemukan

def adminReadTicket(tiket,wahana,N=Nmax):
    # Input user
    findUsername = input("Masukkan username: ")
    # Pencarian dan pengeprintan tiket terkait
    searchFound = cariDanPrintTiket(tiket,wahana,findUsername,N)
    if not searchFound:
        print("Pencarian tidak ditemukan")
    print()

########################### End of function ##############################
