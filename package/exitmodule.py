############################## Informasi Modul ##############################
## Modul exitmodule
# Desainer
# Finna Alivia Nabila  / 16519125 / 24 April 2020

# Coder
# Finna Alivia Nabila / 16519125 / 24 April 2020

# Tester
# Hizkia R. / 16519515 / 24 April 2020

######### Kamus #########
### Argumen yang direquest oleh fungsi
# saveArray             : 3D Matrix of strings
# databaseFolderPath    : Strings
# databaseFileCount     : Integer

### Kamus Internal
# userInput : String

###### Spesifikasi ######
# exitSequence     : (3D Matrix of strings, String, Integer) -> ()
#############################################################################

############################### Algoritma ################################
from package.base import *
from package.save import *

def exitSequence(saveArray,databaseFolderPath,databaseFileCount):
    userInput = input("Apakah anda mau melakukan penyimpanan file yang sudah dilakukan (Y/N) ? ")
    if userInput in ["y","Y"]:
        databaseSave(saveArray,databaseFolderPath,databaseFileCount)
    print("See you later!")
    exit()

########################### End of function ##############################
