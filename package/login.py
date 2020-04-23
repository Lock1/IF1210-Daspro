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

def requestLogin(user,N=Nmax):
    isPasswordBenar = False
    while not isPasswordBenar:
        inputUsername = input("Masukkan username: ")
        inputPassword = input("Masukkan password: ")
        print()
        
        ##### Pengecekan Password #####
        # Pencarian informasi pada database
        inputPassword = hash(inputUsername, inputPassword)
        isUsernameExist, userInformationIndex = isExistOnDatabase(user,3,inputUsername,N,False,True)
        if isUsernameExist:
            if (user[userInformationIndex][4] == inputPassword):
                isPasswordBenar = True
                nama, username, role, status = user[userInformationIndex][0], user[userInformationIndex][3], user[userInformationIndex][5], user[userInformationIndex][7]
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
