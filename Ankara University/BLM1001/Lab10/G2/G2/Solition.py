
class Islem:
    def __init__(self, sayi1, sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2

    def ebob(self):
        sayi1, sayi2 = self.sayi1, self.sayi2
        while sayi2 != 0:
            temp = sayi2
            sayi2 = sayi1 % sayi2
            sayi1 = temp
        return sayi1
    
    def ekok(self):
        sayi1, sayi2 = self.sayi1, self.sayi2
        return sayi1 * sayi2 // self.ebob()

class FaktoriyelPozitifBolenler(Islem):
    def faktoriyel_ve_pozitif_bolenleri_hesapla(self):
        ebob = self.ebob()
        ekok = self.ekok()
        
        faktoriyel = 1
        for i in range(1, ebob + 1):
            faktoriyel *= i
        
        pozitif_bolenler = []
        for i in range(1, int(ekok**0.5) + 1):
            if ekok % i == 0:
                pozitif_bolenler.append(i)
                if i != ekok // i:
                    pozitif_bolenler.append(ekok // i)
        
        return faktoriyel, sorted(pozitif_bolenler)

# Kullanıcı tarafından verilerin alınması
sayi1 = int(input("Sayi 1: "))
sayi2 = int(input("Sayi 2: "))

# Nesne oluşturma
obj = FaktoriyelPozitifBolenler(sayi1, sayi2)

# Ebob ve Ekok değerlerinin hesaplanması
ebob = obj.ebob()
ekok = obj.ekok()

# Faktöriyel ve pozitif tam sayı bölen değerlerinin hesaplanması ve yazdırılması
faktoriyel, pozitif_bolenler = obj.faktoriyel_ve_pozitif_bolenleri_hesapla()

# Sonuçların yazdırılması
print(ebob)
print(ekok)
print(faktoriyel)
print(pozitif_bolenler)
