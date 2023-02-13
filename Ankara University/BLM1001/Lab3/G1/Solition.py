
import math
#math modülünü kullanmadan yapmak istersek de abs yerine öncesinde a'nın mı yoksa b'nin mi büyük olduğunu sorgulayan ifade yazmamız gerekir.

def f(x):
    return x**3 - x**2 + 2  # Değeri bulunacak fonksiyon

def Bisection(a, b, tolerans):
    c = (a + b) / 2  # Orta nokta hesaplama
    while abs(b-a) > tolerans:  # tolerans değerinden büyükken döngüyü sürdür
        c = (a + b) / 2  # Orta nokta hesaplama
        if f(c) == 0:  # Eğer f(c) = 0 ise kök bulundu
            return round(c, 4)  # Sonucu noktadan sonra 4 hane olacak şekilde yazdıralım
        elif f(a) * f(c) < 0:  # Eğer f(a)*f(c) < 0 ise kök a ve c arasındadır
            b = c  # b'yi c'ye eşitleyelim
        else:  # Aksi halde kök b ve c arasındadır
            a = c  # a'yı c'ye eşitleyelim
    return round(c, 4)  # Sonucu noktadan sonra 4 hane olacak şekilde yazdıralım

# kullanıcıdan a, b ve tolerans değerlerini alalım
a = int(input("a değerini giriniz: "))
b = int(input("b değerini giriniz: "))
tolerans = float(input("tolerans değerini giriniz: "))

print(Bisection(a, b, tolerans))

