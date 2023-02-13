# Toplam puanı sıfır olarak başlatalım
total_score = 0

# 3 defa döngü
for i in range(3):
    # Kullanıcıdan 2 sayı alalım
    num1 = int(input("1. sayıyı girin: "))
    num2 = int(input("2. sayıyı girin: "))
    
    # Eğer sayılar eşitse oyuncu kaybeder
    if num1 == num2:
        print("Oyunu kaybettiniz!")
        break
    
    # Sayıları topla ve toplam puana ekleyelim
    total_score += num1 + num2

# Toplam puanı ekrana yazdıralım
print("Toplam puanınız: ", total_score)

# NOT: Lablarda inputların ve printlerin içinin tamamen boş olması istenmekte. Bu örneklerin daha kolay anlaşılması için dolduruldu.