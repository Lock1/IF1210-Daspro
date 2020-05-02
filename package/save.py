############################## Informasi Modul ##############################
## Modul save
# Desainer
# Hizkia R. / 16519515 / 23 April 2020

# Coder
# Hizkia R. / 16519515 / 23 April 2020

# Tester
# Tanur Rizaldi Rahardjo / 16519525 / 23 April 2020

######### Kamus #########
### Argumen yang direquest oleh fungsi
# containerArray        : 3D Matrix of strings
# dbFolderPath          : String
# dbFileCount           : Integer
# N                     : Integer

### Kamus Internal
# containerName     : Array of strings
# containerLabel    : Array of strings
# openFileSuccess   : Boolean
# databasePath      : String
# database          : File object

###### Spesifikasi ######
# databaseSave      : (3D Matrix of strings, String, Integer, Integer) -> ()
# arrayToStringCSV  : (Array of strings, Integer) -> (String)
#############################################################################

############################### Algoritma ################################
from package.base import *

# Fungsi merubah array of string ke string csv
def arrayToStringCSV(array,maxCount):
    string = ""
    # Loop pembuatan string csv
    for i in range(maxCount):
        string = string + str(array[i])
        if (i < (maxCount - 1)):
            string += ","           # "Delimiter"
    return string

def databaseSave(containerArray,dbFolderPath=databaseFolderPath,dbFileCount=databaseFileCount,N=Nmax):
    # Inisiasi label yang digunakan
    containerLabel = ["Nama,Tanggal_Lahir,Tinggi_Badan,Username,Password,Role,Saldo,Gold\n","ID_Wahana,Nama_Wahana,Harga_Tiket,Batasan_Umur,Batasan_Tinggi\n","Username,Tanggal_Pembelian,ID_Wahana,Jumlah_Tiket\n","Username,Tanggal_Penggunaan,ID_Wahana,Jumlah_Tiket\n","Username,ID_Wahana,Jumlah_Tiket\n","Username,Tanggal_Refund,ID_Wahana,Jumlah_Tiket\n","Username,Tanggal_Kritik,ID_Wahana,Isi_Kritik\n","Username,Tanggal_Kehilangan,ID_Wahana,Jumlah_Tiket\n"]
    containerName = ["User", "Daftar Wahana", "Pembelian Tiket", "Penggunaan Tiket", "Kepemilikan Tiket", "Refund Tiket", "Kritik dan Saran", "Kehilangan Tiket"]
    # Loop untuk penyimpanan dengan exception handle ketika file tidak bisa dibuka
    for i in range(dbFileCount=databaseFileCount):
        databasePath = databaseFilePath(dbFolderPath=databaseFolderPath,"Masukkan nama File {:18}: ".format(containerName[i]))
        openFileSuccess = False
        # Exception handling
        while not openFileSuccess:
            try:
                open(databasePath,"w")
                openFileSuccess = True
            except PermissionError:
                print()
                print("Mohon untuk menutup program lain seperti excel ketika save.")
                input("Tekan enter untuk mencoba lagi menyimpan pada {}".format(databasePath))
        # Penulisan file
        with open(databasePath,"w") as database:
            database.write(containerLabel[i])
            for j in range(N):
                if (containerArray[i][j][0] == "~~~"):
                    database.write("~~~")
                    break
                databaseRow = arrayToStringCSV(containerArray[i][j],databaseColumn[i])+"\n"
                database.write(databaseRow)

    print()
    print("Data berhasil disimpan!")
    print()

########################### End of function ##############################
