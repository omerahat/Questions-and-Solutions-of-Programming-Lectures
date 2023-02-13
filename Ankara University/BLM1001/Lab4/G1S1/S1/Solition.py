
def labirent(size_of_map):

    # Yılanın başlangıç boyu 1 birimdir
    snake_size = 1
    food = 0

    # Yılan yediği yiyecek miktarı labirent boyutunun kare kadar büyük olana kadar devam eder
    while snake_size <= size_of_map**2:
        food += 1
        snake_size *= 2
    return food-1

# Kullanıcıdan haritanın 1 kenarının uzunluğunun alınması
size_of_map = int(input())

print(labirent(size_of_map))
