############################## Informasi Modul ##############################
## Modul topup
# Desainer
# Finna Alivia Nabila  / 16519125 / 24 April 2020

# Coder
# Finna Alivia Nabila / 16519125 / 24 April 2020

# Tester
# Tanur Rizaldi Rahardjo / 16519525 / 26 April 2020

######### Kamus #########
### Argumen yang direquest oleh fungsi
# user      : 2D Matrix of string
# N         : Integer

### Kamus Internal
# balanceUsername      : String
# addBalance           : Integer
# isUsernameExist      : Boolean
# usernameTopUpIndex   : Integer
# newBalance           : Integer

### Kamus informasi yang direturn
# user      : 2D Matrix of string

###### Spesifikasi ######
# requestTopUp  : (2D Matrix of string, Integer) -> (2D Matrix of string)
#############################################################################

############################### Algoritma ################################
from package.base import *

def requestTopUp(user,N=Nmax):
    # Input informasi yang dibutuhkan
    balanceUsername = input("Masukkan username: ")
    addBalance = posIntInput("Masukkan saldo yang di-top up: ")

    # Pencarian username pada database user
    isUsernameExist, usernameTopUpIndex = isExistOnDatabase(user,3,balanceUsername,True)
    if isUsernameExist:
        # Penggantian saldo ketika ditemukan username
        newBalance = int(user[usernameTopUpIndex][6]) + addBalance
        user = replaceColumn(user,usernameTopUpIndex,[6,newBalance])
        print("Top up berhasil. Saldo {} bertambah menjadi {}".format(user[usernameTopUpIndex][0], newBalance))
    else:
        print("Maaf username {} tidak ditemukan".format(balanceUsername))

    # Returning print
    print()
    return user

########################### End of function ##############################
