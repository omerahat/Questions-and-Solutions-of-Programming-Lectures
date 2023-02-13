# Küçük harf listesi
lower_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
              "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# Büyük harf listesi
upper_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
              "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
# Özel karakter listesi
char_list = ["#", "@", "*", "?"]


def password(password):
    # Şifrenin her bir karakterini liste halinde depolayalım
    pass_list = []
    # Şifredeki küçük harf, büyük harf ve özel karakter sayısını saklayalım
    counter = [0, 0, 0]
    # Şifreyi liste haline getirelim
    for i in range(len(password)):
        pass_list.append(password[i])
    # Şifredeki her bir karakter için kontrol yapalım
    for i in pass_list:
        # Küçük harf varsa sayacı arttıralım
        if i in lower_list:
            counter[0] += 1
        # Büyük harf varsa sayacı arttıralım
        elif i in upper_list:
            counter[1] += 1
        # Özel karakter varsa sayacı arttıralım
        elif i in char_list:
            counter[2] += 1
    # Şifrede en az bir tane küçük harf, büyük harf ve özel karakter olmalı
    if counter[0] == 0 or counter[1] == 0 or counter[2] == 0:
        return False
    else:
        return True


# Kullanıcıdan şifre girişi alalım
password_in = input("Şifrenizi girin: ")
# Şifre fonksiyonunu çalıştır ve sonucu ekrana bastıralım
print("Geçerli şifre: ", password(password_in))
