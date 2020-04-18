# Modul base
# Desainer
# Tanur Rizaldi Rahardjo / 16519525 / 17 April 2020

# Coder
# Tanur Rizaldi Rahardjo / 16519525 / 17 April 2020


####### Algoritma #######
### Modul dasar untuk fungsi umum ###
# Fungsi xinput()
# xinput digunakan untuk input user dengan penambahan sebuah string >>> didepannya
def xinput(str1=""):
    if not(str1 == ""):
        print(str1)
    print(">>> ",end="")
    n = input()
    return n

# fungsi konversi tanggal


# Fungsi input untuk integer
def intinput(str1=""):
    while True:
        n = input(str1)
        try:
            return int(n)
        except ValueError:
            print("Masukan tidak diketahui")

# Prosedur rawPrint
def rawPrint(str1):
    print(str1,end="")

# Fungsi addBracket
def addBracket(str1):
    bracketed = "(" + str1 + ")"
    return bracketed

# Prosedur printMenu
def printMenu(row,column,maxMenuIndex,varArray,nameArray):
    for i in range(row):
        for j in range(column):
            if ((i + row*j) >= maxMenuIndex):
                rawPrint("")
            else:
                rawPrint("{}. {:20} {:15} ".format((i+1+row*j),nameArray[i+row*j],addBracket(varArray[i+row*j])))
        print()

#
def loadConfig():
    config = ["" for i in range(12)]
    with open("config.ini") as configFile:
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

def stringConfigToArray(str1,maxCount):
    array = ["" for i in range(maxCount)]
    indexArray = [0 for i in range(2*maxCount)]
    counter = 0
    for i in range(200): # konfig
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
