import pandas as pd
from PIL import Image, ImageDraw

notlar = pd.read_csv("cords.csv")

# Verileri (x, y) koordinatları olarak al
x = notlar.iloc[:, 1].tolist()
y = notlar.iloc[:, 2].tolist()

# Nokta veya daire boyutu
point_size = 10

# Resmi aç
image = Image.open("resim.png")

# Bir ImageDraw nesnesi oluştur
draw = ImageDraw.Draw(image)

# Her bir (x, y) koordinatı işle ve resim üzerine noktaları çiz
for i in range(len(x)):
    point = (int(x[i]), int(y[i]))  # (x, y) koordinatı
    draw.rectangle([point[0], point[1], point[0] + point_size, point[1] + point_size], fill="red")

# Resmi kaydet veya görüntüle
image.save("output_image.png")
image.show()
