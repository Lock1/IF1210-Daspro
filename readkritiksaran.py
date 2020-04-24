############################## Informasi Modul ##############################

## Modul readkritiksaran

# Desainer

# Hizkia R. / 16519515 / 24 April 2020



# Coder

# Hizkia R. / 16519515 / 24 April 2020



# Tester

# Tanur Rizaldi Rahardjo / 16519525 / 24 April 2020





## Kamus

#N: integer





## Spesifikasi





#############################################################################



####### Algoritma #######

from package.base import *
def sortKritikSaran(database,N):
    for i in range (N):
        for j in range (i-1,-1,j,-1):
            if ord(kritiksaran[j][2][0])>ord(kritiksaran[j][2][0]):
                kritiksaran[j],kritiksaran[j+1]=kritiksaran[j+1],kritiksaran[j]
            else:
                break
            
def printKritikSaran(database,N):
    sortKritikSaran(kritiksaran,N)
    print("Kritik dan saran:")
    for i in range(N):
        print("{:6}|{:10}|{:20}|{50}".format(kritiksaran[i][2],kritiksaran[i][1],kritiksaran[i][0],kritiksaran[i][3])
    
