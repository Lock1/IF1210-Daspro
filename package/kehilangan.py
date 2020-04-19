############################## Informasi Modul ##############################
# Modul kehilangan
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
# Digunakan Algoritma yang tidak jauh berbeda pada modul usetiket
from package.base import *

def hilang(tiket,kehilangan,N):
    # Interface
    rawPrint("Masukkan username: ")
    lostUsername = input()
    rawPrint("Tanggal kehilangan tiket: ")
    lostTime = input()
    rawPrint("ID wahana: ")
    lostID = input()
    rawPrint("Jumlah tiket yang dihilangkan: ")
    lostTicket = intinput()
    print()
    # Pencarian informasi database pada tiket.csv dan pengecekan kevalidan
    isTicketValid = False
    isUsernameExist, lostTicketIndex = isExistOnDatabase(tiket,0,lostUsername,N,False,True)
    if isUsernameExist:
        if (tiket[lostTicketIndex][1] == lostID) and (int(tiket[lostTicketIndex][2]) >= lostTicket):
            isTicketValid = True
            tiket[lostTicketIndex][2] = str(int(tiket[lostTicketIndex][2]) - lostTicket)
    # Penulisan informasi baru pada kehilangan.csv
    if isTicketValid:
        print("Laporan kehilangan tiket Anda telah direkam.")
        kehilanganBaru = [lostUsername, lostTime, lostID, lostTicket]
        kehilangan = appendDatabase(kehilangan,kehilanganBaru,N)
    else:
        print("{} tidak memiliki tiket sebanyak {}".format(lostUsername,lostTicket))
    print()
    return (tiket,kehilangan)
