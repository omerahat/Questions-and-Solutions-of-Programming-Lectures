# Kullanıcıdan bir tamsayı alalım
number = int(input("Bir tamsayı girin: "))
# Kontrol edilecek sayı
sum_of_digits = 0

# Sayının rakamlarının toplamını bulalım
while number > 0:
    sum_of_digits += number % 10
    number //= 10

# Sayının rakamlarının toplamı sayının böleni mi kontrol edelim
if number % sum_of_digits == 0:
    print("true")
else:
    print("false")
    
# NOT: Lablarda inputların ve printlerin içinin tamamen boş olması istenmekte. Bu örneklerin daha kolay anlaşılması için dolduruldu.