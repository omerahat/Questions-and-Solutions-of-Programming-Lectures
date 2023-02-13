
import ast

# Inputları alan fonksiyon
def func1():
	# Inputları saklamak için bir liste oluşturalım
    input_arr = []
	
    input1 = input("Ögrenci Bilgisi: ")
    input1 = input1.strip() # Baştaki ve sondaki boşlukları sil
    input_first = ast.literal_eval(input1) # String ifadeyi liste olarak yorumla
    input_arr.append(input_first)
    while True: # Sürekli input almak için döngü
        input2 = input("Ögrenci Bilgisi: ")
        input2 = input2.strip()
        if input2 == "END": # Eğer input "END" ise döngüden çıkalım
            break
        arr = ast.literal_eval(input2) # String ifadeyi liste olarak yorumla
        input_arr.append(arr) # İkinci inputu listeye ekle
    return input_arr

# Inputları alan fonksiyonun sonucunu değişkene ata
input_arr_result = (func1())


def func2(input_arr):
    result_list = [] # Sonuçları tutmak için bir liste oluşturalım
    for i in range(len(input_arr)):
        sayac = 0
        for j in range(1, 4):
			# Her bir j için eğer j. sütunları aynı ise sayacı 1 arttır
            if input_arr[i][j][0] == input_arr[i][j][1] and input_arr[i] not in result_list:
                sayac += 1
                if sayac == 3:
                    result_list.append(input_arr[i])

    return result_list

# İkinci fonksiyonun sonucunu değişkene atama
y = (func2(input_arr_result))

result = []
for i in range(len(y)):
    result.append(y[i][0])

print(result)
