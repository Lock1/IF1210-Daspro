import csv
# basic loader scheme
s = csv.reader(open('user.csv'))
d = ["" for i in range(100)]
s.__next__()
for i in range(99):
    tp = s.__next__()
    if tp[0] == "~~~":
        print("loaded")
        break
    else:
        d[i] = tp
