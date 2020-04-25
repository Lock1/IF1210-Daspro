############################## Informasi Modul ##############################
# Modul buytiket
# Desainer
# Kevin Domenico Tantiyo / 16519205 / 24 April 2020

# Coder
# Kevin Domenico Tantiyo / 16519205 / 24 April 2020

# Tester
# Tanur Rizaldi Rahardjo / 16519525 / 24 April 2020


## Kamus


## Spesifikasi


#############################################################################
####### Algoritma #######
from package.base import *

# Pengecekan string untuk mencegah ketidakvalidan tanggal
def isValidDateString(str1):
    # Mark
    str1 = str1 + "\n"
    i = 0
    j = 0
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

def stringDateToArray(string):
    dateContainer = [0 for i in range(3)]
    indexArray = [0 for i in range(3)]
    # Mark
    string = string + "\n"
    # Loop pencarian indeks "/"
    i, j = 0, 0
    while True:
        if (string[i] == "\n"):
            indexArray[j] = i
            break
        if (string[i] == "/"):
            indexArray[j] = i
            j += 1
        i += 1
    date = int(string[0:indexArray[0]])
    month = int(string[(indexArray[0]+1):indexArray[1]])
    year = int(string[(indexArray[1]+1):indexArray[2]])
    dateContainer[0], dateContainer[1], dateContainer[2] = date, month, year
    return dateContainer

# Tidak ada pertimbangan untuk kabisat
def dateArrayToInteger(array):
    dateInteger = 365*array[2] + 30*array[1] + array[0]
    return dateInteger

def beliTiketUser(username,gold,user,wahana,tiket,discountFactor=goldDiscountMultiplier,N=Nmax):
    # Penulisan interface
    beliWahanaID = input("Masukkan ID wahana: ")
    beliTanggal = input("Masukkan tanggal hari ini: ")
    while not isValidDateString(beliTanggal):
        print("Tanggal tidak valid.")
        print()
        beliTanggal = input("Masukkan tanggal hari ini: ")

    beliTanggal = stringDateToArray(beliTanggal)
    beliTiket = intinput("Jumlah tiket yang dibeli: ")

    # Cek database user dan wahana
    (isUsernameExist, usernameIndex) = isExistOnDatabase(user,3,username,N,False,True)
    (isWahanaExist, wahanaIndex) = isExistOnDatabase(wahana,0,beliWahanaID,N,False,True)
    if isUsernameExist and isWahanaExist:
        userTanggalLahir = stringDateToArray(user[usernameIndex][1])
        arrayWahana = wahana[wahanaIndex]
        # [id wahana, nama wahana, harga, batas umur, batas tinggi]

        ### Prosedur dibawah hanya akan diproses ketika username exist dan wahana exist
        # Pengecekan umur
        beliTanggal = dateArrayToInteger(beliTanggal)
        userTanggalLahir = dateArrayToInteger(userTanggalLahir)
        userUmur = beliTanggal - userTanggalLahir
        batasUmur = 365*17
        isValidUmur, isValidTinggi = False, False
        if (arrayWahana[3] == "dewasa") and (batasUmur <= userUmur):
            isValidUmur = True
        elif (arrayWahana[3] == "anak-anak") and (batasUmur > userUmur):
            isValidUmur = True
        elif (arrayWahana[3] == "semua umur"):
            isValidUmur = True

        # Pengecekan tinggi
        if (int(arrayWahana[4]) <= int(user[usernameIndex][2])):
            isValidTinggi = True

        # Pemrosesan saldo & tiket
        if isValidUmur and isValidTinggi:
            if (not gold) and ((int(user[usernameIndex][6]) < (int(arrayWahana[2])*beliTiket))):
                print("Saldo Anda tidak cukup")
                print("Silakan mengisi saldo Anda")
            elif gold and (int(user[usernameIndex][6]) < (int(arrayWahana[2])*beliTiket*discountFactor)):
                print("Saldo Anda tidak cukup")
                print("Silakan mengisi saldo Anda")
            else:
                if gold:
                    user[usernameIndex][6] = str(int(int(user[usernameIndex][6]) - int(arrayWahana[2])*beliTiket*discountFactor))
                else:
                    user[usernameIndex][6] = str(int(int(user[usernameIndex][6]) - int(arrayWahana[2])*beliTiket))
                newTicket = [username, beliWahanaID, str(beliTiket)]
                tiket = appendDatabase(tiket,newTicket,N)
                print("Selamat bersenang-senang di {}.".format(arrayWahana[1]))
        else:
            print("Anda tidak memenuhi persyaratan untuk memainkan wahana ini.")
            print("Silakan menggunakan wahana lain yang tersedia.")
    else:
        print("Maaf terdapat kesalahan pada username atau ID wahana.")

    print()
    return (user, tiket)
