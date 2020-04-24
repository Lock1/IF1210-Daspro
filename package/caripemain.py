############################## Informasi Modul ##############################
## Modul caripemain
# Desainer
# Finna Alivia Nabila  / 16519125 / 24 April 2020

# Coder
# Finna Alivia Nabila / 16519125 / 24 April 2020

# Tester
#


## Kamus



## Spesifikasi


#############################################################################

####### Algoritma #######
from package.base import *

def searchPemain(user,N=Nmax):
    searchUsername = input("Masukkan username: ")
    (usernameExist, usernameIndex) = isExistOnDatabase(user,3,searchUsername,N,False,True)
    if usernameExist:
        print("Nama Pemain: {}".format(user[usernameIndex][0]))
        print("Tinggi Pemain: {}".format(user[usernameIndex][2]))
        print("Tanggal Lahir Pemain: {}".format(user[usernameIndex][1]))

    print()
