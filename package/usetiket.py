############################## Informasi Modul ##############################
# Modul usetiket
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

def bermain(username,tiket,penggunaan,N):
    # Penulisan interface
    print()
    rawPrint("Masukkan ID wahana: ")
    playID = input()
    rawPrint("Masukkan tanggal hari ini: ")
    playTime = input()
    rawPrint("Jumlah tiket yang digunakan: ")
    playTicket = intinput()
    print()
    # Pengecekan tiket pada tiket.csv
    isTicketValid = False
    isUsernameExist, playTicketIndex = isExistOnDatabase(tiket,0,username,N,False,True)
    if isUsernameExist:
        if (tiket[playTicketIndex][1] == playID) and (int(tiket[playTicketIndex][2]) >= playTicket):
            isTicketValid = True
            tiket[playTicketIndex][2] = str(int(tiket[playTicketIndex][2]) - playTicket)
    # Penulisan informasi baru
    if isTicketValid:
        print("Terima kasih telah bermain.")
        penggunaanBaru = [username, playTime, playID, playTicket]
        penggunaan = appendDatabase(penggunaan,penggunaanBaru,N)
    else:
        print("Tiket Anda tidak valid dalam sistem kami")
    print()
    return (tiket,penggunaan)
