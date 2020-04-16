# Main function

# base
# load
# login

# import sequence
from package import *

#from package import goldenaccount
#from package import bestwahana
#from package import kehilangan

# Fungsi utama
wait = xinput()
if wait == "load":
    (user,wahana,pembelian,penggunaan,tiket,refund,kritiksaran,kehilangan) = load()
    username = login(user) # Terdapat loop pada fungsi login
    while True:
        print("Menu")
        print("Ketik angka atau tuliskan menu yang diinginkan")
        print("1. {:20} {:15}  5. {:19} {}".format("Cari Wahana","(cari)","Kritik dan Saran","(kritik_saran)"))
        print("2. {:20} {:15}  6. {:19} {}".format("Beli Tiket","(beli_tiket)","Wahana terbaik","(best_wahana)"))
        print("3. {:20} {:15}  7. {:19} {}".format("Bermain","(main)","Laporan Kehilangan","(tiket_hilang)"))
        print("4. {:20} {:15}  8. {:19} {}".format("Refund","(refund)","Keluar","(exit)"))
        """if admin:
            print()
            print("Admin")
            print("A. {:20} {:15}  E. {:19} {}".format("Sign Up","(signup)","Lihat Tiket","(tiket_pemain)"))
            print("B. {:20} {:15}  F. {:19} {}".format("Cari Pemain","(cari_pemain)","Riwayat Wahana","(riwayat_wahana)"))
            print("C. {:20} {:15}  G. {:19} {}".format("Wahana Baru","(tambah_wahana)","Upgrade ke Gold","(upgrade_gold)"))
            print("D. {:20} {:15}  H. {:19} {}".format("Lihat Kritik Saran","(lihat_laporan)","Keluar","(exit)"))
        """ # nyalakan ketika flag admin sudah ada
        pilih = xinput()

        # Switch untuk pemain
        if pilih in ["1", "cari"]:
            cariwahana(wahana)
        elif pilih in ["2", "beli_tiket"]:
            print("TBA")
        elif pilih in ["3", "main"]:
            print("TBA")
        elif pilih in ["4", "refund"]:
            print("TBA")
        elif pilih in ["5", "kritik_saran"]:
            print("TBA")
        elif pilih in ["6", "best_wahana"]:
            print("TBA")
        elif pilih in ["7", "tiket_hilang"]:
            print("TBA")
        elif pilih in ["8", "exit"]:
            print("TBA")
        """else:
            # Switch tambahan untuk admin
            if admin:
                if pilih == "A" or pilih == "signup":

                elif pilih == "B" or pilih == "cari_pemain":

                elif pilih == "C" or pilih == "tambah_wahana":

                elif pilih == "D" or pilih == "lihat_laporan":

                elif pilih == "E" or pilih == "tiket_pemain":

                elif pilih == "F" or pilih == "riwayat_wahana":

                elif pilih == "G" or pilih == "upgrade_gold":

                elif pilih == "H":

            else:
                print("Masukkan tidak diketahui")
                print("\n")"""
