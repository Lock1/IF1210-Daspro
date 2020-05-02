############################## Informasi Modul ##############################
# Modul kehilangan
# Desainer
# Tanur Rizaldi Rahardjo / 16519525 / 17 April 2020

# Coder
# Tanur Rizaldi Rahardjo / 16519525 / 17 April 2020

# Tester
# Hizkia R. / 16519515 / 24 April 2020

######### Kamus #########
### Argumen yang direquest oleh fungsi
# user      : 2D Matrix of string
# N         : Integer

### Kamus Internal
# lostUsername                : String
# lostTime                    : String
# lostID                      : String
# lostTicket                  : Integer
# isTicketValid               : Boolean
# isUsernameExist             : Boolean
# lostTicketIndex             : Integer
# kehilanganBaru              : Array of strings

### Kamus informasi yang direturn
# tiket      : 2D Matrix of string
# kehilangan : 2D Matrix of string

###### Spesifikasi ######
# hilang        : (2D Matrix of strings, 2D Matrix of strings, Integer) -> (2D Matrix of strings, 2D Matrix of strings)
#############################################################################

############################### Algoritma ################################
# Digunakan Algoritma yang tidak jauh berbeda pada modul usetiket
from package.base import *

def hilang(tiket,kehilangan,N=Nmax):
    # Interface
    lostUsername = input("Masukkan username: ")
    lostTime = dateInput("Tanggal kehilangan tiket: ")
    lostID = idInput("ID wahana: ")
    lostTicket = posIntInput("Jumlah tiket yang dihilangkan: ")
    print()

    # Pencarian informasi database pada tiket.csv dan pengecekan kevalidan
    tiket, ticketUpdated = tiketUpdate(tiket,lostUsername,lostID,(lambda a, b: a - b),lostTicket,True)

    # Penulisan informasi baru pada database kehilangan
    if ticketUpdated:
        kehilanganBaru = [lostUsername, lostTime, lostID, lostTicket]
        kehilangan = appendDatabase(kehilangan,kehilanganBaru,N)
        print("Laporan kehilangan tiket Anda telah direkam.")
    else:
        print("{} tidak memiliki tiket sebanyak {}".format(lostUsername,lostTicket))

    print()
    return (tiket,kehilangan)

########################### End of function ##############################
