############################## Informasi Modul ##############################
### Modul untuk fungsi yang umum ###
## Kamus


## Spesifikasi


#############################################################################

############################### Fungsi Dasar ################################
from hashlib import *
############ Fungsi I/O dan string operation ############
## Fungsi xinput()
# xinput digunakan untuk input user dengan penambahan sebuah string >>> didepannya
def xinput(str1=""):
    if not(str1 == ""):
        print(str1)
    print(">>> ",end="")
    n = input()
    return n

## Fungsi intinput
# Meminta input integer secara paksa
# Jika tidak integer, input akan diulangi
def intinput(str1=""):
    while True:
        n = input(str1)
        try:
            return int(n)
        except ValueError:
            print("Masukan tidak diketahui")

## Prosedur rawPrint
# Menuliskan tulisan dilayar tanpa endline ("\n")
def rawPrint(str1):
    print(str1,end="")

## Fungsi addBracket
# Menambahkan kurung pada string
def addBracket(str1):
    bracketed = "({})".format(str1)
    return bracketed

## Prosedur printMenu
# Menuliskan menu pada program utama
def printMenu(row,column,maxMenuIndex,varArray,nameArray):
    for i in range(row):
        for j in range(column):
            if ((i + row*j) >= maxMenuIndex):
                rawPrint("")
            else:
                rawPrint("{}. {:20} {:17} ".format((i+1+row*j),nameArray[i+row*j],addBracket(varArray[i+row*j])))
        print()


########### Fungsi database ###########
## Fungsi appendDatabase
def appendDatabase(database,insertArray,N):
    for i in range(N):
        if (database[i][0] == "~~~"):
            database[i] = insertArray
            if (i != N):
                database[i+1][0] = "~~~"
            break
    return database

## Fungsi isExistOnDatabase
# Digunakan untuk mengecek apakah relasi antara database[][index] dan search
# dengan checkFunction benar, jika benar flagToBeToggled akan dinegasi dan direturn
# Argumen tambahan replace digunakan untuk mengganti database
def isExistOnDatabase(database,index,search,N,flagToBeToggled=False,indexReturn=False,checkFunction=(lambda a,b: a==b),replace="Null"):
    for i in range(N):
        if (database[i][0] == "~~~"):
            break
        if (checkFunction(database[i][index],search)):
            flagToBeToggled = not flagToBeToggled
            if indexReturn:
                return (flagToBeToggled,i)
            if (replace != "Null"): # To be fixed
                database[i][index] = replace
                return (flagToBeToggledFlag,database)
            break
    if indexReturn:
        # Failure to find index
        return (False,"Null")
    return flagToBeToggled

############ Fungsi Config ###########
## Fungsi loadConfig
# Digunakan untuk membaca file config.ini dan mengganti informasi pada file tersebut
# menjadi array of strings
def loadConfig():
    config = ["" for i in range(12)]
    try:
        checkExist = open("tools/config.ini")
    except FileNotFoundError:
        print("config.ini tidak ditemukan pada /tools/config.ini")
        print("Konfigurasi default akan digunakan")
        with open("tools/config.ini","w") as defaultConfig:
            defaultConfig.write("databaseFolderPath=\"database/\"\n")
            defaultConfig.write("databaseFileCount=8\n")
            defaultConfig.write("Nmax=100\n")
            defaultConfig.write("toGoldCost=15000\n")
            defaultConfig.write("menuPlayerCount=8\n")
            defaultConfig.write("menuAdminCount=8\n")
            defaultConfig.write("menuColumn=2\n")
            defaultConfig.write("menuRow=4\n")
            defaultConfig.write("menuVarName=[\"cari\",\"beli_tiket\",\"main\",\"refund\",\"kritik_saran\",\"best_wahana\",\"tiket_hilang\",\"exit\"]\n")
            defaultConfig.write("menuName=[\"Cari Wahana\",\"Beli Tiket\",\"Bermain\",\"Refund\",\"Kritik dan Saran\",\"Wahana Terbaik\",\"Laporan Kehilangan\",\"Keluar\"]\n")
            defaultConfig.write("menuAdminVarName=[\"signup\",\"cari_pemain\",\"tambah_wahana\",\"lihat_laporan\",\"tiket_pemain\",\"riwayat_wahana\",\"upgrade_gold\",\"exit\"]\n")
            defaultConfig.write("menuAdminName=[\"Sign Up\",\"Cari Pemain\",\"Wahana Baru\",\"Lihat Kritik Saran\",\"Lihat Tiket\",\"Riwayat Wahana\",\"Upgrade ke Gold\",\"Keluar\"]")

    with open("tools/config.ini") as configFile:
        for i in range(12):
            strCheck = configFile.readline().rstrip()
            for j in range(200): # 200 bisa di konfig
                try:
                    if (strCheck[j] == "="):
                        startIndex =  j + 1
                except IndexError:
                    endIndex = j
                    break
            config[i] = strCheck[startIndex:endIndex]
    return config

## Fungsi stringConfigToArray
# Merubah suatu string dengan cara tulis tertentu menjadi array of string
def stringConfigToArray(str1,maxCount):
    array = ["" for i in range(maxCount)]
    indexArray = [0 for i in range(2*maxCount)]
    counter = 0
    for i in range(200): # 200 bisa di konfig
        try:
            if (str1[i] == "\""):
                if (counter % 2):
                    indexArray[counter] = i
                else:
                    indexArray[counter] = i + 1
                counter += 1
        except IndexError:
            break
    for i in range(maxCount):
         array[i] = str1[indexArray[2*i]:indexArray[2*i+1]]
    return array

# FUNGSI KONVERSI TANGGAL
############################################################################

############################# Fungsi spesifik ##############################
###### Modul login & signup ######
## Fungsi hash dan lcg
# >> Desainer & Koder : Tanur Rizaldi Rahardjo / 16519525
# >> Digunakan pada modul login dan signup
# Fungsi rng menggunakan sistem linear congruence generator sederhana
# Fungsi hash menggunakan rng untuk membuat salt
# Random number generator sederhana dengan definisi fungsi
def lcg(m,a,b,s):
    if a:
        s = (a * s + b) % m
    else:
        return s
    return lcg(m,a-1,b,s)

# !!! st1 dan st2 tidak komutatif
def hash(st1,st2):
    hashedst1 = sha512(str(st1).encode('utf-8')).hexdigest()
    s = lcg(16,50,1,ord(str(st1)[0])) # Digunakan char pertama st1 sebagai seed pseudo rng
    if (s % 2):
        salted = hashedst1 + st2
    else:
        salted = st2 + hashedst1
    hashed = sha512(salted.encode('utf-8')).hexdigest()
    return hashed
#################################


####### Modul bestwahana ########
## Fungsi selectionSort
# >> Desainer & Koder : Tanur Rizaldi Rahardjo / 16519525
# >> Digunakan pada modul bestwahana
# Sort maksimum terdepan
# Digunakan kembali Selection sort yang diimplementasikan pada NIM sort pada soal sortmhs.py
def selectionSort(unsortedArray,N,secondIndex="Null"):
    if (secondIndex == "Null"):
        for i in range(N):
            sortedArray = unsortedArray[i]
            for j in range(i+1,N):
                if (sortedArray < unsortedArray[j]):
                    unsortedArray[i], unsortedArray[j] = unsortedArray[j], unsortedArray[i]
        sortedArray = unsortedArray
        return sortedArray
    else:
        for i in range(N):
            sortedArray = unsortedArray[i][secondIndex]
            for j in range(i+1,N):
                if (sortedArray < unsortedArray[j][secondIndex]):
                    unsortedArray[i], unsortedArray[j] = unsortedArray[j], unsortedArray[i]
        sortedArray = unsortedArray
        return sortedArray
#################################

############################################################################

############################ Load config ###################################
### Pembacaan konfigurasi
# Inisiasi variabel konfigurasi dengan membaca config.ini
config = loadConfig()
# Konfigurasi umum
databaseFolderPath = config[0].replace("\"","")
databaseFileCount = int(config[1])
Nmax = int(config[2])
toGoldCost = int(config[3])
menuPlayerCount = int(config[4])
menuAdminCount = int(config[5])
menuColumn = int(config[6])
menuRow = int(config[7])
# Konfigurasi array
menuVarName = stringConfigToArray(config[8],menuPlayerCount)
menuName = stringConfigToArray(config[9],menuPlayerCount)
menuAdminVarName = stringConfigToArray(config[10],menuAdminCount)
menuAdminName = stringConfigToArray(config[11],menuAdminCount)
# Pengecekan apakah konfigurasi menu* valid
if (menuRow*menuColumn < menuPlayerCount) and (menuRow*menuColumn < menuAdminCount):
    print("Error, Konfigurasi menu tidak valid")
    exit()
