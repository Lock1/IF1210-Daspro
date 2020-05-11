############################## Informasi Modul ##############################
## Modul signup
# Desainer
# Kevin Domenico Tantiyo / 16519205 / 18 April 2020

# Coder
# Kevin Domenico Tantiyo / 16519205 / 18 April 2020

# Tester
# Finna Alivia Nabila / 16519125 / 26 April 2020

######### Kamus #########
### Argumen yang direquest oleh fungsi
# user      : 2D Matrix of string
# N         : Integer

### Kamus Internal
# playerName        : String
# playerBornDay     : String
# playerHeight      : String
# playerUsername    : String
# playerPassword    : Strings
# playerRole        : Strings
# playerSaldo       : Strings
# playerGold        : Strings
# newPlayer         : Array of strings

### Kamus informasi yang direturn
# user      : 2D Matrix of string

###### Spesifikasi ######
# signUpUser        : (2D Matrix of strings, Integer) -> (2D Matrix of strings)
#############################################################################

############################### Algoritma ################################
from package.base import *

def signUpUser(user,N=Nmax):
    # Penulisan interface dan input data
    print()
    playerName = input("Masukkan nama pemain: ")                                   # Nama
    playerBornDay = dateInput("Masukkan tanggal lahir pemain (DD/MM/YYYY): ")      # Tanggal Lahir
    playerHeight = str(posIntInput("Masukkan tinggi badan pemain (cm): "))         # Tinggi
    playerUsername = input("Masukkan username pemain: ")                           # Username

    # Pengecekan username
    while isExistOnDatabase(user,3,playerUsername):
        playerUsername = input("Username sudah digunakan, masukan username lain: ")

    # Penulisan interface lanjutan
    playerPassword = input("Masukkan password pemain: ")                           # Password

    # Setting informasi default untuk pemain baru
    playerPassword = hash(playerUsername,playerPassword)
    playerRole = "Pemain"                                       # Role
    playerSaldo = "0"                                           # Saldo
    playerGold = "0"                                            # Status Gold

    # Penulisan informasi baru
    newPlayer = [playerName, playerBornDay, playerHeight, playerUsername, playerPassword, playerRole, playerSaldo, playerGold]
    user = appendDatabase(user,newPlayer)

    # Returning print
    print()
    print("Selamat menjadi pemain, {}. Selamat bermain.".format(playerName))
    print()
    return user

########################### End of function ##############################
