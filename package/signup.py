# Modul signup
# Desainer
# Kevin Domenico Tantiyo / 16519205 / 18 April 2020

# Coder
# Kevin Domenico Tantiyo / 16519205 / 18 April 2020

# Tester
#

####### Algoritma #######
from package.base import *

def signup(user,N):
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
    isUsernameValid = False
    for i in range(N):
        if (playerUsername != tiket[i][3]):
            isUsernameValid = True
            break
    while not isUsernameValid:
        rawPrint("Username sudah digunakan, masukan username lain: ")
        playerUsername = input()
        for i in range(N):
        if (playerUsername != tiket[i][3]):
            isUsernameValid = True
            break
    #Penulisan interface lanjutan
    rawPrint("Masukkan password pemain: ")
    playerPassword = input()
    playerRole = "pemain"
    playerSaldo = 0
    playerGold = 0
    # Penulisan informasi baru
    print()
    print("Selamat menjadi pemain, "+str(playerName)+". Selamat bermain.")
    for i in range (N):
        if (user[i][0] == "~~~"):
            user[i] = [playerName, playerBornDay, playerHeight, playerUsername, playerPassword, playerRole, playerSaldo, playerGold]
            if (i!=N):
                user[i+1][0] = "~~~"
            break
    print()
    return(user)
