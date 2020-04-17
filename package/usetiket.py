# Modul usetiket
# Desainer
# Tanur Rizaldi Rahardjo / 16519525 / 17 April 2020

# Coder
# Tanur Rizaldi Rahardjo / 16519525 / 17 April 2020

# Tester
#

####### Algoritma #######
from package.base import *

def bermain(nama,tiket,penggunaan,N):
    # Penulisan interface
    print()
    print("Masukkan ID wahana: ", end="")
    playID = input()
    print("Masukkan tanggal hari ini: ", end="")
    playtime = input()
    print("Jumlah tiket yang digunakan: ", end="")
    playticket = intinput()
    print()

    # Pengecekan tiket pada tiket.csv
    valid = False

    for i in range(N):
        if (tiket[i][0], tiket[i][1]) == (nama, playID):
            if int(tiket[i][2]) >= playticket:
                valid = True
                tiket[i][2] = str(int(tiket[i][2]) - playticket)
                break
        if tiket[i][0] == "~~~":
            break

    # Penulisan informasi baru
    if valid:
        print("Terima kasih telah bermain.")
        for i in range(N):
            if penggunaan[i][0] == "~~~":
                penggunaan[i] = [username, playtime, playID, playticket]
                penggunaan[i+1][0] = "~~~"
                break
    else:
        print("Tiket Anda tidak valid dalam sistem kami")
    print()
    return (tiket,penggunaan)
