
# Kullanıcıdan 5 haneli bir sayı alalım.
sayi = int(input("Lütfen 5 haneli bir sayı girin: "))

# Sayının ilk rakamını bulalım.
ilk_rakam = sayi // 10000

# Sayıyı ilk rakamından kurtaralım
sayi = sayi % 10000

# Sayının ikinci rakamını bulalım
ikinci_rakam = sayi // 1000

# Sayıyı ikinci rakamından kurtaralım
sayi = sayi % 1000

# Sayının üçüncü rakamını bulalım
ucuncu_rakam = sayi // 100

# Sayıyı üçüncü rakamından kurtaralım
sayi = sayi % 100

# Sayının dördüncü rakamını bulalım
dorduncu_rakam = sayi // 10

# Sayının beşinci rakamını bulalım
besinci_rakam = sayi % 10

# Rakamları ekrana basalım
print(f"Sayının rakamları: {ilk_rakam}, {ikinci_rakam}, {ucuncu_rakam}, {dorduncu_rakam}, {besinci_rakam}")

# NOT: Lablarda inputların ve printlerin içinin tamamen boş olması istenmekte. Bu örneklerin daha kolay anlaşılması için dolduruldu.