
# Kullanıcıdan bir harf alalım.
char=input("Harfi Giriniz: ")

# Aldığımız karakterin ascii kodunu bulalım.
ascii_input=ord(char)

# Inputun ascii kodunu "a" ve "z" nin ascii koduyla karşılaştıralım.
if 97 <= ascii_input<=122:
    print(True)
else: 
    print(False)

# NOT: Lablarda inputların ve printlerin içinin tamamen boş olması istenmekte. Bu örneklerin daha kolay anlaşılması için dolduruldu.