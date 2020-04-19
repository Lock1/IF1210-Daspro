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

## Fungsi isUsernameValid
# Digunakan untuk mengecek apakah username sudah ada didatabase
# Jika sudah ada, return False
def isUsernameValid(user,username,N):
    isValid = True
    isValid = isExistOnDatabase(user,3,username,N,isValid)
    return isValid

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
    while not isUsernameValid(user,playerUsername,N):
        rawPrint("Username sudah digunakan, masukan username lain: ")
        playerUsername = input()
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
    newPlayer = [playerName, playerBornDay, playerHeight, playerUsername, playerPassword, playerRole, playerSaldo, playerGold]
    user = appendDatabase(user,newPlayer,N)
    print()
    return user
