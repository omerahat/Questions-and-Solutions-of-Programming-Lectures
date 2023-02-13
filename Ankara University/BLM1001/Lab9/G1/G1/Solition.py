class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
        
    def __str__(self):
        return f"{self.real} + {self.imag}i"

    def add(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def subtract(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)
    
    def multiply(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)

    def equal(self, other):
        if self.real == other.real and self.imag == other.imag:
            return 1
        else:
            return 0

real1 = int(input("1. kompleks sayının reel değerini girin: "))
imag1 = int(input("1. kompleks sayının imaginer değerini girin: "))
complex1 = Complex(real1, imag1)

real2 = int(input("2. kompleks sayının reel değerini girin: "))
imag2 = int(input("2. kompleks sayının imaginer değerini girin: "))
complex2 = Complex(real2, imag2)

print("1. Kompleks sayı:", complex1)
print("2. Kompleks sayı:", complex2)
print("Toplam:", complex1.add(complex2))
print("Çıkarma:", complex1.subtract(complex2))
print("Çarpım:", complex1.multiply(complex2))
print("Eşit:", complex1.equal(complex2))
