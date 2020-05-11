############################## Informasi Modul ##############################
# Modul addwahana
# Desainer
# Tanur Rizaldi Rahardjo / 16519525 / 17 April 2020

# Coder
# Tanur Rizaldi Rahardjo / 16519525 / 17 April 2020

# Tester
# Finna Alivia Nabila / 16519125 / 26 April 2020

######### Kamus #########
### Argumen yang direquest oleh fungsi
# wahana    : 2D Matrix of string
# N         : Integer

### Kamus Internal
# newID             : String
# newName           : String
# newCost           : Integer {Dikonversi ke str ketika penyimpanan}
# newAge            : String
# newHeight         : Integer {Dikonversi ke str ketika penyimpanan}
# wahanaBaru        : Array of strings

### Kamus informasi yang direturn
# wahana    : 2D Matrix of string

###### Spesifikasi ######
# tambahWahana  : (2D Matrix of string, Integer) -> (2D Matrix of string)
#############################################################################

############################### Algoritma ################################
from package.base import *

def tambahWahana(wahana,N=Nmax):
    # Meminta input user
    print("Masukkan Informasi Wahana yang ditambahkan:")
    newID = idInput("Masukkan ID Wahana: ")
    while isExistOnDatabase(wahana,0,newID):
        newID = idInput("ID sudah terdaftar, masukkan ID lain: ")

    newName = input("Masukkan Nama Wahana: ")
    newCost = str(posIntInput("Masukkan Harga Tiket: "))
    newAge = umurInput("Batasan umur: ")
    newHeight = str(posIntInput("Batasan tinggi badan: "))

    # Update array wahana dengan wahana baru
    wahanaBaru = [newID,newName,newCost,newAge,newHeight]
    wahana = appendDatabase(wahana,wahanaBaru)
    print()

    print("Info wahana telah ditambahkan!")
    print()
    return wahana
    # End of function

########################### End of function ##############################
