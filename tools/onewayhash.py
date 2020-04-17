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
    if s % 2:
        salted = hashedst1 + st2
    else:
        salted = st2 + hashedst1
    hashed = sha512(salted.encode('utf-8')).hexdigest()
    return hashed

# Main
usr, pwd = [], []
print("File database user : ", end="")
st = input()
fl = read_csv(st)

for i in range(len(fl)):
    usr.append(fl.loc[i,"Username"])
    pwd.append(fl.loc[i,"Password"])

for i in range(len(fl)):
    fl.loc[i,"Username"] = usr[i]
    fl.loc[i,"Password"] = hash(usr[i],pwd[i])

fl.to_csv(st)
