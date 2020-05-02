############################## Informasi Modul ##############################
## Modul login
# Desainer
# Tanur Rizaldi Rahardjo / 16519525 / 18 April 2020

# Coder
# Tanur Rizaldi Rahardjo / 16519525 / 18 April 2020

# Tester
# Finna Alivia Nabila / 16519125 / 26 April 2020

######### Kamus #########
### Argumen yang direquest oleh fungsi
# pembelian       : 2D Matrix of string
# wahana          : 2D Matrix of string
# N               : Integer

### Kamus Internal
# tiketTerjual        : 2D Matrix of (String, Integer)
# cariWahanaID        : String
# isExistOnWahana     : Boolean
# wahanaIndex         : Integer

###### Spesifikasi ######
# printWahana       : (Integer, 3x Strings) -> ()
# insertNewID       : (2D Matrix of (String, Integer); Array of (String, Integer); Integer; Integer) -> (2D Matrix of (String, Integer))
# isIDNotInArray    : (2D Matrix of strings; Integer; 2D Matrix of (String, Integer); Integer) -> ()
# cariBestWahana    : (2D Matrix of strings, 2D Matrix of strings, Integer) -> ()
#############################################################################

############################### Algoritma ################################
from package.base import *

## Prosedur printWahana
# Untuk mengeprint wahana dengan sintaks bestwahana
def printWahana(i,ID,namaWahana,tiketJual):
    print("{:1} | {:6} | {:30} | {}".format(i, ID, namaWahana, tiketJual))

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

def cariBestWahana(pembelian,wahana,N=Nmax):
    # Penghitungan tiket berdasarkan ID wahana
    tiketTerjual = [["",0] for i in range(N)]     # Array mengandung [ID Wahana, Tiket]
    for i in range(N):
        if (pembelian[i][0] == "~~~"):
            break
        if isIDNotInArray(pembelian,i,tiketTerjual,N):
            tiketTerjual = insertNewID(tiketTerjual,pembelian[i][2],int(pembelian[i][3]),N)
        else:
            for j in range(N):
                if (tiketTerjual[j][0] == pembelian[i][2]):
                    tiketTerjual[j][1] += int(pembelian[i][3])
                    break

    # Sort array tiketTerjual untuk menentukan tiket terjual tertinggi
    selectionSort(tiketTerjual,N,1)
    # Pencarian Nama berdasarkan 3 ID teratas
    for i in range(3):
        cariWahanaID = tiketTerjual[i][0]
        isExistOnWahana, wahanaIndex = isExistOnDatabase(wahana,0,cariWahanaID,True)
        if isExistOnWahana:
            printWahana(i+1,cariWahanaID,wahana[wahanaIndex][1],tiketTerjual[i][1])
    print()

########################### End of function ##############################
