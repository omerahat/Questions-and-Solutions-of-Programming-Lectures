def input_grades():
    # Öğrenci notlarını alıp students.txt dosyasına kaydetme
    with open("students", "w") as f:
        while True:
            student_input = input().strip() # Öğrenci adı ve notu input alınır
            if student_input == "X": # Eğer X girdisi aldıysak döngüden çık
                break
            student_name, grade = student_input.split() # Ad ve notu ayır
            f.write(f"{student_name}\t{grade}\n") # Dosyaya yaz

def calculate_average():
    # students.txt dosyasındaki notların ortalamasını hesaplama
    total = 0
    count = 0
    with open("students", "r") as f:
        for line in f:
            _, grade = line.strip().split() # Her satırdaki ad ve notu ayır
            total += int(grade) # Notları topla
            count += 1
    return round(total / count, 2) # Ortalamayı hesapla ve 2 ondalık basamağına yuvarlanır

def find_max():
    # students.txt dosyasındaki en yüksek notu ve o notu aldığı öğrenciyi bulma
    max_student = ""
    max_grade = -1
    with open("students", "r") as f:
        for line in f:
            student, grade = line.strip().split() # Her satırdaki ad ve notu ayır
            if int(grade) > max_grade: # Eğer bu satırdaki not en yüksek not ise
                max_grade = int(grade) # Not değeri güncellenir
                max_student = student # Öğrenci adı güncellenir
    return max_student, max_grade

input_grades() # Öğrenci notlarını alma
average = calculate_average() # Ortalama notu hesaplama
max_student, max_grade = find_max() # En yüksek notu ve o notu aldığı öğrenciyi bulma
print(average) # Ortalama notu ekrana yaz
print(f"{max_student}\t{max_grade}") # En yüksek notu aldığı öğrenci ve notu ekrana yaz