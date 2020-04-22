#Hizkia Raditya Pratama Roosadi
#Program kritik & saran

#kamus
#ID: string (ID wahana)
#tgl: string (tanggal kritik dan saran diterima)
#kritik: string (kritik dan saran)
#data: tuple data untuk csv

#algoritma
#asumsi input selalu valid
import csv

#input ketiga parameter
ID=input("Masukkan ID Wahana: ")
tgl=input("Masukkan tanggal pelaporan: ")
kritik=input("Kritik/saran Anda: ")

#menyimpan ketiga parameter ke satu tuple dipisah dengan koma
data=[ID,tgl,kritik]

#menulis tuple tersebut ke row baru dari csv
with open(r'kritiksaran.csv','a') as f:
    writer=csv.writer(f)
    writer.writerow(data)

print("Kritik dan saran Anda kami terima")
