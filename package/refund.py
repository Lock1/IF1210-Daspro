############################## Informasi Modul ##############################
## Modul caripemain
# Desainer
# Finna Alivia Nabila  / 16519125 / 24 April 2020

# Coder
# Finna Alivia Nabila / 16519125 / 24 April 2020

# Tester
#


## Kamus



## Spesifikasi


#############################################################################

####### Algoritma #######
from package.base import *

def requestRefund(username,user,tiket,refund,wahana,N=Nmax,refundFactor=refundMultiplier):
    refundID = input("Masukkan ID Wahana: ")
    refundDate = input("Masukkan Tanggal Refund: ")
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
