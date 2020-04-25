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
from package.base import *

# Fungsi loadCSV
"""def loadCSV(file,array,N):
    try:
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
    except OSError:
        raise FileNotFoundError"""

# Load File tanpa library csv
def stringCSVToArray(str1,maxCount):
    if (str1 == "~~~"):
        markArray = ["" for i in range(maxCount)]
        markArray[0] = "~~~"
        return markArray
    # Mark
    str1 = str1 + "\n"
    array = ["" for i in range(maxCount)]
    indexArray = [0 for i in range(2*maxCount)]
    counter, i = 1, 0
    while True:
        if (str1[i] == "\n"):
            indexArray[counter] = i
            break
        if (str1[i] == ","):
            indexArray[counter] = i
            counter += 1
        i += 1
    array[0] = str1[0:indexArray[1]]
    for j in range(1,maxCount):
         array[j] = str1[(indexArray[j]+1):indexArray[j+1]]
    return array

def loadCSV(file,array,fileColumn,N):
    try:
        with open(file) as database:
            database.readline()
            for i in range(N):
                databaseString = database.readline()
                array[i] = stringCSVToArray(databaseString,fileColumn)
                if (array[i][0] == "~~~"):
                    break
        return array
    except OSError:
        raise FileNotFoundError

# Load membaca dari baris ke 1 hingga N+1 (Baris pertama adalah informasi tabel)
def requestLoad(databaseFolderPath,databaseFileCount,N=Nmax):
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
        namaPathDatabase = databaseFilePath(databaseFolderPath,"Masukkan nama File {:18}: ".format(containerName[i]))
        loadFileSukses = False
        while not loadFileSukses:
            try:
                containerArray[i] = loadCSV(namaPathDatabase,containerArray[i],databaseColumn[i],N)
                loadFileSukses = True
            except FileNotFoundError:
                print("File tidak ada atau direktori tidak ada ({})".format(namaPathDatabase))
                namaPathDatabase = databaseFilePath(databaseFolderPath,"Masukkan nama File {:18}: ".format(containerName[i]))
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
