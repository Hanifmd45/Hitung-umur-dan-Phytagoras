import datetime as waktu

#Function untuk input waktu kelahiran dan menghitung umur
def tahun_lahir():
    #input tanggal_kelahiran,bulan_kelahiran,dan tahun_kelahiran
    tanggal_kelahiran, bulan_kelahiran, tahun_kelahiran = map(int, input("Masukan tanggal lahir: ").split("-")) 
    #variabel penampung hasil output dari tanggal_kelahiran,bulan_kelahiran,dan tahun_kelahiran
    waktu_lahir = waktu.date(tahun_kelahiran,bulan_kelahiran,tanggal_kelahiran)
    #varibael untuk menampung tanggal,bulan,dan tahun sekarang
    waktu_sekarang = waktu.date.today()
    #Operasi untuk menghitung umur,bulan dari sisa umur,dan hari dari sisa umur
    umur_hari = waktu_sekarang - waktu_lahir
    my_umur = umur_hari.days // 365
    my_umur_bulan_sisa = (umur_hari.days % 365) // 30
    my_umur_hari_sisa = (umur_hari.days % 365) % 30
    #variabel untuk menampung hasil output dan operasi
    hasil = f"Saya lahir pada hari {waktu_lahir:%A} {tanggal_kelahiran} {waktu_lahir:%B} {waktu_lahir:%Y} \nArtinya saya berusia {my_umur} tahun {my_umur_bulan_sisa} bulan {my_umur_hari_sisa} hari"

    return hasil


