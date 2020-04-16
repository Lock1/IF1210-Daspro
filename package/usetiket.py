# Modul usetiket
# Desainer
# Tanur Rizaldi Rahardjo / 16519525 / 17 April 2020

# Coder
# Tanur Rizaldi Rahardjo / 16519525 / 17 April 2020

# Tester
#

####### Algoritma #######
from package.base import *

def useTiket(status):
    # pull user information
        # DONT FORGET GOLD
    # variabel
    playID = ""
    playtime = ""
    playticket = 0

    print("Masukkan ID wahana: ", end="")
    playID = xinput()
    print()
    print("Masukkan tanggal hari ini: ", end="")
    playtime = xinput()
    print()
    print("Jumlah tiket yang digunakan: ", end="")
    print("\n")

    # validator
    valid = False
    # pull user information


    # validity handler
    if valid:
        print("Terima kasih telah bermain.")
        # update sequence
    else:
        print("Tiket Anda tidak valid dalam sistem kami")
