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
### Import fungsi hash untuk penulisan password

def signUpUser(user,N):
    ### <<< Edit 5
    # Penggunaan nama fungsi sebaiknya tidak sama dengan
    # nama modul (signup.py dan signup()) untuk mencegah error import
    
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
        """if (playerUsername != tiket[i][3]):"""
        # <<< Edit 1
        # 1. Database yang diminta oleh fungsi signup(user,N) adalah user
        # 2. Kalau digunakan playerUsername != user[i][3],
        #    jika playerUsername dengan user[0][3] sudah berbeda, for loop akan
        #    terbreak dan sudah dianggap valid, meskipun username index 1,2,3,..
        #    belum dicek semua
        if (user[i][0] == "~~~"):
            break
        if (user[i][3] == playerUsername):
            isUsernameValid = False
            break
        # >>> Revisi 1
        # Digunakan pengecekan for loop user[i][3] apakah sama dengan playerUsername.
        # Base casenya adalah isUsernameValid benar, dan hanya berganti menjadi salah
        # ketika ada kesamaan antara playerUsername dan user[i][3] yang berarti username sudah ada
    while not isUsernameValid:
        rawPrint("Username sudah digunakan, masukan username lain: ")
        playerUsername = input()
        """for i in range(N):
            if (playerUsername != tiket[i][3]):
                isUsernameValid = True
                break"""
        # <<< Edit 2
        # Penggantian search dan kevalidan seperti pada Edit 1
        for i in range(N):
            if (user[i][0] == "~~~"):
                isUsernameValid = True
                break
            if (user[i][3] == playerUsername):
                break
        # >>> Revisi 2
        # isUsernameValid berganti menjadi benar hanya jika for loop tidak berhasil
        # menemukan username yang sama pada database (dengan menemukan tanda end of array / mark)
    # Penulisan interface lanjutan
    rawPrint("Masukkan password pemain: ")
    playerPassword = input()
    # <<< Edit 3
    # Diperlukan modul hash yang terdapat pada login untuk memasukkan password
    playerPassword = hash(playerUsername,playerPassword)
    # >>> Revisi 3
    # Hanya perlu memanggil fungsi hash()
    playerRole = "Pemain"
    playerSaldo = "0"
    playerGold = "0"
    # Penulisan informasi baru
    print()
    """print("Selamat menjadi pemain, "+str(playerName)+". Selamat bermain.")"""
    # <<< Edit 4
    # Digunakan format untuk memperjelas dan mempermudah penulisan kode
    print("Selamat menjadi pemain, {}. Selamat bermain.".format(playerName))
    for i in range(N):
        if (user[i][0] == "~~~"):
            user[i] = [playerName, playerBornDay, playerHeight, playerUsername, playerPassword, playerRole, playerSaldo, playerGold]
            if (i != N):
                user[i+1][0] = "~~~"
            break
    print()
    return(user)
