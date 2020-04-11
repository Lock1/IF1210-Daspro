# exit

def keluar():
    ans = ""
    print("Apakah anda mau melakukan penyimpanan file yang sudah dilakukan (Y/N) ? ", end="")
    ans = xinput()
    if ans == "Y":
        save()
    exit()
    # end of function
