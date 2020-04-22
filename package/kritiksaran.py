############################## Informasi Modul ##############################
## Modul kritiksaran
# Desainer
# Hizkia R. / 16519515 / 22 April 2020

# Coder
# Hizkia R. / 16519515 / 22 April 2020

# Tester
# Tanur Rizaldi Rahardjo / 16519525 / 23 April 2020


## Kamus
# kritikID       : String (ID wahana yang dikritik)
# tanggalKritik  : String (Tanggal kritik dan saran diterima)
# isiKritik      : String (Isi kritik dan saran)
# kritikBaru     : Array kritikBaru untuk database kritiksaran


## Spesifikasi


#############################################################################

####### Algoritma #######
from package.base import *

def tulisKritikSaran(kritiksaran,N=Nmax):
    # Input ketiga parameter kritik dan saran baru
    rawPrint("Masukkan ID Wahana: ")
    kritikID = input()
    rawPrint("Masukkan tanggal pelaporan: ")
    tanggalKritik = input()
    rawPrint("Kritik/saran Anda: ")
    isiKritik = input()

    # Menyimpan ketiga parameter ke satu array
    kritikBaru = [kritikID, tanggalKritik, isiKritik]
    # Menulis array tersebut ke row baru didatabase
    kritiksaran = appendDatabase(kritiksaran,kritikBaru,N)
    print("Kritik dan saran Anda kami terima")
    return kritiksaran
