############################## Informasi Modul ##############################
# Modul login
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

def login(user,N):
    isPasswordBenar = False
    while not isPasswordBenar:
        rawPrint("Masukkan username: ")
        inputUsername = input()
        rawPrint("Masukkan password: ")
        inputPassword = input()
        print()
        ##### Pengecekan Password #####
        # Pencarian informasi pada database
        inputPassword = hash(inputUsername, inputPassword)
        for i in range(N):
            if (inputUsername, inputPassword) == (user[i][3], user[i][4]):
                isPasswordBenar = True
                nama, username, role, status = user[i][0], user[i][3], user[i][5], user[i][7]
                break
        # Penulisan pada layar ketika password salah
        if not isPasswordBenar:
            print("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi!")
        ##### Akhir bagian pengecekan #####

    # Pengkonversian informasi ke boolean
    admin, gold = False, False
    if (role == "Admin"):
        admin = True
    if (status == "1"):
        gold = True

    print("Selamat bersenang-senang, {}!".format(nama))
    print()
    return (nama, username, admin, gold)
