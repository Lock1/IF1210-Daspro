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
# Function  : isExistOnDatabase(2D Matrix of string, Integer, String, Integer, 2x Boolean, Function, String) -> (Boolean) or (Boolean, Integer)  [TBU]
# Function  : loadConfig() -> (Array of strings)
# Function  : stringConfigToArray(String) -> (Array of strings)
# Function  : lcg(4x Integer) -> (Integer)
# Function  : hash(String, String) -> (String)
# Function  : selectionSort(Array of integer) -> (Array of integer)
# Procedure : rawPrint(String)
# Procedure : printMenu(Integer, Integer, Integer, Integer, Array of strings, Array of strings)
# [TBU] replaceColumn
# Function : isValidDateString(String) -> (Boolean)
# [TBU] dateInput()
# [TBU] idInput()
# [TBU] validator
# [TBU] tiketUpdate
#############################################################################

# Inisiasi dasar
from hashlib import *
capitalCharList = ['' for i in range(26)]
numberCharList = ['' for i in range(10)]

for i in range(26):
    capitalCharList[i] = chr(i+65)

for i in range(10):
    numberCharList[i] = chr(i+48)

# --------------------------- Definisi fungsi ----------------------------- #

############################### Fungsi Dasar ################################

############ Fungsi validasi ###########
# Pengecekan string untuk mencegah ketidakvalidan tanggal
def isValidDateString(str1):
    # Mark
    str1 = str1 + "\n"
    i, j = 0, 0
    while True:
        if (str1[i] == "\n"):
            break
        if (str1[i] == "/"):
            j += 1
        i += 1
    if (j == 2):
        return True
    else:
        return False

# Pengecekan string ID Wahana
def isValidIDString(str1):
    # Mark
    str1 = str1 + "\n"
    i = 0
    while True:
        if (str1[i] == "\n"):
            break
        if (i < 3) and (str1[i] not in capitalCharList):
            break
        if (i >= 3) and (str1[i] not in numberCharList):
            break
        i += 1
    if (i == 6):
        return True
    else:
        return False

# Pengecekan kevalidan umur
def isValidAgeString(str1):
    if (str1 in ["semua umur","dewasa","anak-anak"]):
        return True
    else:
        return False

############ Fungsi I/O dan string operation ############
## Fungsi xinput()
# xinput digunakan untuk input user dengan penambahan sebuah string >>> didepannya
def xinput(str1=""):
    if str1:
        print(str1)
    print(">>> ",end="")
    n = input()
    return n

## Fungsi posIntInput
# Meminta input integer positif secara paksa
# Jika tidak integer, input akan diulangi
def posIntInput(str1="",errorMsg=""):
    while True:
        n = input(str1)
        try:
            if (int(n) > 0):
                return int(n)
        except ValueError:
            if errorMsg:
                print(errorMsg)
            else:
                print("Masukan tidak diketahui")

## Fungsi dateInput
# Meminta input tanggal dengan penulisan yang valid
# Format spesifikasi "dd/mm/yyyy"
def dateInput(str1=""):
    while True:
        date = input(str1)
        if isValidDateString(date):
            return date
        else:
            print("Tanggal tidak valid.")

## Fungsi idInput
# Meminta input wahana ID dengan pengecekan
# Format wahana ID, AAANNN dengan A adalah huruf kapital dan N adalah angka
def idInput(str1=""):
    if str1:
        stringToPrint = str1
    else:
        stringToPrint = "Masukkan ID Wahana: "
    while True:
        id = input(stringToPrint)
        if isValidIDString(id):
            return id
        else:
            print("ID Wahana tidak valid.")

## Fungsi umurInput
# Meminta input umur dengan pengecekan
def umurInput(str1=""):
    while True:
        age = input(str1)
        if isValidAgeString(age):
            return age
        else:
            print("Umur tidak valid.")
            print("Tuliskan salah satu batasan umur berikut:")
            print("1. semua umur")
            print("2. dewasa")
            print("3. anak-anak")


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
def printMenu(row,column,maxMenuIndex,varArray,nameArray,isAdmin=False):
    if not isAdmin:
        for i in range(row):
            for j in range(column):
                if ((i + row*j) >= maxMenuIndex):
                    rawPrint("")
                else:
                    rawPrint("{}. {:20} {:17} ".format((i+1+row*j),nameArray[i+row*j],addBracket(varArray[i+row*j])))
            print()
    else:
        for i in range(row):
            for j in range(column):
                if ((i + row*j) >= maxMenuIndex):
                    rawPrint("")
                else:
                    rawPrint("{}. {:20} {:17} ".format(chr(64+(i+1+row*j)),nameArray[i+row*j],addBracket(varArray[i+row*j])))
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










# ------------- Pendefinisian fungsi database dan fungsi lain ------------- #
# Fungsi pada bagian ini diletakkan setelah pemanggilan loadconfig dikarenakan
# fungsi dibawah ini menggunakan default argumen yang bergantung pada variabel
# yang terdapat pada config.ini / file konfigurasi.
########### Fungsi database ###########
## Fungsi appendDatabase
# Digunakan untuk menambahkan informasi baru pada bagian bawah database / replace informasi dimark
def appendDatabase(database,insertArray,N=Nmax):
    for i in range(N):
        if (database[i][0] == "~~~"):
            database[i] = insertArray
            if (i != (N - 1)):
                database[i+1][0] = "~~~"
            break
    return database

## Fungsi isExistOnDatabase
# Digunakan untuk mengecek apakah ada data yang sama antara
# database dengan kolom index dan search, jika ada return True
# Fungsi ini memiliki 2 mode return, mode default akan mengembalikan True atau False
# berdasarkaan search ada atau tidak dan mode indexReturn untuk mengembalikan tuple (Boolean, Integer)
# dengan boolean adalah ada tidaknya search dan integer adalah indeks pada database
def isExistOnDatabase(database,searchColumnIndex,search,indexReturn=False,N=Nmax):
    for i in range(N):
        if (database[i][0] == "~~~"):
            if (search == "~~~") and indexReturn:
                return (True,i)
            break
        if (database[i][searchColumnIndex] == search):
            if indexReturn:
                return (True,i)
            else:
                return True
    if indexReturn:
        return (False,"null")
        # Ketika fungsi diminta untuk mode return index dan gagal menemukan
    # Jika tidak ada data yang sama, kembalikan false
    return False

## Fungsi replaceColumn
# Fungsi replaceColumn digunakan untuk mengganti informasi pada kolom tertentu
# Semua database digunakan Matrix of String, dan replaceColumn akan mengharuskan
# konversi non string ke string.
# replaceArray = [replaceColumnIndex,newColumn] -> Single Mode
# replaceArray = [[Array of Integer], [Array of Strings]] -> Multi Mode
def replaceColumn(database,dataRowIndex,replaceArray,multi=False,multiLength=0):
    # Jika digunakan tipe single
    if (not multi):
        database[dataRowIndex][replaceArray[0]] = str(replaceArray[1])
    # Mode multi
    else:
        for i in range(multiLength):
            database[dataRowIndex][replaceArray[0][i]] = str(replaceArray[1][i])
    return database

## Fungsi tiketUpdate
# Digunakan untuk mengupdate database tiket
def tiketUpdate(tiket,username,wahanaID,operator,tiketOperan,ticketGreaterThan=False,N=Nmax):
    updateExistingTicket = False
    for i in range(N):
        if (tiket[i][0] == "~~~"):
            break
        if (tiket[i][0] == username) and (tiket[i][1] == wahanaID):
            updateExistingTicket = True
            if (ticketGreaterThan) and (int(tiket[i][2]) >= tiketOperan):
                tiket[i][2] = str(operator(int(tiket[i][2]), tiketOperan))
            elif (not ticketGreaterThan):
                tiket[i][2] = str(operator(int(tiket[i][2]), tiketOperan))
            else:
                updateExistingTicket = False
            break
    return (tiket, updateExistingTicket)

# ------------------------------------------------------------------------- #
