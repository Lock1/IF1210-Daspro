# Modul signup
# Desainer
# Kevin Domenico Tantiyo / 16519205 / 18 April 2020

# Coder
# Kevin Domenico Tantiyo / 16519205 / 18 April 2020

# Tester
#

####### Algoritma #######
from package.base import *
from package.login import *

def signUpUser(user,N):
    # Penulisan interface
    print()
    rawPrint("Masukkan nama pemain: ")
    playerName = input()
    rawPrint("Masukkan tanggal lahir pemain (DD/MM/YYYY): ")
    playerBornDay = input()
    rawPrint("Masukkan tinggi badan pemain (cm): ")
    playerHeight = input()
    rawPrint("Masukkan username pemain: ")
    playerUsername = input()
    # Pengecekan username
    isUsernameValid = True
    for i in range(N):
        if (user[i][0] == "~~~"):
            break
        if (user[i][3] == playerUsername):
            isUsernameValid = False
            break
    while not isUsernameValid:
        rawPrint("Username sudah digunakan, masukan username lain: ")
        playerUsername = input()
        for i in range(N):
            if (user[i][0] == "~~~"):
                isUsernameValid = True
                break
            if (user[i][3] == playerUsername):
                break
    # Penulisan interface lanjutan
    rawPrint("Masukkan password pemain: ")
    playerPassword = input()
    playerPassword = hash(playerUsername,playerPassword)
    playerRole = "Pemain"
    playerSaldo = "0"
    playerGold = "0"
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
