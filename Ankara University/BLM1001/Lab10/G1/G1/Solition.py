pi=3

class Kure:
    def __init__(self, yaricap):
        self.yaricap = yaricap

    def alan_hacim_hesapla(self):
        alan = 4 * pi * self.yaricap**2
        hacim = (4/3) * pi * self.yaricap**3
        print("%.2f" % alan)
        print("%.2f" % hacim)

class KureDilimi(Kure):
    def __init__(self, yaricap, aci):
        Kure.__init__(self, yaricap)
        self.aci = aci

    def kure_dilimi_alan_hacim_hesapla(self):
        alan = 4 * pi * self.yaricap**2 * (self.aci / 360)
        hacim = (4/3) * pi * self.yaricap**3 * (self.aci / 360)
        print("%.2f" % alan)
        print("%.2f" % hacim)

if __name__ == "__main__":
    yaricap = int(input().strip())
    aci = int(input().strip())
    kure = Kure(yaricap)
    kure_dilimi = KureDilimi(yaricap, aci)
    kure.alan_hacim_hesapla()
    kure_dilimi.kure_dilimi_alan_hacim_hesapla()

# Kure ve KureDilimi adında iki sınıf tanımlanıyor.
# Kure sınıfı üst sınıf, KureDilimi sınıfı alt sınıftır (kalıtım)

class Kure:
    # Kure sınıfının yaricap adında bir niteliği var.
    def __init__(self, yaricap):
        self.yaricap = yaricap

    # Kure sınıfının alan_hacim_hesapla adında bir fonksiyonu var.
    # Bu fonksiyon sırasıyla alan ve hacimi ekrana yazdırır.
    def alan_hacim_hesapla(self):
        alan = 4 * pi * self.yaricap**2
       
