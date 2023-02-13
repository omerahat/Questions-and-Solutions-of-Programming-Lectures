import ast

def pie_chart(data_catalog, data_frequency):
    total = sum(data_frequency)
    angles = [f / total * 360 for f in data_frequency]
    return [[data_catalog[i], angles[i]] for i in range(len(data_catalog))]

# Kullanıcıdan veri katalogları ve frekanslarının listelerini alın
data_catalog = input("Veri kataloglarının listesini girin: ")
data_frequency = input("Frekansların listesini girin: ")

# Kullanıcı tarafından girilen verileri liste tipine dönüştür
data_catalog = ast.literal_eval(data_catalog)
data_frequency = ast.literal_eval(data_frequency)

# Pasta dilimi grafiğini oluşturan fonksiyonu çağır
result = pie_chart(data_catalog, data_frequency)

# Sonuçları ekrana yazdır
print("Pasta dilimi grafiği:", result)
