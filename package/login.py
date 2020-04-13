# Login

# pre defined xinput()
# req system.os

def login():
    notlogged = True
    While notlogged:
        print("Masukkan username: ", end="")
        inputusername = xinput()
        print()
        print("Masukkan password: ", end="")
        inputpassword = xinput()
        # CLS untuk keamanan
        print("\n")


        ##### Checking Sequence #####
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

        #// if found then notlogged false and pull user information

        # Validator
        if (password benar) # tambah kondisi
            notlogged = False
        else
            print("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi!")
        ##### End of Sequence #####

    # Flag set // pull every information about user, may few or everything

    print("Selamat bersenang-senang, {}!".format(isi variabel username disini))
    # End of function
