ogrenciler = ["Belma Demirkaan","Murat Demirkaan","Türkan Arda"]

def ogrenciEkle ():
    name = input("İsim : ")
    lastName = input("Soyisim : ")
    ogrenciler.append(name+" "+lastName)
    for ogrenci in ogrenciler:
        print(ogrenci)
        
ogrenciEkle()

def ogrenciCikar ():
    name = input("İsim : ")
    lastName = input("Soyisim : ")
    ogrenciler.remove(name+" "+lastName)
    for ogrenci in ogrenciler:
        print(ogrenci)
        
ogrenciCikar()

def listele():
    for ogrenci in ogrenciler:
        print(ogrenci)

listele()

def cokluEkle():
    x = int(input("Eklenecek Kişi Sayısı : "))
    i = 0 
    while i < x:
        name = input("İsim : ")
        lastName = input("Soyisim : ")
        ogrenciler.append(name+" "+lastName)
        i += 1 
    else:
        print(ogrenciler)
        
cokluEkle()

def cokluCıkar():
    x = int(input("Çıkarılacak Kişi Sayısı : "))
    i = 0 
    while i < x:
        name = input("İsim : ")
        lastName = input("Soyisim : ")
        ogrenciler.remove(name+" "+lastName)
        i += 1 
    else:
        print(ogrenciler)
        
cokluCıkar()