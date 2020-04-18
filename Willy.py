# Program utama
from package import *

# List Variabel
# tba



# Inisiasi Variabel
Nmax = 100
toGoldCost = 15000
databaseFolderPath = "database/"
databaseFileCount = 8

# Fungsi utama
wait = xinput()
if wait == "load":
    (user, wahana, pembelian, penggunaan, tiket, refund, kritiksaran, kehilangan) = load(databaseFolderPath,databaseFileCount,Nmax)
    (nama, username, role, status) = login(user,Nmax)
    admin, gold = False, False
    if role == "Admin":
        admin = True
    if status == "1":
        gold = True

    while True:
        print("Menu")
        print("Ketik angka atau tuliskan menu yang diinginkan")
        print("1. {:20} {:15}  5. {:19} {}".format("Cari Wahana","(cari)","Kritik dan Saran","(kritik_saran)"))
        print("2. {:20} {:15}  6. {:19} {}".format("Beli Tiket","(beli_tiket)","Wahana terbaik","(best_wahana)"))
        print("3. {:20} {:15}  7. {:19} {}".format("Bermain","(main)","Laporan Kehilangan","(tiket_hilang)"))
        print("4. {:20} {:15}  8. {:19} {}".format("Refund","(refund)","Keluar","(exit)"))
        if admin:
            print()
            print("Admin")
            print("A. {:20} {:15}  E. {:19} {}".format("Sign Up","(signup)","Lihat Tiket","(tiket_pemain)"))
            print("B. {:20} {:15}  F. {:19} {}".format("Cari Pemain","(cari_pemain)","Riwayat Wahana","(riwayat_wahana)"))
            print("C. {:20} {:15}  G. {:19} {}".format("Wahana Baru","(tambah_wahana)","Upgrade ke Gold","(upgrade_gold)"))
            print("D. {:20} {:15}  H. {:19} {}".format("Lihat Kritik Saran","(lihat_laporan)","Keluar","(exit)"))
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
