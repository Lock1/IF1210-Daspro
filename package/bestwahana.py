############################## Informasi Modul ##############################
## Modul login
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

def insertNewID(array,newID,newTicket,N):
    for i in range(N):
        if (array[i] == ["",0]):
            array[i] = [newID, newTicket]
            break
    return array

def isIDNotInArray(pembelian,index,arr,N): # POSSIBLY REPLACED WITH NEW DATABASE SEARCH
    isInArray = False
    for i in range(N):
        if (pembelian[index][2] == arr[i][0]):
            isInArray = True
            break
    return (not isInArray)

def cariBestWahana(pembelian,wahana,N):
    # Penghitungan tiket berdasarkan ID wahana
    tiketTerjual = [["",0] for i in range(N)]     # Array mengandung [ID Wahana, Tiket]
    for i in range(N):
        if (pembelian[i][0] == "~~~"):
            break
        if isIDNotInArray(pembelian,i,tiketTerjual,N):
            tiketTerjual = insertNewID(tiketTerjual,pembelian[i][2],int(pembelian[i][3]),N)
        else:
            for j in range(N):
                if (tiketTerjual[j] == pembelian[i][2]):
                    tiketTerjual[j] += int(pembelian[i][3])
                    break
    # Sort array tiketTerjual untuk menentukan tiket terjual tertinggi
    selectionSort(tiketTerjual,N,1)
    # Pencarian Nama berdasarkan 3 ID teratas
    for i in range(3):
        cariWahanaID = tiketTerjual[i][0]
        isExistOnWahana, wahanaIndex = isExistOnDatabase(wahana,0,cariWahanaID,N,False,True)
        if isExistOnWahana:
            printWahana(i+1,cariWahanaID,wahana[wahanaIndex][1],tiketTerjual[wahanaIndex][1])
    print()
