############################## Informasi Modul ##############################
### Modul untuk fungsi yang umum ###
## Informasi tentang per fungsi akan dijelaskan pada komentar fungsi

## Spesifikasi & list untuk fungsi dan prosedur terdefinisi pada modul base
# Function  : xinput(String) -> (String)
# Function  : intinput(String) -> (Integer)
# Function  : addBracket(String) -> (String)
# Function  : databaseFilePath(String, String) -> (String)
# Function  : appendDatabase(2D Matrix of strings, Array of strings, Integer) -> (2D Matrix of strings)
# Function  : replaceChar(3x String) -> (String)
# Function  : isExistOnDatabase(2D Array of string, Integer, String, Integer, 2x Boolean, Function, String) -> (Boolean) or (Boolean, Integer)
# Function  : loadConfig() -> (Array of strings)
# Function  : stringConfigToArray(String) -> (Array of strings)
# Function  : lcg(4x Integer) -> (Integer)
# Function  : hash(String, String) -> (String)
# Function  : selectionSort(Array of integer) -> (Array of integer)
# Procedure : rawPrint(String)
# Procedure : printMenu(Integer, Integer, Integer, Integer, Array of strings, Array of strings)
#############################################################################


# --------------------------- Definisi fungsi ----------------------------- #

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

## Fungsi databaseFilePath
# Membuat string direktori database
def databaseFilePath(databaseFolderPath,databaseFilename=""):
    databasePath = databaseFolderPath + input(databaseFilename)
    return databasePath

def replaceChar(string,charFind,charReplace):
    # Mark
    string = string + "\n"
    ## Alternatif 1
    newString = ""
    # Jika string "" dianggap seperti array dinamis, Implementasikan
    # char newString[1000] atau semacamnya seperti pada C atau C++
    ## Alternatif 2
    # newString = ["" for i in range(1000)]
    # Maka hard limit untuk fungsi ini adalah string dengan 1000 char (atau 999 untuk C dikarenakan karakter terminasi)
    # Replace algorithm
    i, j = 0, 0
    while True:
        if (string[i] == "\n"):
            break
        elif (string[i] == charFind) and (charReplace == ""):
            i += 1
            continue
        elif (string[i] == charFind):
            newString[j] = charReplace
            j += 1
        else:
            ## Alternatif 1
            newString = newString + string[i]
            ## Alternatif 2
            # newString[j] = string[i]
            j += 1
        i += 1
    # Merge / join algorithm untuk alternatif 2
    #for i in range(1000):
    #    if (newString[i],newString[i+1],newString[i+2]) == ("","",""):
    #        # Mengurangi iterasi tidak berguna
    #        break
    #    if not newString[i]:
    #        for j in range(i,1000):
    #            newString[i+j] = newString[i+j+1]
    #            if (newString[i],newString[i+1],newString[i+2]) == ("","",""):
    #                break
    return newString


########### Fungsi database ###########
## Fungsi appendDatabase
# Digunakan untuk menambahkan informasi baru pada bagian bawah database / replace informasi dimark
def appendDatabase(database,insertArray,N):
    for i in range(N):
        if (database[i][0] == "~~~"):
            database[i] = insertArray
            if (i != (N - 1)):
                database[i+1][0] = "~~~"
            break
    return database

## Fungsi isExistOnDatabase
# Digunakan untuk mengecek apakah relasi antara database[][index] dan search
# dengan checkFunction benar, jika benar flagToBeToggled akan dinegasi dan direturn
# Argumen tambahan replace digunakan untuk mengganti database       # Note to self : check function dan replace belum digunakan secara maksimal
def isExistOnDatabase(database,index,search,N,flagToBeToggled=False,indexReturn=False,checkFunction=(lambda a,b: a==b),replace="Null"):
    for i in range(N):
        if (database[i][0] == "~~~"):
            if (search == "~~~") and indexReturn:
                return (True,i)
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
            defaultConfig.write("menuPlayerCount=9\n")
            defaultConfig.write("menuAdminCount=9\n")
            defaultConfig.write("menuColumn=3\n")
            defaultConfig.write("menuRow=3\n")
            defaultConfig.write("menuVarName=[\"cari\",\"beli_tiket\",\"main\",\"refund\",\"kritik_saran\",\"best_wahana\",\"tiket_hilang\",\"exit\"]\n")
            defaultConfig.write("menuName=[\"Cari Wahana\",\"Beli Tiket\",\"Bermain\",\"Refund\",\"Kritik dan Saran\",\"Wahana Terbaik\",\"Laporan Kehilangan\",\"Keluar\"]\n")
            defaultConfig.write("menuAdminVarName=[\"signup\",\"cari_pemain\",\"tambah_wahana\",\"lihat_laporan\",\"tiket_pemain\",\"riwayat_wahana\",\"upgrade_gold\",\"topup\",\"exit\"]\n")
            defaultConfig.write("menuAdminName=[\"Sign Up\",\"Cari Pemain\",\"Wahana Baru\",\"Lihat Kritik Saran\",\"Lihat Tiket\",\"Riwayat Wahana\",\"Upgrade ke Gold\",\"Top Up Saldo\",\"Keluar\"]\n")

    with open("tools/config.ini") as configFile:
        for i in range(12):
            strCheck = configFile.readline()
            j = 0
            while True:
                if (strCheck[j] == "\n"):
                    endIndex = j
                    break
                if (strCheck[j] == "="):
                    startIndex =  j + 1
                j += 1
            config[i] = strCheck[startIndex:endIndex]
    return config

## Fungsi stringConfigToArray
# Merubah suatu string dengan cara tulis tertentu menjadi array of string
def stringConfigToArray(str1,maxCount):
    array = ["" for i in range(maxCount)]
    indexArray = [0 for i in range(2*maxCount)]
    str1 += "\n" # Mark
    counter, i = 0, 0
    while True:
        if (str1[i] == "\n"):
            break
        if (str1[i] == "\""):
            if (counter % 2):
                indexArray[counter] = i
            else:
                indexArray[counter] = i + 1
            counter += 1
        i += 1
    for j in range(maxCount):
         array[j] = str1[indexArray[2*j]:indexArray[2*j+1]]
    return array

# FUNGSI KONVERSI TANGGAL
############################################################################

############################# Fungsi spesifik ##############################
###### Modul login & signup ######
## Fungsi hash dan lcg
# >> Desainer & Koder : Tanur Rizaldi Rahardjo / 16519525
# >> Tester           : Kevin Domenico Tantiyo / 16519205
# >> Digunakan pada modul login dan signup
# Fungsi rng menggunakan sistem linear congruence generator sederhana
# Fungsi hash menggunakan rng untuk membuat salt
# Random number generator sederhana dengan definisi fungsi

######### Kamus #########
### Argumen yang direquest oleh fungsi
# st1   : String
# st2   : String

## Kamus Internal
# hashedst1     : String
# s             : Integer
# salted        : String

## Kamus informasi yang direturn
# hashed : String

###### Spesifikasi ######
# lcg    : (4x Integer) -> Integer
# hash   : (String, String) -> (String)

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

# ------------------------------------------------------------------------- #






# ---- Fungsi yang dicall & prosedur yang dijalan ketika modul diload ----- #

############################ Load config ###################################
### Pembacaan konfigurasi
# Inisiasi variabel konfigurasi dengan membaca config.ini
config = loadConfig()
# Konfigurasi umum
# databaseFolderPath = config[0].replace("\"","") # Jika tidak diperbolehkan dengan string method replace
databaseFolderPath = replaceChar(config[0],"\"","")
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
############################################################################


# Hard coded configuration
databaseColumn = [8,5,4,4,3,4,4,4]
refundMultiplier = 0.5
goldDiscountMultiplier = 0.5
# [user, wahana, pembelian, penggunaan, tiket, refund, kritiksaran, kehilangan]

# Pengecekan apakah konfigurasi menu* valid
if (menuRow*menuColumn < menuPlayerCount) and (menuRow*menuColumn < menuAdminCount):
    print("Error, Konfigurasi menu tidak valid")
    exit()

# ------------------------------------------------------------------------- #
