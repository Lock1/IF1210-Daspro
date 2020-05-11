############################## Informasi Modul ##############################
## Modul kritiksaran
# Desainer
# Hizkia R. / 16519515 / 22 April 2020

# Coder
# Hizkia R. / 16519515 / 22 April 2020

# Tester
# Tanur Rizaldi Rahardjo / 16519525 / 23 April 2020

######### Kamus #########
### Argumen yang direquest oleh fungsi
# username      : String
# kritiksaran   : 2D Matrix of strings
# N             : Integer

### Kamus Internal
# kritikID       : String           {ID wahana yang dikritik}
# tanggalKritik  : String           {Tanggal kritik dan saran diterima}
# isiKritik      : String           {Isi kritik dan saran}
# kritikBaru     : Array of string  {Array kritikBaru untuk database kritiksaran}

### Kamus informasi yang direturn
# kritiksaran   : 2D Matrix of strings

###### Spesifikasi ######
# tulisKritikSaran  : (String, 2D Matrix of strings, Integer) -> (2D Matrix of strings)
#############################################################################

############################### Algoritma ################################
from package.base import *

def tulisKritikSaran(username,kritiksaran,wahana,N=Nmax):
    # Input ketiga parameter kritik dan saran baru
    kritikID = idInput("Masukkan ID Wahana: ")
    while not isExistOnDatabase(wahana,0,kritikID):
        kritikID = idInput("ID tidak ada pada database, masukkan ID valid: ")
    tanggalKritik = dateInput("Masukkan tanggal pelaporan: ")
    isiKritik = input("Kritik/saran Anda: ")

    # Menyimpan ketiga parameter ke satu array
    kritikBaru = [username, tanggalKritik, kritikID, isiKritik]

    # Menulis array tersebut ke row baru didatabase
    kritiksaran = appendDatabase(kritiksaran,kritikBaru)
    print("Kritik dan saran Anda kami terima")

    print()
    return kritiksaran

########################### End of function ##############################
