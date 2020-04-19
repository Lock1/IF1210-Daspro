############################## Informasi Modul ##############################
# Modul signup
# Desainer
# Kevin Domenico Tantiyo / 16519205 / 18 April 2020

# Coder
# Kevin Domenico Tantiyo / 16519205 / 18 April 2020

# Tester
#


## Kamus


## Spesifikasi


#############################################################################
####### Algoritma #######
from package.base import *

def cekUsername(user,username,N):
    isUsernameValid = True
    for i in range(N):
        if (user[i][0] == "~~~"):
            break
        if (user[i][3] == username):
            isUsernameValid = False
            break
    return isUsernameValid

def signUpUser(user,N):
    # Penulisan interface
    print()
    rawPrint("Masukkan nama pemain: ")
    playerName = input()                                        # INama
    rawPrint("Masukkan tanggal lahir pemain (DD/MM/YYYY): ")
    playerBornDay = input()                                     # Tanggal Lahir
    rawPrint("Masukkan tinggi badan pemain (cm): ")
    playerHeight = input()                                      # Tinggi
    rawPrint("Masukkan username pemain: ")
    playerUsername = input()                                    # Username
    # Pengecekan username
    isUsernameValid = cekUsername(user,playerUsername,N)
    while not isUsernameValid:
        rawPrint("Username sudah digunakan, masukan username lain: ")
        playerUsername = input()
        isUsernameValid = cekUsername(user,playerUsername,N)
    # Penulisan interface lanjutan
    rawPrint("Masukkan password pemain: ")
    playerPassword = input()                                    # Password
    playerPassword = hash(playerUsername,playerPassword)
    playerRole = "Pemain"                                       # Role
    playerSaldo = "0"                                           # Saldo
    playerGold = "0"                                            # Status Gold
    # Penulisan informasi baru
    print()
    print("Selamat menjadi pemain, {}. Selamat bermain.".format(playerName))
    for i in range(N):
        if (user[i][0] == "~~~"):
            user[i] = [playerName, playerBornDay, playerHeight, playerUsername, playerPassword, playerRole, playerSaldo, playerGold]
            if (i != N):
                user[i+1][0] = "~~~"
            break
    print()
    return(user)
