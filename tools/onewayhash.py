from pandas import *
from hashlib import *

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
    if (s % 2):
        salted = hashedst1 + st2
    else:
        salted = st2 + hashedst1
    hashed = sha512(salted.encode('utf-8')).hexdigest()
    return hashed

# Main
username, password = [], []

isFileExist = False
while not isFileExist:
    print("File database user : ", end="")
    st = input()
    try:
        fl = read_csv(st)
        isFileExist = True
    except FileNotFoundError:
        print("Error: File Not Found ({})".format(st))

if (len(fl.loc[0,"Password"]) == 128):
    print("File sudah dihash")
else:
    for i in range(len(fl)):
        username.append(fl.loc[i,"Username"])
        password.append(fl.loc[i,"Password"])

    for i in range(len(fl)):
        fl.loc[i,"Username"] = username[i]
        fl.loc[i,"Password"] = hash(username[i],password[i])
    fl.to_csv(st)

input("Press any key to continue")
