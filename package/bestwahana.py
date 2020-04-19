############################## Informasi Modul ##############################
# Modul login
# Desainer
# Tanur Rizaldi Rahardjo / 16519525 / 18 April 2020

# Coder
# Tanur Rizaldi Rahardjo / 16519525 / 18 April 2020

# Tester
#


## Kamus


## Spesifikasi


#############################################################################
####### Algoritma #######
from package.base import *

def printWahana(i,ID,namaWahana,tiketJual):
    print("{:1} | {:6} | {:30} | {}".format(i, ID, namaWahana, tiketJual))

def insertNewID(array,newID,newTicket,N):
    for i in range(N):
        if (array[i] == ["",0]):
            array[i] = [newID, newTicket]
            break
    return array

def isIDNotInArray(pembelian,index,arr,N):
    found = False
    for i in range(N):
        if (pembelian[index][2] == arr[i][0]):
            found = True
            break
    return (not found)

def cariBestWahana(pembelian,wahana,N):
    # Penghitungan tiket berdasarkan ID wahana
    tiketTerjual = [["",0] for i in range(N)]     # Array mengandung [ID Wahana, Tiket]
    for i in range(N):
        if (pembelian[i][0] == "~~~"):
            break
        if isIDNotInArray(pembelian,i,tiketTerjual,N):
            tiketTerjual = insertNewID(tiketTerjual,pembelian[i][2],int(pembelian[i][3]),N)
        else:
            print("ID ada di array")
            for j in range(N):
                if (tiketTerjual[j] == pembelian[i][2]):
                    tiketTerjual[j] += int(pembelian[i][3])
                    break
    # Sort array tiketTerjual untuk menentukan tiket terjual tertinggi
    # Digunakan kembali Selection sort yang diimplementasikan pada NIM sort pada soal sortmhs.py
    for i in range(N):
        tiketcek = tiketTerjual[i][1]
        for j in range(i+1,N):
            if (tiketcek < tiketTerjual[j][1]):
                tiketTerjual[i], tiketTerjual[j] = tiketTerjual[j], tiketTerjual[i]
    # Pencarian Nama berdasarkan 3 ID teratas
    for i in range(3):
        cariWahanaID = tiketTerjual[i][0]
        for j in range(N):
            if (wahana[j][0] == "~~~"):
                break
            if (wahana[j][0] == cariWahanaID):
                cariNamaWahana = wahana[j][1]
                break
        printWahana(i+1,cariWahanaID,cariNamaWahana,tiketTerjual[i][1])
    print()
