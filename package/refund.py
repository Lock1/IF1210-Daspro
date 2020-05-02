############################## Informasi Modul ##############################
## Modul caripemain
# Desainer
# Finna Alivia Nabila  / 16519125 / 24 April 2020

# Coder
# Finna Alivia Nabila / 16519125 / 24 April 2020

# Tester
# Kevin Domenico Tantiyo / 16519205 / 26 April 2020

######### Kamus #########
### Argumen yang direquest oleh fungsi
# username          : String
# user              : 2D Matrix of strings
# tiket             : 2D Matrix of strings
# refund            : 2D Matrix of strings
# wahana            : 2D Matrix of strings
# N                 : Integer
# refundFactor      : Float

### Kamus Internal
# refundID              : String
# refundDate            : String
# refundTicket          : Integer
# isTicketValid         : Boolean
# isUsernameExist       : Boolean
# refundUsernameIndex   : Integer
# refundBaru            : Array of string
# usernameExistOnUser   : Boolean
# usernameIndex         : Integer
# wahanaExist           : Boolean
# wahanaIndex           : Integer

### Kamus informasi yang direturn
# user          : 2D Matrix of strings
# tiket         : 2D Matrix of strings
# refund        : 2D Matrix of strings

###### Spesifikasi ######
# requestRefund     : (String, 4x 2D Matrix of string, Integer, Integer) -> (3x 2D Matrix of string)
#############################################################################

############################### Algoritma ################################
from package.base import *

def requestRefund(username,user,tiket,refund,wahana,N=Nmax,refundFactor=refundMultiplier):
    # Database user digunakan untuk menambah saldo, tiket untuk mengurangi tiket
    # refund untuk menambah log refund, dan wahana untuk mengambil harga yang wahana terkait

    # Input user
    refundID = idInput("Masukkan ID Wahana: ")
    refundDate = dateInput("Masukkan Tanggal Refund: ")
    refundTicket = posIntInput("Jumlah tiket yang di-refund: ","Maaf tiket tidak valid.")

    # Digunakan algoritma yang sama dengan kehilangan & tiket pada database tiket
    tiket, isTicketValid = tiketUpdate(tiket,username,refundID,(lambda a, b: a - b),refundTicket,True)

    # Penulisan informasi baru pada database refund dan user
    if isTicketValid:
        refundBaru = [username, refundDate, refundID, str(refundTicket)]
        refund = appendDatabase(refund,refundBaru)
        # Pencarian informasi pada user dan wahana
        (usernameExistOnUser, usernameIndex) = isExistOnDatabase(user,3,username,True)
        (wahanaExist, wahanaIndex) = isExistOnDatabase(wahana, 0, refundID,True)
        if usernameExistOnUser and wahanaExist:
            saldoUser = int(user[usernameIndex][6])
            refundBalance = refundTicket*int(wahana[wahanaIndex][2])
            updatedBalance = int(saldoUser + refundFactor*refundBalance)
            newBalance = [6, updatedBalance]
            user = replaceColumn(user,usernameIndex,newBalance)
        print("Uang refund sudah kami berikan pada akun Anda.")
    else:
        print("Anda tidak memiliki tiket terkait.")

    print()
    return (user,tiket,refund)

########################### End of function ##############################
