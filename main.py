from waktu_lahir import tahun_lahir
from menghitung_Phytagoras import phytagoras

def Nama():
    #menginputkan nama
    nama = str(input("Masukan Nama : "))
    #memanggil hasil output nama
    hasil =f"\nHallo Perkenalkan nama saya {nama}"
    return hasil

#Variabel untuk menampung nama
inputkan_nama = Nama
#variabel untuk menampung fungsi tahun lahir
tanggal_lahir = tahun_lahir
 #variabel untuk menampung fungsi phytagoras
menghitung_phytagoras = phytagoras
print(inputkan_nama(), tanggal_lahir(), menghitung_phytagoras())
