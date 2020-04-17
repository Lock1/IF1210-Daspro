# Modul login
# Desainer
# Tanur Rizaldi Rahardjo / 16519525 / 17 April 2020

# Coder
# Tanur Rizaldi Rahardjo / 16519525 / 17 April 2020

# Tester
#


####### Algoritma #######
from package.base import *
from hashlib import *

##### Fungsi Hash #####
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
    if s % 2:
        salted = hashedst1 + st2
    else:
        salted = st2 + hashedst1
    hashed = sha512(salted.encode('utf-8')).hexdigest()
    return hashed
#######################

def login(user,N):
    notlogged, passwordbenar = True, False
    while notlogged:
        print("Masukkan username: ", end="")
        inputusername = input()
        print("Masukkan password: ", end="")
        inputpassword = input()
        print()
        ##### Pengecekan Password #####
        # Pencarian informasi pada database
        inputpassword = hash(inputusername,inputpassword)
        for i in range(N):
            if (inputusername, inputpassword) == (user[i][3], user[i][4]):
                notlogged, passwordbenar = False, True
                nama, username, role, status = user[i][0], user[i][3], user[i][5], user[i][7]
                break

        # Penulisan pada layar ketika password salah
        if not passwordbenar:
            print("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi!")
        ##### Akhir bagian pengecekan #####

    print("Selamat bersenang-senang, {}!\n".format(nama))
    return (nama, username, role, status)
