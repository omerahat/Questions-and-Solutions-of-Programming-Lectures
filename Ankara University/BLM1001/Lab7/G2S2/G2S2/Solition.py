
# Bu fonksiyon bir pozitif tam sayı alır ve Roma rakamına çevirir
def int_to_roman(num):
    # Roma rakamları için sözlük
    d = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL",
         10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
    # Sonuç stringi
    result = ""
    # Her anahtarı döndür ve sayının anahtardan büyük eşit olduğu süre boyunca sonuç stringine ekle
    for key in d.keys():
        while num >= key:
            result += d[key]
            num -= key
    # Sonuç stringini döndür
    return result

num=int(input("Sayıyı giriniz: "))

print("Roma harflerine dönüştürülmüş hali:",int_to_roman(num))