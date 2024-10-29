import math

#Function untuk menghitung rumus phytagoras
def phytagoras():
    #menginputkan sisi_1 dan sisi_2
    sisi_1= int(input("Masukan sisi 1: "))
    sisi_2 = int(input("Masukan sisi 2: "))
    #rumus phytagoras
    hasil =  math.sqrt( sisi_1**2 + sisi_2**2)
    #Variabel penampung hasil dari penghitungan phytagoras
    result = f"\n\nHari ini saya akan menghitung rumus phytagoras \npada sebuah sisi segitiga dengan sisi siku-siku {sisi_1} & {sisi_2} \nmaka panjang sisi miringnya adalah {int(hasil)}"

    return result