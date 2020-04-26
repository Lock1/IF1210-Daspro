################ Tugas Besar - IF1210 - Dasar Pemrograman ################
# Kelas             : Dasar Pemrograman 05
# Kelompok          : 13

######## Anggota ########
# Finna Alivia Nabila               / 16519125
# Kevin Domenico Tantiyo            / 16519205
# Hizkia Raditya Pratama Roosadi    / 16519515
# Tanur Rizaldi Rahardjo            / 16519525

######### Kamus #########
### Variabel tersedia pada program utama
## Variabel yang berhubungan database
# user              : Array of strings
# wahana            : Array of strings
# pembelian         : Array of strings
# penggunaan        : Array of strings
# tiket             : Array of strings
# refund            : Array of strings
# kritiksaran       : Array of strings
# kehilangan        : Array of strings
# Nmax              : Integer           # {Nmax diload pada config.ini, lihat bagian variabel config.ini}
                                        # {Nmax Digunakan ketika fungsi ingin melakukan baca database,}
                                        # {Nmax digunakan sebagai batas maksimum informasi yang dibaca (Hard limit).}
                                        # {Untuk batas efektif gunakan mark ~~~ pada kolom pertama dan baris akhir.}

## Variabel menyangkut user yang terlogin
# nama     : String      {Nama pemain yang terlogin}
# username : String      {Username pemain yang terlogin}
# isAdmin  : Boolean     {Status akses user}
# gold     : Boolean     {Status account user, apakah gold atau standard}

## Variabel sementara
# isLoaded    : Boolean     {Status program apakah telah dilakukan load database atau belum}
# pilihanMenu : String      {String untuk mencari pilihan menu yang dipilih oleh user}
# wait        : String      {Menunggu input user ketika pertama kali program berjalan}

### Variabel yang terdapat ketika program load package (Baca pada modul base untuk lebih lanjut)
## Variabel config.ini
# databaseFolderPath    : String                {Folder dasar dimana file database diletakkan}
# databaseFileCount     : Integer               {Banyaknya file database yang ada}
# Nmax                  : Integer               {Nmax adalah batas maksimum baris database yang dibaca}
# toGoldCost            : Integer               {Harga untuk mengupgrade ke gold}
# menuPlayerCount       : Integer               {Banyaknya menu pada menu player}
# menuAdminCount        : Integer               {Banyaknya menu pada menu admin}
# menuColumn            : Integer               {Banyak kolom yang diinginkan pada print menu}
# menuRow               : Integer               {Banyak baris yang diinginkan pada print menu}
## Konfigurasi dalam bentuk array
# menuVarName           : Array of strings      {Container untuk nama variabel yang bisa dicall oleh user (contoh: cari_pemain)}
# menuName              : Array of strings      {Container nama menu}
# menuAdminVarName      : Array of strings      {Container untuk nama variabel yang hanya bisa dicall oleh admin}
# menuAdminName         : Array of strings      {Container nama menu tambahan untuk admin}

## Variabel konfigurasi pada base.py
# databaseColumn            : Array of integer  {Banyaknya kolom pada database}
# refundMultiplier          : Float             {Pengali harga tiket refund}
# goldDiscountMultiplier    : Float             {Pengali harga diskon untuk gold membership}
#############################################################################

############################### Algoritma ################################
from package import *


# Menunggu hingga menulis load dan melakukan load + login
isLoaded = False
print("Selamat Datang!")
while not isLoaded:
    wait = xinput()
    if (wait == "load"):
        # Pemanggilan fungsi load & login dan inisiasi variabel yang akan digunakan
        (user, wahana, pembelian, penggunaan, tiket, refund, kritiksaran, kehilangan) = requestLoad(databaseFolderPath,databaseFileCount)
        (nama, username, isAdmin, gold) = requestLogin(user)
        isLoaded = True

### Game loop
while isLoaded:
    # Pengeprintan list menu yang ada
    print("Menu")
    print("Ketik angka atau tulis menu yang diinginkan")
    printMenu(menuRow,menuColumn,menuPlayerCount,menuVarName,menuName)
    if isAdmin:
        # Hanya diprint untuk admin
        print()
        print("Admin")
        print("Ketik menu yang diinginkan")
        printMenu(menuRow,menuColumn,menuAdminCount,menuAdminVarName,menuAdminName,True)

    # Menunggu input user
    pilihanMenu = xinput()
    ## Switch untuk pemain
    # Fungsi dan prosedur yang terkait akan dipanggil dan pemberian database yang direquest oleh fungsi atau prosedur.
    # Untuk fungsi yang mengganti database, return fungsi akan menggantikan database yang ada pada program utama.
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

########################### End of function ##############################
