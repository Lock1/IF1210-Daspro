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
        print("\n")


        ##### Checking Sequence #####
        # Salt & Hash
        #// salt use pseudo random + key generator for seed, optional rsa // seems shit using rsa on offline app but whatever


        # Database find

        #// if found then notlogged false and pull user information


        # Flag set // pull every information about user, may few or everything

        ##### End of Sequence #####
    # End of function
