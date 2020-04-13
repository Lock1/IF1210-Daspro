# Main function
# Deliverable didesain untuk windows (penggunaan "cls")

# import sequence
from package import base
from package import load
from package import save
from package import signup
from package import login
from package import caripemain
from package import cariwahana
from package import buytiket
from package import usetiket
from package import refund
from package import kritiksaran
from package import readkritiksaran
from package import addwahana
from package import topup
from package import readwahana
from package import readtiket
from package import exit

from package import goldenaccount
from package import bestwahana
from package import kehilangan

# Fungsi utama
load()
login() # Terdapat loop pada fungsi login
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
    if pilih == 1 or pilih == "cari":

    elif pilih == 2 or pilih == "beli_tiket":

    elif pilih == 3 or pilih == "main":

    elif pilih == 4 or pilih == "refund":

    elif pilih == 5 or pilih == "kritik_saran":

    elif pilih == 6 or pilih == "best_wahana":

    elif pilih == 7 or pilih == "tiket_hilang":

    elif pilih == 8 or pilih == "exit":

    else:
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
            print("\n")
