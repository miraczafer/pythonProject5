import matplotlib.pyplot as plt

# İlk Grafik
# x değerlerini oluştur
x1 = list(range(1, 101))
# y değerlerini oluştur
y1 = list(range(1, 101))

# İkinci Grafik
# x değerlerini oluştur
x2 = list(range(100, 0, -1))
# y değerlerini oluştur (100 elemanlı olarak)
y2 = list(range(1, 101))

# Nokta veya daire boyutu
point_size = 10

# Boş bir şekil (figure) oluştur
plt.figure()

# İlk grafik
plt.scatter(x1, y1, s=point_size, c='red', label="Grafik 1")

# İkinci grafik
plt.scatter(x2, y2, s=point_size, c='green', label="Grafik 2")

# Grafik görünümünü ayarla
plt.xlabel("X Ekseni")
plt.ylabel("Y Ekseni")

# Grafik başlığını ayarla
plt.title("İki Grafik")

# Grafik içindeki her iki grafiği de göster
plt.legend()

# Grafiği göster
plt.show()
