############################## Informasi Modul ##############################
## Modul login
# Desainer
# Tanur Rizaldi Rahardjo / 16519525 / 17 April 2020

# Coder
# Tanur Rizaldi Rahardjo / 16519525 / 17 April 2020

# Tester
# Finna Alivia Nabila / 16519125 / 26 April 2020

######### Kamus #########
### Argumen yang direquest oleh fungsi
# user      : 2D Matrix of strings
# N         : Integer

### Kamus Internal
# isPasswordBenar           : Boolean
# inputPassword             : String
# inputUsername             : String
# isPasswordInputNotValid   : Boolean
# isUserInputNotValid       : Boolean
# isUsernameExist           : Boolean
# userInformationIndex      : Integer
# role                      : String
# status                    : String

### Kamus informasi yang direturn
# nama          : String
# username      : String
# admin         : Boolean
# gold          : Boolean

###### Spesifikasi ######
# requestLogin  : (2D Matrix of strings, Integer) -> (String, String, Boolean, Boolean)
#############################################################################

############################### Algoritma ################################
from package.base import *

def requestLogin(user,N=Nmax):
    ## Loop permintaan login ##
    isPasswordBenar = False
    while not isPasswordBenar:
        # Loop untuk meminta input username & password
        inputUsername = input("Masukkan username: ")
        inputPassword = input("Masukkan password: ")
        isUserInputNotValid, isPasswordInputNotValid = (inputUsername + " ").isspace(), (inputPassword + " ").isspace()
        # Diperlukan pengecekan karena hash() tidak memiliki handler untuk karakter spasi,
        # dan karakter spasi dianggap bukanlah karakter yang valid untuk password
        while (isUserInputNotValid) or (isPasswordInputNotValid):
            print()
            print("Masukkan tidak valid")
            inputUsername = input("Masukkan username: ")
            inputPassword = input("Masukkan password: ")
            isUserInputNotValid, isPasswordInputNotValid = (inputUsername + " ").isspace(), (inputPassword + " ").isspace()
        print()

        ##### Pengecekan Password #####
        # Pencarian informasi pada database
        inputPassword = hash(inputUsername, inputPassword)
        # Pemanggilan isExistOnDatabase dengan mode indexReturn
        isUsernameExist, userInformationIndex = isExistOnDatabase(user,3,inputUsername,True)
        if isUsernameExist:
            if (user[userInformationIndex][4] == inputPassword):
                isPasswordBenar = True
                # Pengambilan nilai dari database yang berhubungan dengan username dan password yang benar
                nama, username, role, status = user[userInformationIndex][0], user[userInformationIndex][3], user[userInformationIndex][5], user[userInformationIndex][7]
        ##### Akhir bagian pengecekan #####
        # Penulisan pada layar ketika password salah
        if not isPasswordBenar:
            print("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi!")
    ## Akhir Loop permintaan login ##

    # Pengkonversian informasi ke boolean
    admin, gold = False, False
    if (role == "Admin"):
        admin = True
    if (status == "1"):
        gold = True

    # Returning print
    print("Selamat bersenang-senang, {}!".format(nama))
    print()
    return (nama, username, admin, gold)

########################### End of function ##############################
