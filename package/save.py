############################## Informasi Modul ##############################
## Modul save
# Desainer
# Hizkia R. / 16519515 / 23 April 2020

# Coder
# Hizkia R. / 16519515 / 23 April 2020

# Tester
# Tanur Rizaldi Rahardjo / 16519525 / 23 April 2020


## Kamus


## Spesifikasi


#############################################################################
####### Algoritma #######
from package.base import *


# Save file tanpa library csv
def arrayToStringCSV(array,maxCount):
    string = ""
    for i in range(maxCount):
        string = string + array[i]
        if (i < (maxCount - 1)):
            string += ","           # "Delimiter"
    return string

def databaseSave(containerArray,databaseFolderPath,databaseFileCount,N=Nmax):
    containerLabel = ["Nama,Tanggal_Lahir,Tinggi_Badan,Username,Password,Role,Saldo,Gold\n","ID_Wahana,Nama_Wahana,Harga_Tiket,Batasan_Umur,Batasan_Tinggi\n","Username,Tanggal_Pembelian,ID_Wahana,Jumlah_Tiket\n","Username,Tanggal_Penggunaan,ID_Wahana,Jumlah_Tiket\n","Username,ID_Wahana,Jumlah_Tiket\n","Username,Tanggal_Refund,ID_Wahana,Jumlah_Tiket\n","Username,Tanggal_Kritik,ID_Wahana,Isi_Kritik\n","Username,Tanggal_Kehilangan,ID_Wahana,Jumlah_Tiket\n"]
    containerName = ["User", "Daftar Wahana", "Pembelian Tiket", "Penggunaan Tiket", "Kepemilikan Tiket", "Refund Tiket", "Kritik dan Saran", "Kehilangan Tiket"]
    for i in range(databaseFileCount):
        databasePath = databaseFilePath(databaseFolderPath,"Masukkan nama File {:18}: ".format(containerName[i]))
        openFileSuccess = False
        while not openFileSuccess:
            try:
                open(databasePath,"w")
                openFileSuccess = True
            except PermissionError:
                print()
                print("Mohon untuk menutup program lain seperti excel ketika save.")
                input("Tekan enter untuk mencoba lagi menyimpan pada {}".format(databasePath))

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
