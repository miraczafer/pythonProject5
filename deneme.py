import pandas as pd

notlar = pd.read_csv("cords.csv")

# A1 sütunu ilk sütunsa, direkt olarak notlar'ı kullanabilirsiniz
veriler = notlar.iloc[:, 0].tolist()

# Verileri üçe ayır
ids = veriler[::3]  # Her üçüncü veri ID
x_eks = veriler[1::3]  # Her üçüncü veri X ekseni
y_eks = veriler[2::3]  # Her üçüncü veri Y ekseni

# Verileri ekrana yazdır
for i in range(len(ids)):
    print(f"ID: {ids[i]}, X Ekseni: {x_eks[i]}, Y Ekseni: {y_eks[i]}")
