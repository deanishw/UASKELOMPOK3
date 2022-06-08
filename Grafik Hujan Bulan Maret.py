# -*- coding: utf-8 -*-
"""
Created on Tue Jun 3 15:04:51 2022

@author: Amalia, Deanis, Keisha, Marissa, Yuannisa
"""

#Program Membuat Grafik Curah Hujan Bulan Maret

'''KEISHA'''

#import library yang dibutuhkan
import pandas as pd
import matplotlib.pyplot as plt

#mengubah file excel menjadi dataframe
filename = r"C:\Users\deann\Documents\Presentasi Komputasi\Data Curah Hujan Kelompok 3.csv"
df = pd.read_csv(filename, sep=",", decimal=',', index_col=0)
print(df)

#membagi dan menghapus bagian yang tidak diperlukan pada dataframe
df[['Tanggal-Bulan-Tahun','Waktu']]=df["waktu"].str.split(' ',expand=True)
del df["waktu"]
df[['Tahun','Bulan','Tanggal']]=df["Tanggal-Bulan-Tahun"].str.split('-',expand=True)
print(df)

del df["Waktu"]
del df["Tahun"]
del df["Bulan"]
del df["Tanggal-Bulan-Tahun"]
print(df)

#menggabungkan tanggal yang sama pada dataframe, menjadi satu
T1 = df['Tanggal']
T2 = T1.values.tolist()
Tf = list(dict.fromkeys(T2))
print("List Tanggal")
print(Tf)

'''MARISSA'''

#memilah dan merata-ratakan data sesuai dengan tanggal yang sama
T3 = df.groupby(['Tanggal']).mean()
D1 = pd.DataFrame(T3)
D2 = D1.reset_index(drop=True)
D3 = D2.values.tolist()
Df = [x for xs in D3 for x in xs]
print("\n")
print("List Curah Hujan Perhari")
print(Df)

#membuat tabel dataframe untuk dijadikan plot  
tabel = pd.DataFrame({"Tanggal": Tf,
                      "Data Curah Hujan": Df}) 
tabel.index = tabel["Tanggal"]
del tabel["Tanggal"]
print("\n")
print("Tabel Curah Hujan Bulan Maret 2022")
print(tabel)

#membuat plot atau grafik
fig = plt.figure(figsize=(15,4), dpi=200)
plt.plot(Tf,Df, label="Data Curah Hujan")

plt.xlabel("Tanggal", size=12)
plt.ylabel("Data", size=12)

plt.title("Grafik Curah Hujan Bulan Maret 2022", size=16)
plt.grid(True)

plt.legend()
plt.show()
