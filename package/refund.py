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
    refundID = input("Masukkan ID Wahana: ")
    refundDate = input("Masukkan Tanggal Refund: ")
    refundTicket = intinput("Jumlah tiket yang di-refund: ")

    # Filter refundTicket
    while refundTicket <= 0:
        print("Maaf tiket tidak valid")
        refundTicket = intinput("Jumlah tiket yang di-refund: ")

    # Digunakan algoritma yang sama dengan kehilangan & tiket pada database tiket
    isTicketValid = False
    isUsernameExist, refundUsernameIndex = isExistOnDatabase(tiket,0,username,N,False,True)
    if isUsernameExist:
        if (tiket[refundUsernameIndex][1] == refundID) and (int(tiket[refundUsernameIndex][2]) >= refundTicket):
            isTicketValid = True
            tiket[refundUsernameIndex][2] = str(int(tiket[refundUsernameIndex][2]) - refundTicket)

    # Penulisan informasi baru pada database refund dan user
    if isTicketValid:
        refundBaru = [username, refundDate, refundID, str(refundTicket)]
        refund = appendDatabase(refund,refundBaru,N)
        # Pencarian informasi pada user dan wahana
        (usernameExistOnUser, usernameIndex) = isExistOnDatabase(user,3,username,N,False,True)
        (wahanaExist, wahanaIndex) = isExistOnDatabase(wahana, 0, refundID,N,False,True)
        if usernameExistOnUser and wahanaExist:
            balance = int(int(user[usernameIndex][6]) + refundFactor*refundTicket*int(wahana[wahanaIndex][2]))
            user[usernameIndex][6] = str(balance)
        print("Uang refund sudah kami berikan pada akun Anda.")
    else:
        print("Anda tidak memiliki tiket terkait.")

    print()
    return (user,tiket,refund)

########################### End of function ##############################
