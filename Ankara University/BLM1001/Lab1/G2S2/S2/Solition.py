
# Kullanıcıan bir sayı alalım.
sayi=input("Sayıyı Giriniz: ")

# Sayının rakamlar toplamını tutan değişkeni tanımlayalım.
rakamlar_toplam=0

# Sayının rakamlarını toplayan for loopunu yazalım.
for i in range(len(sayi)):
    rakamlar_toplam+=int(i)

# Rakamlar toplamıyla sayının tekliğini çiftliği kontrol edelim.
if rakamlar_toplam%2 == int(sayi)%2:
    print(True)
else:   
    print(False)

# NOT: Lablarda inputların ve printlerin içinin tamamen boş olması istenmekte. Bu örneklerin daha kolay anlaşılması için dolduruldu.