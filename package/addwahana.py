# Modul addwahana
# Desainer
# Tanur Rizaldi Rahardjo / 16519525 / 17 April 2020

# Coder
# Tanur Rizaldi Rahardjo / 16519525 / 17 April 2020

# Tester
#


def tambahWahana(wahana,N):
    # Meminta input user
    print("Masukkan Informasi Wahana yang ditambahkan:")
    print("Masukkan ID Wahana: ", end="")
    newID = input()
    print("Masukkan Nama Wahana: ", end="")
    newName = input()
    print("Masukkan Harga Tiket: ", end="")
    newCost = input()
    print("Batasan umur: ", end="")
    newAge = input()
    print("Batasan tinggi badan: ", end="")
    newHeight = input()
    print()
    print("Info wahana telah ditambahkan!")

    # Update
    for i in range(N):
        if wahana[i][0] == "~~~":
            wahana[i] = [newID,newName,newCost,newAge,newHeight]
            wahana[i+1][0] = "~~~"
            break
    return wahana
    # End of function
