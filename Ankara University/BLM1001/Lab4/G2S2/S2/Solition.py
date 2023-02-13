
def only_both(str1, str2):
    only1 = ""
    only2 = ""
    both = ""
    for i in str1:
        if i in str2 and i not in both:
            both = both+i
        elif i not in str2 and i not in only1:
            only1 = only1+i
    for i in str2:
        if i in str1 and i not in both:
            both = both+i
        elif i not in str1 and i not in only1:
            only2 = only2+i
    # sadece str1'de bulunanlar, sadece str2'de bulunanlar ve her ikisinde de bulunanlar döndürür
    return only1, only2, both


# Kullanıcıdan stringlerin alınması
str1 = input()
str2 = input()
x = only_both(str1, str2)

for i in x:
    print(i, end=" ")
