import pandas as pd
import matplotlib.pyplot as plt

notlar = pd.read_csv("cords.csv")

# Verileri (x, y) koordinatları olarak al
x = notlar.iloc[:, 1].tolist()
y = notlar.iloc[:, 2].tolist()

# Nokta veya daire boyutu
point_size = 10

# Boş bir şekil (figure) oluştur
plt.figure()

# Her bir (x, y) koordinatı döngü içinde işle ve bir daire/nokta çiz
for i in range(len(x)):
    plt.scatter(x[i], y[i], s=point_size, c='red')

# Grafik görünümünü ayarla
plt.xlabel("X Ekseni")
plt.ylabel("Y Ekseni")

# Grafiği göster
plt.show()
