############################## Informasi Modul ##############################
## Modul usetiket
# Desainer
# Tanur Rizaldi Rahardjo / 16519525 / 17 April 2020

# Coder
# Tanur Rizaldi Rahardjo / 16519525 / 17 April 2020

# Tester
# Kevin Domenico Tantiyo / 16519205 / 26 April 2020

######### Kamus #########
### Argumen yang direquest oleh fungsi
# tiket      : 2D Matrix of strings
# penggunaan : 2D Matrix of strings
# username   : String
# N          : Integer

### Kamus Internal
# playID            : String
# playTime          : String
# playTicket        : Integer
# isTicketValid     : Boolean
# isUsernameExist   : Boolean
# playTicketIndex   : Integer
# penggunaanBaru    : Array of strings

### Kamus informasi yang direturn
# tiket      : 2D Matrix of strings
# penggunaan : 2D Matrix of strings

###### Spesifikasi ######
# bermain : (String, 2D Matrix of strings, 2D Matrix of strings, Integer) -> (2D Matrix of strings, 2D Matrix of strings)
#############################################################################

############################### Algoritma ################################
from package.base import *

def bermain(username,tiket,penggunaan,N=Nmax):
    # Penulisan interface dan meminta input
    print()
    playID = idInput("Masukkan ID wahana: ")
    playTime = dateInput("Masukkan tanggal hari ini: ")
    playTicket = posIntInput("Jumlah tiket yang digunakan: ")
    print()

    # Pengupdatean jika tiket valid
    tiket, ticketUpdated = tiketUpdate(tiket,username,playID,(lambda a, b: a - b),playTicket,True)

    # Penulisan informasi baru
    if ticketUpdated:
        penggunaanBaru = [username, playTime, playID, playTicket]
        penggunaan = appendDatabase(penggunaan,penggunaanBaru)
        print("Terima kasih telah bermain.")
    else:
        print("Tiket Anda tidak valid dalam sistem kami")

    print()
    return (tiket,penggunaan)

########################### End of function ##############################
