# Kullanıcıdan bir string alalım
user_string = input("Bir string girin: ")

# Yeni bir string oluşturalım
new_string = ""

# İlk karakteri ekleyelim
new_string += user_string[0]

# Stringi dolaşalım
for i in range(1, len(user_string)):
    # Eğer önceki karakter ile şimdiki karakter farklıysa ekleyelim
    if user_string[i] != user_string[i-1]:
        new_string += user_string[i]

# Yeni stringi ekrana yazdıralım
print(new_string)

# NOT: Lablarda inputların ve printlerin içinin tamamen boş olması istenmekte. Bu örneklerin daha kolay anlaşılması için dolduruldu.