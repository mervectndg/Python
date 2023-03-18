print(" 2.Gün Ödevleri ")

ogrenciler=["Ayşe Yıldız","Ali Soylu"]
print(ogrenciler.index("Ali Soylu"))

def isim_ekle():
    isim = input("Eklememek istediğiniz öğrencinin adını giriniz: \n").capitalize() #büyük baş harflekaydetmesini sağlıyor
    soyisim = input("Eklememek istediğiniz öğrencinin soyadını giriniz: \n").capitalize()
    isimikilisi = (isim+" "+soyisim)
    return isimikilisi

def isim_sil():
    isim = input("Silmek istediğiniz öğrencinin adını giriniz: \n").capitalize() #büyük baş harflekaydetmesini sağlıyor
    soyisim = input("Silmek istediğiniz öğrencinin soyadını giriniz: \n").capitalize()
    isimikilisi = (isim+" "+soyisim)
    return isimikilisi

def ogrenci_ekle():
    isimikilisi = isim_ekle()
    ogrenciler.append(isimikilisi)
    print(ogrenciler)

ogrenci_ekle()

print("*********************")

def ogrencileri_ekle():
    ogrenci = isim_ekle()
    ogrenci1 = isim_ekle()
    ogrenciler.extend([ogrenci,ogrenci1])
    print(ogrenciler)

#ogrencileri_ekle()

print("*********************")

def ogrenci_sil():
    print(ogrenciler)
    isimikilisi = isim_sil()
    ogrenciler.remove(isimikilisi)

ogrenci_sil()

print("****************")

def tum_liste():
    for i in ogrenciler:
        print(i)

tum_liste()
   
print(ogrenciler)

def ogrenci_numarasi():
    isim = input("Numarasını öğrenmek istediğiniz öğrencinin adını giriniz: \n").capitalize() #büyük baş harflekaydetmesini sağlıyor
    soyisim = input("Numarasını öğretnmek istediğiniz öğrencinin soyadını giriniz: \n").capitalize()
    isimikilisi = (isim+" "+soyisim)
    return ogrenciler.index(isimikilisi)

value=ogrenci_numarasi()
print(value)

def ogrencileri_sil():
    print(ogrenciler)
    kacDefa = int(input("Silmek istediğiniz öğrenci sayısı: \n"))
    while kacDefa > 0:
        ogrenci_sil()
        kacDefa -=1 

ogrencileri_sil()
