# Modul kehilangan
# Desainer
# Tanur Rizaldi Rahardjo / 16519525 / 17 April 2020

# Coder
# Tanur Rizaldi Rahardjo / 16519525 / 17 April 2020

# Tester
#


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
    for i in range(N):
        if (tiket[i][0] == "~~~"):
            break
        if (tiket[i][0], tiket[i][1]) == (lostUsername, lostID):
            if (int(tiket[i][2]) >= lostTicket):
                isTicketValid = True
                tiket[i][2] = str(int(tiket[i][2]) - lostTicket)
                break
    # Penulisan informasi baru pada kehilangan.csv
    if isTicketValid:
        print("Laporan kehilangan tiket Anda telah direkam.")
        for i in range(N):
            if (kehilangan[i][0] == "~~~"):
                kehilangan[i] = [lostUsername, lostTime, lostID, lostTicket]
                if (i != N):
                    kehilangan[i+1][0] = "~~~"
                break
    print()
    return (tiket,kehilangan)
