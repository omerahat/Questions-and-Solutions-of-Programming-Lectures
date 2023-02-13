def f(x):
  return x**4 - 4*x

def riemann_sum(a, b, n):
  delta_x = (b - a) / n
  sum = 0
  for i in range(n+1):
    sum += f(a + i * delta_x) * delta_x
  return sum

# Kullanıcıdan değerleri alın
a = int(input("a değerini girin: "))
b = int(input("b değerini girin: "))
n = int(input("n değerini girin: "))

result = riemann_sum(a, b, n)

# Sonucu 4 hane noktadan sonra yazdırın
print("Sonuç: {:.4f}".format(result))
