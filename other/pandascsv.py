from pandas import *

print("File :", end="")
st = input()

usr, pwd = [], []

fl = read_csv(st)
for i in range(len(fl)):
    usr.append(fl.loc[i,"Username"])
    pwd.append(fl.loc[i,"Password"])


print(fl)
print("Username \n",usr)
print("Password \n",pwd)
