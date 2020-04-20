#Program Read riwayat wahana
#Hizkia R. 16519515, 20 April 2020

#Kamus
#i=int
#N=string


#Algoritma


#pertama input id wahana
import csv

N=input("Masukkkan ID Wahana: ")
with open('Penggunaan.csv','r') as f:
    reader=csv.reader(f,delimiter=',')
    row=next(reader)
    i=0
    for row in reader:
        if row[2]==N: #menyocokan hasil input dengan data yang ada
            print(row[1],end="")
            print("|",end="")
            print(row[0],end="")
            print("|",end="")
            print(row[3])
            i+=1
    if i==0:
        print("Maaf, ID yang anda masukkan salah")
