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
    for i in range(N):
        if (tiket[i][0] == "~~~"):
            break
        if (tiket[i][0], tiket[i][1]) == (username, playID):
            if (int(tiket[i][2]) >= playTicket):
                isTicketValid = True
                tiket[i][2] = str(int(tiket[i][2]) - playTicket)
                break
    # Penulisan informasi baru
    if isTicketValid:
        print("Terima kasih telah bermain.")
        for i in range(N):
            if (penggunaan[i][0] == "~~~"):
                penggunaan[i] = [username, playTime, playID, playTicket]
                if (i != N):
                    penggunaan[i+1][0] = "~~~"
                break
    else:
        print("Tiket Anda tidak valid dalam sistem kami")
    print()
    return (tiket,penggunaan)
