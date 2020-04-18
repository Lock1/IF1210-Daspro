# Modul addwahana
# Desainer
# Tanur Rizaldi Rahardjo / 16519525 / 17 April 2020

# Coder
# Tanur Rizaldi Rahardjo / 16519525 / 17 April 2020

# Tester
#

####### Algoritma #######
from package.base import *

def tambahWahana(wahana,N):
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
    for i in range(N):
        if (wahana[i][0] == "~~~"):
            wahana[i] = [newID,newName,newCost,newAge,newHeight]
            if (i != N):
                wahana[i+1][0] = "~~~"
            break
    return wahana
    # End of function
