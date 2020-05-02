############################## Informasi Modul ##############################
## Modul readwahana
# Desainer
# Hizkia R. / 16519515 / 20 April 2020

# Coder
# Hizkia R. / 16519515 / 20 April 2020

# Tester
# Tanur Rizaldi Rahardjo / 16519525 / 20 April 2020

######### Kamus #########
### Argumen yang direquest oleh fungsi
# penggunaan    : 2D Matrix of string
# N             : Integer

### Kamus Internal
# riwayatWahanaID       : String  {ID Wahana yang akan dicari}
# pencarianDitemukan    : Boolean {Status apakah ada wahana didatabase}

###### Spesifikasi ######
# cariDanPrintRiwayatWahana     : (2D Matrix of strings, String, Integer) -> (Boolean)
# riwayatWahana                 : (2D Matrix of strings, Integer) -> ()
#############################################################################

############################### Algoritma ################################
from package.base import *

def cariDanPrintRiwayatWahana(penggunaan,riwayatWahanaID,N=Nmax):
    pencarianDitemukan = False
    # Loop pencarian, jika ditemukan ID wahana yang sama print informasi pada baris terkait
    for i in range(N):
        if (penggunaan[i][2] == riwayatWahanaID):
            print("{:10} | {:17} | {:3}".format(penggunaan[i][1],penggunaan[i][0],penggunaan[i][2]))
            pencarianDitemukan = True
    return pencarianDitemukan

def riwayatWahana(penggunaan,N=Nmax):
    # Input user untuk mencari wahana pada database penggunaan
    riwayatWahanaID = idInput("Masukkkan ID Wahana: ")
    pencarianDitemukan = cariDanPrintRiwayatWahana(penggunaan,riwayatWahanaID)
    if not pencarianDitemukan:
        print("Maaf, ID yang anda masukkan salah atau riwayat kosong")
    print()

########################### End of function ##############################
