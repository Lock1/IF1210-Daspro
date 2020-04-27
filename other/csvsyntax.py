from pandas import *
import csv

memu = []
memp = []

with open("User.csv", newline="") as file:
    cs = csv.reader(file)
    cs.__next__() # next sequence for csvreader object
    for row in cs:
        print("{:30} {:15}".format(row[3], row[4]))
        memu.append(row[3])
        memp.append(row[4])

with open("User.csv", newline="") as file:
    cs = csv.writer(file)
    cs.__next__()
    for row in cs:
