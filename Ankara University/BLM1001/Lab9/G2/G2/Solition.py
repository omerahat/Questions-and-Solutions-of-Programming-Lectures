import math

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __str__(self):
        return f"{self.x},{self.y},{self.z}"
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Vector(x, y, z)
    
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return Vector(x, y, z)
    
    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def distance(self, other):
        return (self - other).magnitude()

x1 = int(input("Enter the value for x: "))
y1 = int(input("Enter the value for y: "))
z1 = int(input("Enter the value for z: "))

x2 = int(input("Enter the value for x: "))
y2 = int(input("Enter the value for y: "))
z2 = int(input("Enter the value for z: "))

v1 = Vector(x1, y1, z1)
v2 = Vector(x2, y2, z2)

print(v1) # 1,2,3
print(v2) # 4,5,6
print(v1 + v2) # 5,7,9 (toplam değeri)
print(v1 - v2) # -3,-3,-3 (çıkarım değeri)
print(v1.dot(v2)) # 32 (skaler çarpım değeri)
print(round(v1.distance(v2),2)) # 5.20 (iki nokta arası uzaklık)
