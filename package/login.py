# Login

# pre defined xinput()

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
        #// salt use pseudo random + key generator for seed, optional rsa // seems shit using rsa on offline app but whatever


        # Database find

        #// if found then notlogged false and pull user information

        # Validator
        if (password benar) # tambah kondisi
            break
        else
            print("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi!")
        ##### End of Sequence #####

    # Flag set // pull every information about user, may few or everything

    print("Selamat bersenang-senang, {}!".format(isi variabel username disini))
    # End of function
