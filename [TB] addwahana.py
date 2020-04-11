# add wahana

# pre defined xinput() and update()

def addWahana():
    # no restriction, filter admin / non admin at main loop
    # variables
    newID = ""
    newname = ""
    newcost = 0
    newage = ""
    newheight = ""

    # Meminta input user
    print("Masukkan Informasi Wahana yang ditambahkan:")

    print("Masukkan ID Wahana: ", end="")
    newID = xinput()
    print()     # newline
    print("Masukkan Nama Wahana: ", end="")
    newName = xinput()
    print()
    print("Masukkan Harga Tiket: ", end="")
    newcost = xinput()
    print()
    print("Batasan umur: ", end="")
    newage = xinput()
    print()
    print("Batasan tinggi badan: ", end="")
    newheight = xinput()
    print("\n")
    print("Info wahana telah ditambahkan!")

    # update
    # call update()


    # end of function
