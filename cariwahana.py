#Program cari wahana
#Hizkia R. 16519515, 12 April 2020

#Kamus
#batsTinggi {Batas tinggi}: integer
#batasUmur {Batas umur}: integer

#General interface agar pengguna tahu apa yang harus di input
import csv
print ("Jenis batasan umur:")
print("1. Anak-anak (<17 tahun)")
print("2. Dewasa (>=17 tahun)")
print("3. Semua umur")
print("")
print("Jenis batasan tinggi badan:")
print("1. Lebih dari 170 cm")
print("2. Tanpa batasan")


#Algoritma pemilihan utama
batsUmur=input("Batasan umur pemain:")
if (batsUmur!="1" and batsUmur!="2" and batsUmur!="3"):
    while (batsUmur!="2" and batsUmur!="1"):
        print("Batasan umur tidak valid!")
        batsUmur=input("Batasan umur pemain:")
        if batsUmur=="3" or batsUmur=="2" or batsUmur=="1":
            break
    
batsTinggi=input("Batasan tinggi badan:")
if(batsTinggi!="1" and batsTinggi!="2"):
    while (batsTinggi!="2" and batsTinggi!="1"):
        print("Batasan tinggi tidak valid!")
        batsTinggi=input("Batasan tinggi pemain:")
        if batsTinggi=="2" or batsTinggi=="1":
            break



#algoritma untuk menghasilkan hasil search sesuai pilihan kategori
with open('Wahana.csv', 'r') as f:
    reader=csv.reader(f,delimiter=',')
    row=next(reader)
    i=0
    for row in reader:
        if batsUmur=="1" and batsTinggi=="1":
            if int(row[4])>=170 and row[3]=="anak-anak":
                print(row[0],end="")
                print("|",end="")
                print(row[1],end="")
                print("|",end="")
                print(row[2])
                i+=1
        elif batsUmur=="1" and batsTinggi=="2":
            if row[3]=="anak-anak":
                print(row[0],end="")
                print("|",end="")
                print(row[1],end="")
                print("|",end="")
                print(row[2])
                i+=1
        elif batsUmur=="2" and batsTinggi=="1":
            if int(row[4])>=170 and row[3]=="dewasa":
                print(row[0],end="")
                print("|",end="")
                print(row[1],end="")
                print("|",end="")
                print(row[2])
                i+=1
        elif batsUmur=="2" and batsTinggi=="2":
            if row[3]=="dewasa":
                print(row[0],end="")
                print("|",end="")
                print(row[1],end="")
                print("|",end="")
                print(row[2])
                i+=1
        elif batsUmur=="3" and batsTinggi=="1":
            if int(row[4])>=170 and row[3]=="semua umur":
                print(row[0],end="")
                print("|",end="")
                print(row[1],end="")
                print("|",end="")
                print(row[2])
                i+=1
        elif batsUmur=="3" and batsTinggi=="2":
            if row[3]=="semua umur":
                print(row[0],end="")
                print("|",end="")
                print(row[1],end="")
                print("|",end="")
                print(row[2])
                i+=1

            
    if i==0:
        print("Tidak ada wahana yang sesuai dengan pencarian anda.")
        
        

   
