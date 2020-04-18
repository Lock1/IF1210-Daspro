# Program utama
from package import *

# Inisiasi variabel konfigurasi dengan membaca config.ini
config = loadConfig()

databaseFolderPath = config[0].replace("\"","")
databaseFileCount = int(config[1])
Nmax = int(config[2])
toGoldCost = int(config[3])
menuPlayerCount = int(config[4])
menuAdminCount = int(config[5])
menuColumn = int(config[6])
menuRow = int(config[7])

menuVarName = stringConfigToArray(config[8],menuPlayerCount)
menuName = stringConfigToArray(config[9],menuPlayerCount)
menuAdminVarName = stringConfigToArray(config[10],menuAdminCount)
menuAdminName = stringConfigToArray(config[11],menuAdminCount)

# Fungsi utama
# Pengecekan apakah variabel global menu* valid
if (menuRow*menuColumn < menuPlayerCount) and (menuRow*menuColumn < menuAdminCount):
    print("Error, Konfigurasi menu tidak valid")
    exit()
# Menunggu hingga user load file utama dan login
loaded = False
while not loaded:
    wait = xinput()
    if wait == "load":
        # Pemanggilan fungsi load & login dan inisiasi variabel yang akan digunakan lagi
        (user, wahana, pembelian, penggunaan, tiket, refund, kritiksaran, kehilangan) = load(databaseFolderPath,databaseFileCount,Nmax)
        (nama, username, role, status) = login(user,Nmax)
        admin, gold = False, False
        if (role == "Admin"):
            admin = True
        if (status == "1"):
            gold = True
        loaded = True
# Menu utama
while loaded:
    print("Menu")
    print("Ketik angka atau tuliskan menu yang diinginkan")
    printMenu(menuRow,menuColumn,menuPlayerCount,menuVarName,menuName)
    if admin:
        print()
        print("Admin")
        printMenu(menuRow,menuColumn,menuAdminCount,menuAdminVarName,menuAdminName)
    pilih = xinput()

    # Switch untuk pemain
    if pilih in ["1", "cari"]:
        cariwahana(wahana,Nmax)
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
                print("TBA")
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
