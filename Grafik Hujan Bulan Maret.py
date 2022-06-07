#import library yang dibutuhkan
import pandas as pd
import matplotlib.pyplot as plt

#mengubah file excel menjadi dataframe
filename = r"C:\Users\deann\Downloads\Data Curah Hujan Kelompok 3.csv"
df = pd.read_csv(filename, sep=",", decimal=',', index_col=0)

#membagi dan menghapus bagian yang tidak diperlukan pada dataframe
df[['Tanggal-Bulan-Tahun','Waktu']]=df["waktu"].str.split(' ',expand=True)
del df["waktu"]
df[['Tahun','Bulan','Tanggal']]=df["Tanggal-Bulan-Tahun"].str.split('-',expand=True)

#menggabungkan tanggal yang sama pada dataframe, menjadi satu
T1 = df['Tanggal']
T2 = T1.values.tolist()
Tf = list(dict.fromkeys(T2))

#memilah dan merata-ratakan data sesuai dengan tanggal yang sama
T3 = df.groupby(['Tanggal-Bulan-Tahun']).mean()
D1 = pd.DataFrame(T3)
D2 = D1.reset_index(drop=True)
D3 = D2.values.tolist()
Df = [x for xs in D3 for x in xs]

#membuat tabel dataframe untuk dijadikan plot  
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
