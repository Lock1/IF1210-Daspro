# Modul load
# Desainer
# Tanur Rizaldi Rahardjo / 16519525 / 17 April 2020

# Coder
# Tanur Rizaldi Rahardjo / 16519525 / 17 April 2020

# Tester
#


####### Algoritma #######
import csv
# Load membaca dari baris ke 1 hingga N+1 (Baris pertama adalah informasi tabel)
def load(N):
    ##### Inisiasi array penyimpanan #####
    # Database user.csv
    user = [["" for j in range(7)] for i in range(N+1)]
    # [nama, tanggal, tinggi, username, pwd, role, saldo]

    # Database wahana.csv
    wahana = [["" for j in range(5)] for i in range(N+1)]
    # [id wahana, nama wahana, harga wahana, batas umur, batas tinggi]

    # Database pembelian.csv
    pembelian = [["" for j in range(4)] for i in range(N+1)]
    # [username, tanggal beli, id wahana, jumlah tiket]

    # Database penggunaan.csv
    penggunaan = [["" for j in range(4)] for i in range(N+1)]
    # [username, tanggal beli, id wahana, jumlah tiket]

    # Database tiket.csv
    tiket = [["" for j in range(3)] for i in range(N+1)]
    # [username, id wahana, jumlah tiket]

    # Database refund.csv
    refund = [["" for j in range(4)] for i in range(N+1)]
    # [username, tanggalrefund, id wahana, jumlah tiket]

    # Database kritiksaran.csv
    kritiksaran = [["" for j in range(4)] for i in range(N+1)]
    # [username, tanggalkritik, idwahana, isikritik]

    # Database kehilangan.csv
    kehilangan = [["" for j in range(4)] for i in range(N+1)]
    # [username, tanggalkehilangan, idwahana, jumlahtiket]
    ######################################

    ##### Input nama file #####
    print("Masukkan nama File {:18}: ".format("User"),end="")
    usdb = "database/" + input()
    with open(usdb) as f:
        s = csv.reader(f)
        s.__next__() # Skip baris teratas
        for i in range(N):
            tp = s.__next__()
            if tp[0] == "~~~":
                user[i] = tp
                break
            else:
                user[i] = tp

    print("Masukkan nama File {:18}: ".format("Daftar Wahana"),end="")
    wadb = "database/" + input()
    with open(wadb) as f:
        s = csv.reader(f)
        s.__next__() # Skip baris teratas
        for i in range(N):
            tp = s.__next__()
            if tp[0] == "~~~":
                wahana[i] = tp
                break
            else:
                wahana[i] = tp

    print("Masukkan nama File {:18}: ".format("Pembelian Tiket"),end="")
    bedb = "database/" + input()
    with open(bedb) as f:
        s = csv.reader(f)
        s.__next__() # Skip baris teratas
        for i in range(N):
            tp = s.__next__()
            if tp[0] == "~~~":
                pembelian[i] = tp
                break
            else:
                pembelian[i] = tp

    print("Masukkan nama File {:18}: ".format("Penggunaan Tiket"),end="")
    gudb = "database/" + input()
    with open(gudb) as f:
        s = csv.reader(f)
        s.__next__() # Skip baris teratas
        for i in range(N):
            tp = s.__next__()
            if tp[0] == "~~~":
                penggunaan[i] = tp
                break
            else:
                penggunaan[i] = tp

    print("Masukkan nama File {:18}: ".format("Kepemilikan Tiket"),end="")
    tidb = "database/" + input()
    with open(tidb) as f:
        s = csv.reader(f)
        s.__next__() # Skip baris teratas
        for i in range(N):
            tp = s.__next__()
            if tp[0] == "~~~":
                tiket[i] = tp
                break
            else:
                tiket[i] = tp

    print("Masukkan nama File {:18}: ".format("Refund Tiket"),end="")
    redb = "database/" + input()
    with open(redb) as f:
        s = csv.reader(f)
        s.__next__() # Skip baris teratas
        for i in range(N):
            tp = s.__next__()
            if tp[0] == "~~~":
                refund[i] = tp
                break
            else:
                refund[i] = tp

    print("Masukkan nama File {:18}: ".format("Kritik dan Saran"),end="")
    krdb = "database/" + input()
    with open(krdb) as f:
        s = csv.reader(f)
        s.__next__() # Skip baris teratas
        for i in range(N):
            tp = s.__next__()
            if tp[0] == "~~~":
                kritiksaran[i] = tp
                break
            else:
                kritiksaran[i] = tp

    print("Masukkan nama File {:18}: ".format("Kehilangan Tiket"),end="")
    hidb = "database/" + input()
    with open(hidb) as f:
        s = csv.reader(f)
        s.__next__() # Skip baris teratas
        for i in range(N):
            tp = s.__next__()
            if tp[0] == "~~~":
                kehilangan[i] = tp
                break
            else:
                kehilangan[i] = tp
    ###########################
    print("File perusahaan Willy Wangky’s Chocolate Factory telah di-load.\n")
    return (user,wahana,pembelian,penggunaan,tiket,refund,kritiksaran,kehilangan)
