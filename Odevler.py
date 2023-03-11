# Python 1.Ders Ödevleri;
# 1. Python'da Veri Tiplerini araştırınız, her bir veri tipi için kendi cümlelerinizle açıklamalar yazınız. 

# str = Metin tipleri için.
# int, float, complex = Sayısal tiplerdir. Tam sayı, ondalıklı sayı ve karmaşık sayı türleri içindir.
# list, tuple, range = Dizi tipleridir. Listeleme, listede değişime izin vermeme ve istediğimiz aralıklarla çalışması içindir.
# dict = Adresleme tipidir. İsim= Merve, Yaş= 24 gibi.
# set, frozenset = Küme tipleridir. Değiştirebilen ve değiştirilemeyen küme elemanlarının belirilmesidir.
# bool = Mantıksal tiptir. Doğru veya yanlış için kullanılır.
# bytes, bytearray, memoryview = ? (Anlayamadım )

# 2. Kodlama.io sitesinde değişken olarak kullanıldığını düşündüğünüz verileri, veri tipleriyle birlikte örneklendiriniz.

# Kursların isimleri, ödevlerin açıklamaları, ders programının açıklamaları gibi bölümler metinsel ifadelerdir. Örneğin;
# kursAdi=”(2023) Yazılım Geliştirme Yetiştirme Kampı – Python & Selenium”

# Kategori ve Eğitmen bölümleri dizi tipidir. Örneğin;
# egitmen=[“Tümü”,”Engin Demirog”,“Halit Enes Kalaycı”]

# Kursların tamamlanma ifadeleri de sayısal verilerdir. Örneğin;
# kursTamamlamaYuzdesi= %100

# 3. Kodlama.io sitesinde şart blokları kullanıldığını düşündüğünüz kısımları örneklendiriniz ve Python dilinde bu örnekleri koda dökünüz.

# Ödevlerin tamamladıktan sonra bitir ve devam etten sonra ders tamamlamaların yüzdelerinin değişmesi örnek verilebilir.


kurs=0 

if kurs>=1:
    print("Kursun %25'ini tamamladınız.")
elif kurs>=2:
    print("Kursun %50'sini tamamladınız.")
elif kurs>=3:
    print("Kursun %75'ini tamamladınız.")
elif kurs>=4:
    print("Kursun %100'ünü tamamladınız.")
else:
    print("Kursu tamamlamadınız")











