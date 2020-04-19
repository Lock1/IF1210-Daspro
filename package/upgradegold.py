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

def upgradeToGold(user,upgradeGoldCost,N):
    # Interface
    rawPrint("Masukkan username yang ingin di-upgrade: ")
    upgradeUsername = input()
    print()
    # Pencarian pada database dan penggantian status gold
    # jika memenuhi persyaratan saldo username >= upgradeGoldCost
    upgradeGagal = False
    for i in range(N):
        if (user[i][0] == "~~~"):
            break
        if (user[i][3] == upgradeUsername):
            if (int(user[i][6]) >= upgradeGoldCost):
                user[i][7] = "1"
                print("Akun anda telah diupgrade.")
            elif (int(user[i][6]) >= upgradeGoldCost) and (user[i][7] == "1"):
                print("Username {} sudah memiliki Gold membership".format(upgradeUsername))
            else:
                upgradeGagal = True
            break
    if upgradeGagal:
        print("Username tidak ditemukan atau saldo tidak mencukupi.")
    print()
    return user
