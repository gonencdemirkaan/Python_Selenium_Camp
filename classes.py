class Banka:
    
    def krediBasvurusu(self):
        print("Başvuru Yapıldı")

    def krediHesapla(self):
        print("Hesaplandı")

banka = Banka()
banka.krediBasvurusu()

# self = this

class Matematik:
    def __init__(self,sayi1,sayi2): # constructor - yapıcı
        self.sayi1 = sayi1
        self.sayi2 = sayi2
        print("Matematik başladı")
    def topla(self):
        return self.sayi1 + self.sayi2
    def cikar(self):
        return self.sayi1 - self.sayi2
    def carp(self):
        return self.sayi1 * self.sayi2
    def bol(self):
        return self.sayi1 / self.sayi2

matematik = Matematik(9,7)
sonuc = matematik.topla()
print(str(sonuc))
sonuc = matematik.cikar()
print(str(sonuc))
sonuc = matematik.carp()
print(str(sonuc))
sonuc = matematik.bol()
print(str(sonuc))


class Person:
    def __init__(self,name,lastName):
        self.name = name
        self.lastName = lastName
    
musteri1 = Person("Gönenç","Demirkaan")
musteri2 = Person("Berna","Arda")
musteri3 = Person("Poyraz","Demirkaan")

print(musteri1.name)