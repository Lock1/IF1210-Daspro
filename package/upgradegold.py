############################## Informasi Modul ##############################
# Modul upgradegold
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

def upgradeToGold(gold,user,upgradeGoldCost,N=Nmax):
    # Interface
    upgradeUsername = input("Masukkan username yang ingin di-upgrade: ")
    print()

    # Pencarian pada database dan penggantian status gold
    # jika memenuhi persyaratan saldo username >= upgradeGoldCost
    isUsernameExist, upgradeIndex = isExistOnDatabase(user,3,upgradeUsername,N,False,True)
    if isUsernameExist:
        if (int(user[upgradeIndex][6]) >= upgradeGoldCost):
            user[upgradeIndex][6] = str(int(user[upgradeIndex][6]) - upgradeGoldCost) # SALDO DECREASE
            user[upgradeIndex][7] = "1"
            gold = True
            print("Akun anda telah diupgrade.")
        elif (int(user[upgradeIndex][6]) >= upgradeGoldCost) and (user[upgradeIndex][7] == "1"):
            print("Username {} sudah memiliki Gold membership".format(upgradeUsername))
        else:
            print("Username tidak ditemukan atau saldo tidak mencukupi.")

    print()
    return (user, gold)
