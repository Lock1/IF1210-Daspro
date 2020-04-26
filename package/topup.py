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
# balanceUsername   : String
# addBalance        : Integer
# usernameExist     : Boolean
# usernameIndex     : Integer

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
    addBalance = intinput("Masukkan saldo yang di-top up: ")
    # Pencarian username pada database user
    (usernameExist, usernameIndex) = isExistOnDatabase(user,3,balanceUsername,N,False,True)
    if usernameExist:
        # Penggantian saldo ketika ditemukan username
        balance = int(user[usernameIndex][6]) + addBalance
        user[usernameIndex][6] = str(balance)
        print("Top up berhasil. Saldo {} bertambah menjadi {}".format(user[usernameIndex][0], balance))
    else:
        print("Maaf username {} tidak ditemukan".format(balanceUsername))

    print()
    return user

########################### End of function ##############################
