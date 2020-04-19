############################## Informasi Modul ##############################
# Modul load
# Desainer
# Tanur Rizaldi Rahardjo / 16519525 / 17 April 2020

# Coder
# Tanur Rizaldi Rahardjo / 16519525 / 17 April 2020

# Tester
#


## Kamus


## Spesifikasi


#############################################################################
####### Algoritma #######
import csv
from package.base import *

# Fungsi direktori database
def databaseFilePath(databaseFolderPath):
    n = databaseFolderPath + input()
    return n

# Fungsi loadCSV
def loadCSV(file,array,N):
    with open(file) as f:
        s = csv.reader(f)
        s.__next__() # Skip baris teratas
        for i in range(N): # Iterasi dimulai dari baris ke 1 hingga N+1
            tp = s.__next__()
            array[i] = tp
            # Mark akan diikutkan dalam insersi ke array
            if (tp[0] == "~~~"):
                break
    return array

# Load membaca dari baris ke 1 hingga N+1 (Baris pertama adalah informasi tabel)
def load(databaseFolderPath,databaseFileCount,N):
    ##### Inisiasi array penyimpanan #####
    user = [["" for j in range(7)] for i in range(N)]
    # Database user.csv
    # [nama, tanggal, tinggi, username, password, role, saldo, gold]

    wahana = [["" for j in range(5)] for i in range(N)]
    # Database wahana.csv
    # [id wahana, nama wahana, harga wahana, batas umur, batas tinggi]

    pembelian = [["" for j in range(4)] for i in range(N)]
    # Database pembelian.csv
    # [username, tanggal beli, id wahana, jumlah tiket]

    penggunaan = [["" for j in range(4)] for i in range(N)]
    # Database penggunaan.csv
    # [username, tanggal beli, id wahana, jumlah tiket]

    tiket = [["" for j in range(3)] for i in range(N)]
    # Database tiket.csv
    # [username, id wahana, jumlah tiket]

    refund = [["" for j in range(4)] for i in range(N)]
    # Database refund.csv
    # [username, tanggal refund, id wahana, jumlah tiket]

    kritiksaran = [["" for j in range(4)] for i in range(N)]
    # Database kritiksaran.csv
    # [username, tanggal kritik, idwahana, isi kritik]

    kehilangan = [["" for j in range(4)] for i in range(N)]
    # Database kehilangan.csv
    # [username, tanggal kehilangan, id wahana, jumlah tiket]
    ######################################

    ##### Input nama file #####
    containerArray = [user, wahana, pembelian, penggunaan, tiket, refund, kritiksaran, kehilangan]
    containerName = ["User", "Daftar Wahana", "Pembelian Tiket", "Penggunaan Tiket", "Kepemilikan Tiket", "Refund Tiket", "Kritik dan Saran", "Kehilangan Tiket"]
    for i in range(databaseFileCount):
        rawPrint("Masukkan nama File {:18}: ".format(containerName[i]))
        namaPathDatabase = databaseFilePath(databaseFolderPath)
        loadFileSukses = False
        while not loadFileSukses:
            try:
                containerArray[i] = loadCSV(namaPathDatabase,containerArray[i],N)
                loadFileSukses = True
            except FileNotFoundError:
                print("File tidak ada atau direktori tidak ada ({})".format(namaPathDatabase))
                rawPrint("Masukkan nama File {:18}: ".format(containerName[i]))
                namaPathDatabase = databaseFilePath(databaseFolderPath)
    ###########################

    # Insersi ke array database
    user = containerArray[0]
    wahana = containerArray[1]
    pembelian = containerArray[2]
    penggunaan = containerArray[3]
    tiket = containerArray[4]
    refund = containerArray[5]
    kritiksaran = containerArray[6]
    kehilangan = containerArray[7]

    print("File perusahaan Willy Wangky’s Chocolate Factory telah di-load.\n")
    return (user, wahana, pembelian, penggunaan, tiket, refund, kritiksaran, kehilangan)
