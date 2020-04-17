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
    # Inteface
    print("Masukkan username: ",end="")
    lostUsername = input()
    print("Tanggal kehilangan tiket: ",end="")
    lostTime = input()
    print("ID wahana: ",end="")
    lostID = input()
    print("Jumlah tiket yang dihilangkan: ",end="")
    lostTicket = intinput()

    # Pencarian database
    valid = False

    for i in range(N):
        if (tiket[i][0], tiket[i][1]) == (lostUsername, lostID):
            if int(tiket[i][2]) >= lostTicket:
                valid = True
                tiket[i][2] = str(int(tiket[i][2]) - lostTicket)
                break
        if tiket[i][0] == "~~~":
            break

    # Penulisan informasi baru
    if valid:
        print("Laporan kehilangan tiket Anda telah direkam.")
        for i in range(N):
            if kehilangan[i][0] == "~~~":
                kehilangan[i] = [lostUsername, lostTime, lostID, lostTicket]
                kehilangan[i+1][0] = "~~~"
                break
    return (tiket,kehilangan)
