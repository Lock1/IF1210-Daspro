############################## Informasi Modul ##############################
## Modul cariwahana
# Desainer
# Finna Alivia Nabila  / 16519125 / 24 April 2020

# Coder
# Finna Alivia Nabila / 16519125 / 24 April 2020

# Tester
#


## Kamus



## Spesifikasi


#############################################################################

####### Algoritma #######
from package.base import *
from package.save import *

def exitSequence(saveArray,databaseFolderPath,databaseFileCount):
    userInput = input("Apakah anda mau melakukan penyimpanan file yang sudah dilakukan (Y/N) ? ")
    if userInput in ["y","Y"]:
        databaseSave(saveArray,databaseFolderPath,databaseFileCount)
    print("See you later!")
    exit()
