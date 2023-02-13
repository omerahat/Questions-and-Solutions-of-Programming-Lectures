
# Kullanıcıdan 3 intager alalım.
sayi1 = int(input("Birinci sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))
sayi3 = int(input("Üçüncü sayıyı giriniz: "))

# Kaç tane sayısın eş olduğunu tutan değişkeni tanımlayalım.
esit_sayilar = 0

# Kullanıcıdan alınan sayıları karşılaştırıyoruz ve eşit olanları sayalım.
if sayi1 == sayi2:
  esit_sayilar += 1

if sayi1 == sayi3:
  esit_sayilar += 1

if sayi2 == sayi3:
  esit_sayilar += 1

# Eşit olan sayıların sayısını ekrana yazdıralım.
print("Girilen sayıların", esit_sayilar, "tanesi birbirine eşittir.")

# NOT: Lablarda inputların ve printlerin içinin tamamen boş olması istenmekte. Bu örneklerin daha kolay anlaşılması için dolduruldu.