############################## Informasi Modul ##############################
# Modul addwahana
# Desainer
# Tanur Rizaldi Rahardjo / 16519525 / 17 April 2020

# Coder
# Tanur Rizaldi Rahardjo / 16519525 / 17 April 2020

# Tester
#


## Kamus


## Spesifikasi


#############################################################################
####### Algoritma #######
from package.base import *

def tambahWahana(wahana,N=Nmax):
    # Meminta input user
    print("Masukkan Informasi Wahana yang ditambahkan:")
    rawPrint("Masukkan ID Wahana: ")
    newID = input()
    rawPrint("Masukkan Nama Wahana: ")
    newName = input()
    rawPrint("Masukkan Harga Tiket: ")
    newCost = input()
    rawPrint("Batasan umur: ")
    newAge = input()
    rawPrint("Batasan tinggi badan: ")
    newHeight = input()
    print()
    print("Info wahana telah ditambahkan!")
    # Update array wahana dengan wahana baru
    wahanaBaru = [newID,newName,newCost,newAge,newHeight]
    wahana = appendDatabase(wahana,wahanaBaru,N)
    return wahana
    # End of function
