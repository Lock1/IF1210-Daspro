############################## Informasi Modul ##############################
## Modul topup
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

def requestTopUp(user,N=Nmax):
    balanceUsername = input("Masukkan username: ")
    addBalance = intinput("Masukkan saldo yang di-top up: ")
    (usernameExist, usernameIndex) = isExistOnDatabase(user,3,balanceUsername,N,False,True)
    if usernameExist:
        balance = int(user[usernameIndex][6]) + addBalance
        user[usernameIndex][6] = str(balance)
        print("Top up berhasil. Saldo {} bertambah menjadi {}".format(user[usernameIndex][0], balance))
    else:
        print("Maaf username {} tidak ditemukan".format(balanceUsername))

    print()
    return user
