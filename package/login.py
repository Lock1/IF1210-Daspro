from package.base import *
from hashlib import *

def login(user):
    notlogged = True
    passwordbenar = False
    while notlogged:
        print("Masukkan username: ", end="")
        inputusername = input()
        print("Masukkan password: ", end="")
        inputpassword = input()
        print()

        ##### Pengecekan Password #####
        # Salt & Hash
        # Random number generator sederhana dengan definisi fungsi
        def lcg(m,a,b,s):
            if a:
                s = (a * s + b) % m
            else:
                return s
            return lcg(m,a-1,b,s)

        # st1 dan st2 tidak komutatif
        def hash(st1,st2):
            hashedst1 = sha512(str(st1).encode('utf-8')).hexdigest()
            s = lcg(16,50,1,ord(str(st1)[0])) # Digunakan char pertama st1 sebagai seed pseudo rng
            if s % 2:
                salted = hashedst1 + st2
            else:
                salted = st2 + hashedst1
            hashed = sha512(salted.encode('utf-8')).hexdigest()
            return hashed

        # Database find
        inputpassword = hash(inputusername,inputpassword)
        for i in range(99):
            if inputusername == user[i][3] and inputpassword == user[i][4]:
                notlogged = False
                passwordbenar = True
                username = user[i][3]
                break

        # Validator
        if not passwordbenar:
            print("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi!")
        ##### Akhir bagian pengecekan #####

    print("Selamat bersenang-senang, {}!".format(username))
    return username
    # End of function
