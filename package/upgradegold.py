# Modul upgradegold
# Desainer
# Tanur Rizaldi Rahardjo / 16519525 / 17 April 2020

# Coder
# Tanur Rizaldi Rahardjo / 16519525 / 17 April 2020

# Tester
#


####### Algoritma #######


def upgradeToGold(user,upgradeGoldCost,N):
    # Interface
    print("Masukkan username yang ingin di-upgrade: ",end="")
    upUsername = input()
    print()
    # Pencarian pada database dan penggantian status gold
    # jika memenuhi persyaratan saldo username >= upgradeGoldCost
    upgradeGagal = False
    for i in range(N):
        if user[i][0] == "~~~":
            break
        if user[i][3] == upUsername:
            if int(user[i][6]) >= upgradeGoldCost:
                user[i][7] = "1"
                print("Akun anda telah diupgrade.")
            else:
                upgradeGagal = True
            break
    if upgradeGagal:
        print("Username tidak ditemukan atau saldo tidak mencukupi.")
    print()
    return user
