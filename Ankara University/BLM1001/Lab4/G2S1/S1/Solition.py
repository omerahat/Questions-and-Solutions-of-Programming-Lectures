

def prime_factors(num):
    # Asal çarpanları tutacak listeyi oluştur
    prime_factors = []
    result_str = ""

    # 2'den başla ve num'un tam bölünen en küçük asal çarpanı bul
    while num % 2 == 0:
        if result_str == "":
            result_str += "2 "
        num /= 2
    # 3 ile num'un karekökü arasındaki sayıları tek tek tarama
    for i in range(3, int(num ** 0.5) + 1, 2):
        while num % i == 0:
            result_str += "{} ".format(i)
            num = num / i
    # num 1 değilse, kendisi de asal çarpan
    if num > 2:
        result_str += "{} ".format(int(num))
    return result_str


# Kullanıcıdan sayının alınması
number = int(input())

print(prime_factors(number))
