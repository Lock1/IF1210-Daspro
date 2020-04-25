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
               # {gunakan mark ~~~ pada kolom pertama dan baris akhir}

## Variabel menyangkut user yang terlogin
# nama     : String      {Nama pemain yang terlogin}
# username : String      {Username pemain yang terlogin}
# isAdmin  : Boolean     {Status akses user}
# gold     : Boolean     {Status account user, apakah gold atau standard}

## Variabel sementara
# isLoaded    : Boolean
# pilihanMenu : String
##########################################################################
#### Program utama
from package import *

### Game loop
# Menunggu hingga user load file utama dan login
isLoaded = False
print("Selamat Datang!")
while not isLoaded:
    wait = xinput()
    if (wait == "load"):
        # Pemanggilan fungsi load & login dan inisiasi variabel yang akan digunakan lagi
        (user, wahana, pembelian, penggunaan, tiket, refund, kritiksaran, kehilangan) = requestLoad(databaseFolderPath,databaseFileCount)
        (nama, username, isAdmin, gold) = requestLogin(user)
        isLoaded = True

## Menu utama
while isLoaded:
    print("Menu")
    print("Ketik angka atau tulis menu yang diinginkan")
    printMenu(menuRow,menuColumn,menuPlayerCount,menuVarName,menuName)
    if isAdmin:
        print()
        print("Admin")
        print("Ketik menu yang diinginkan")
        printMenu(menuRow,menuColumn,menuAdminCount,menuAdminVarName,menuAdminName)
    pilihanMenu = xinput()
    # Switch untuk pemain
    if pilihanMenu in ["1", "cari"]:
        searchWahana(wahana)
    elif pilihanMenu in ["2", "beli_tiket"]:
        (user,tiket) = beliTiketUser(username,gold,user,wahana,tiket)
    elif pilihanMenu in ["3", "main"]:
        (tiket,penggunaan) = bermain(username,tiket,penggunaan)
    elif pilihanMenu in ["4", "refund"]:
        (user, tiket, refund) = requestRefund(username,user,tiket,refund,wahana)
    elif pilihanMenu in ["5", "kritik_saran"]:
        kritiksaran =  tulisKritikSaran(username,kritiksaran)
    elif pilihanMenu in ["6", "best_wahana"]:
        cariBestWahana(pembelian,wahana)
    elif pilihanMenu in ["7", "tiket_hilang"]:
        (tiket,kehilangan) = hilang(tiket,kehilangan)
    elif pilihanMenu in ["8","save"]:
        saveArray = [user, wahana, pembelian, penggunaan, tiket, refund, kritiksaran, kehilangan]
        databaseSave(saveArray,databaseFolderPath,databaseFileCount)
    elif pilihanMenu in ["9", "exit"]:
        saveArray = [user, wahana, pembelian, penggunaan, tiket, refund, kritiksaran, kehilangan]
        exitSequence(saveArray,databaseFolderPath,databaseFileCount)
    else:
        # Switch tambahan untuk isAdmin
        if isAdmin:
            if pilihanMenu in ["A","signup"]:
                user = signUpUser(user)
            elif pilihanMenu in ["B","cari_pemain"]:
                searchPemain(user)
            elif pilihanMenu in ["C","tambah_wahana"]:
                wahana = tambahWahana(wahana)
            elif pilihanMenu in ["D","lihat_laporan"]:
                printKritikSaran(kritiksaran)
            elif pilihanMenu in ["E","tiket_pemain"]:
                adminReadTicket(tiket,wahana)
            elif pilihanMenu in ["F","riwayat_wahana"]:
                riwayatWahana(penggunaan)
            elif pilihanMenu in ["G","upgrade_gold"]:
                (user, gold) = upgradeToGold(gold,user,toGoldCost)
            elif pilihanMenu in ["H","topup"]:
                user = requestTopUp(user)
            elif pilihanMenu in ["I"]:
                saveArray = [user, wahana, pembelian, penggunaan, tiket, refund, kritiksaran, kehilangan]
                exitSequence(saveArray,databaseFolderPath,databaseFileCount)
            else:
                print("Masukkan tidak diketahui")
                print("\n")
        else:
            print("Masukkan tidak diketahui")
            print("\n")
