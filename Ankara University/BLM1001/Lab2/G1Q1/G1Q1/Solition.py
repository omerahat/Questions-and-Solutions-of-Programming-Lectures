# Kullanıcıdan bir string alalım
string = input("Bir string girin: ")
# Boş bir sözlük oluşturun
counts = {}

# String içindeki her karakter için döngü oluşturalım
for char in string:
    # Eğer karakter sözlükte zaten varsa
    if char in counts:
        # Karakterin sayısını 1 arttıralım
        counts[char] += 1
    else:
        # Karakter sözlükte yoksa, karakteri sözlüğe ekleyin ve sayısını 1 olarak ayarlayalım
        counts[char] = 1

# Sözlükteki her öğe için döngü oluşturalım
for char, count in counts.items():
    # Eğer karakterin sayısı 2'den fazlaysa
    if count >= 2:
        # Karakteri ve sayısını ekrana yazdıralım
        print(char, count)

# NOT: Lablarda inputların ve printlerin içinin tamamen boş olması istenmekte. Bu örneklerin daha kolay anlaşılması için dolduruldu.