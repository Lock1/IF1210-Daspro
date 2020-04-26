############################## Informasi Modul ##############################
## Modul readkritiksaran
# Desainer
# Hizkia R. / 16519515 / 24 April 2020

# Coder
# Hizkia R. / 16519515 / 24 April 2020

# Tester
# Tanur Rizaldi Rahardjo / 16519525 / 24 April 2020

######### Kamus #########
### Argumen yang direquest oleh fungsi
# kritiksaran    : 2D Matrix of string
# N              : Integer

### Kamus Internal
# placeholder   : Boolean
# markIndex     : Integer

###### Spesifikasi ######
# sortKritikSaran   : (2D Matrix of strings, Integer) -> (2D Matrix of strings)
# printKritikSaran  : (2D Matrix of strings, Integer) -> ()
#############################################################################

############################### Algoritma ################################
from package.base import *

def sortKritikSaran(kritiksaran,N):
    # Sorting dengan insertion sort pada praktikum
    for i in range(N):
        for j in range(i-1,-1,-1):
            if (ord(kritiksaran[j][2][0]) > ord(kritiksaran[j+1][2][0])) and (j >= 0):
                kritiksaran[j], kritiksaran[j+1] = kritiksaran[j+1], kritiksaran[j]
            else:
                break
    return kritiksaran

def printKritikSaran(kritiksaran,N=Nmax):
    (placeholder,markIndex) = isExistOnDatabase(kritiksaran,0,"~~~",N,False,True)
    kritiksaran = sortKritikSaran(kritiksaran,markIndex)
    print("Kritik dan saran:")
    for i in range(markIndex):
        print("{:6} | {:10} | {:30} | {:50}".format(kritiksaran[i][2],kritiksaran[i][1],kritiksaran[i][0],kritiksaran[i][3]))

    print()

########################### End of function ##############################
