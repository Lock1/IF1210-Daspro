############################## Informasi Modul ##############################
## Modul caripemain
# Desainer
# Finna Alivia Nabila  / 16519125 / 24 April 2020

# Coder
# Finna Alivia Nabila / 16519125 / 24 April 2020

# Tester
# Hizkia R. / 16519515 / 26 April 2020

######### Kamus #########
### Argumen yang direquest oleh fungsi
# user      : Matrix of string
# N         : Integer

### Kamus Internal
# searchUsername    : String
# usernameExist     : Boolean
# usernameIndex     : Integer

###### Spesifikasi ######
# searchPemain  : (2D Matrix of string, Integer) -> ()
#############################################################################

############################### Algoritma ################################
from package.base import *

def searchPemain(user,N=Nmax):
    # Input username
    searchUsername = input("Masukkan username: ")
    # Pencarian username pada database, jika ada minta indeks username terkait
    (usernameExist, usernameIndex) = isExistOnDatabase(user,3,searchUsername,N,False,True)
    if usernameExist:
        # Pengeprintan informasi username yang dicari
        print("Nama Pemain: {}".format(user[usernameIndex][0]))
        print("Tinggi Pemain: {}".format(user[usernameIndex][2]))
        print("Tanggal Lahir Pemain: {}".format(user[usernameIndex][1]))

    print()

########################### End of function ##############################
