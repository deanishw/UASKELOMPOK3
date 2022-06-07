#import library yang dibutuhkan
import pandas as pd
import matplotlib.pyplot as plt

#mengubah file excel menjadi list dan array
filename = r"C:\Users\deann\Downloads\Data Curah Hujan Kelompok 3.csv"
df = pd.read_csv(filename, sep=",", decimal=',')

del df["Unnamed: 0"]
df[['Tanggal-Bulan-Tahun','Waktu']]=df["waktu"].str.split(' ',expand=True)
del df["waktu"]
df[['Tahun','Bulan','Tanggal']]=df["Tanggal-Bulan-Tahun"].str.split('-',expand=True)

T1 = df['Tanggal']
T2 = T1.values.tolist()
Tf = list(dict.fromkeys(T2))

T3 = df.groupby(['Tanggal-Bulan-Tahun']).mean()
D1 = pd.DataFrame(T3)
D3 = D1.reset_index(drop=True)
D4 = D3.values.tolist()
Df = [x for xs in D4 for x in xs]

tabel = pd.DataFrame({"Tanggal": Tf,
                      "Data Curah Hujan": Df}) 
tabel.index = tabel["Tanggal"]
del tabel["Tanggal"]

print("Tabel Curah Hujan Bulan Maret 2022")
print(tabel)

#membuat plot atau grafik
fig = plt.figure(figsize=(15,4), dpi=200)
plt.plot(Tf,Df, label="Data Curah Hujan")

plt.xlabel("Tanggal")
plt.ylabel("Data")

plt.title("Grafik Curah Hujan Bulan Maret 2022")
plt.grid(True)

plt.legend()
plt.show()
