################ Tugas Besar - IF1210 - Dasar Pemrograman ################
# Kelas             : Dasar Pemrograman 05
# Kelompok          : 13

# Anggota
# Finna Alivia Nabila               / 16519125
# Kevin Domenico Tantiyo            / 16519205
# Hizkia Raditya Pratama Roosadi    / 16519515
# Tanur Rizaldi Rahardjo            / 16519525

# Kamus
### Variabel tersedia pada program utama
## Database
# user              : Array of strings
# wahana            : Array of strings
# pembelian         : Array of strings
# penggunaan        : Array of strings
# tiket             : Array of strings
# refund            : Array of strings
# kritiksaran       : Array of strings
# kehilangan        : Array of strings
# Nmax              : Integer
               # {Nmax Digunakan jika diperlukan membaca database sebagai}
               # {Batas maksimum informasi yang dibaca. Untuk batas efektif}
               # {gunakan mark ~~~ pada kolom pertama dan baris akhir} <<< Potensial ganti

## Variabel menyangkut user yang terlogin
# nama     : String      {Nama pemain yang terlogin}
# username : String      {Username pemain yang terlogin}
# admin    : Boolean     {Status akses user}
# gold     : Boolean     {Status account user, apakah gold atau standard}

##########################################################################
#### Program utama
from package import *

### Pembacaan konfigurasi
# Inisiasi variabel konfigurasi dengan membaca config.ini
config = loadConfig()
# Konfigurasi umum
databaseFolderPath = config[0].replace("\"","")
databaseFileCount = int(config[1])
Nmax = int(config[2])
toGoldCost = int(config[3])
menuPlayerCount = int(config[4])
menuAdminCount = int(config[5])
menuColumn = int(config[6])
menuRow = int(config[7])
# Konfigurasi array
menuVarName = stringConfigToArray(config[8],menuPlayerCount)
menuName = stringConfigToArray(config[9],menuPlayerCount)
menuAdminVarName = stringConfigToArray(config[10],menuAdminCount)
menuAdminName = stringConfigToArray(config[11],menuAdminCount)
# Pengecekan apakah konfigurasi menu* valid
if (menuRow*menuColumn < menuPlayerCount) and (menuRow*menuColumn < menuAdminCount):
    print("Error, Konfigurasi menu tidak valid")
    exit()

### Game loop
# Menunggu hingga user load file utama dan login
loaded = False
print("Selamat Datang!")
while not loaded:
    wait = xinput()
    if (wait == "load"):
        # Pemanggilan fungsi load & login dan inisiasi variabel yang akan digunakan lagi
        (user, wahana, pembelian, penggunaan, tiket, refund, kritiksaran, kehilangan) = load(databaseFolderPath,databaseFileCount,Nmax)
        (nama, username, admin, gold) = login(user,Nmax)
        loaded = True
## Menu utama
while loaded:
    print("Menu")
    print("Ketik angka atau tulis menu yang diinginkan")
    printMenu(menuRow,menuColumn,menuPlayerCount,menuVarName,menuName)
    if admin:
        print()
        print("Admin")
        print("Ketik menu yang diinginkan")
        printMenu(menuRow,menuColumn,menuAdminCount,menuAdminVarName,menuAdminName)
    pilih = xinput()
    # Switch untuk pemain
    if pilih in ["1", "cari"]:
        searchWahana(wahana,Nmax)
    elif pilih in ["2", "beli_tiket"]:
        print("TBA")
    elif pilih in ["3", "main"]:
        (tiket,penggunaan) = bermain(username,tiket,penggunaan,Nmax)
    elif pilih in ["4", "refund"]:
        print("TBA")
    elif pilih in ["5", "kritik_saran"]:
        print("TBA")
    elif pilih in ["6", "best_wahana"]:
        cariBestWahana(pembelian,wahana,Nmax)
    elif pilih in ["7", "tiket_hilang"]:
        (tiket,kehilangan) = hilang(tiket,kehilangan,Nmax)
    elif pilih in ["8", "exit"]:
        print("TBA")
    else:
        # Switch tambahan untuk admin
        if admin:
            if pilih in ["A","signup"]:
                user = signUpUser(user,Nmax)
            elif pilih in ["B","cari_pemain"]:
                print("TBA")
            elif pilih in ["C","tambah_wahana"]:
                wahana = tambahWahana(wahana,Nmax)
            elif pilih in ["D","lihat_laporan"]:
                print("TBA")
            elif pilih in ["E","tiket_pemain"]:
                print("TBA")
            elif pilih in ["F","riwayat_wahana"]:
                print("TBA")
            elif pilih in ["G","upgrade_gold"]:
                user = upgradeToGold(user,toGoldCost,Nmax)
            elif pilih in ["H"]:
                print("TBA")
            else:
                print("Masukkan tidak diketahui")
                print("\n")
        else:
            print("Masukkan tidak diketahui")
            print("\n")
