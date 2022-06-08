# -*- coding: utf-8 -*-
"""
Created on Tue Jun 3 16:15:52 2022

@author: Amalia, Deanis, Keisha, Marissa, Yuannisa
"""

'''AMAL'''

#Program Membuat Grafik Curah Hujan Setiap Hari Saat Bulan Maret

#import library yang dibutuhkan
import pandas as pd
import matplotlib.pyplot as plt

#memasukkan tanggal yang diinginkan
T = int(input("Masukkan tanggal yang diinginkan: "))
if T < 1 or T > 31:
    print("Tanggal yang dimasukkan tidak sesuai")
else:

    #mengubah file excel menjadi dataframe
    filename = r"C:\Users\deann\Documents\Presentasi Komputasi\Data Curah Hujan Kelompok 3.csv"
    df = pd.read_csv(filename, sep=",", decimal=',', index_col=0)
 
    '''DENIS'''
        
    #membagi dan menghapus bagian yang tidak diperlukan pada dataframe
    df[['Tanggal-Bulan-Tahun','Waktu']]=df["waktu"].str.split(' ',expand=True)
    del df["waktu"]
    df[['Tahun','Bulan','Tanggal']]=df["Tanggal-Bulan-Tahun"].str.split('-',expand=True)
    df["Tanggal"] = df["Tanggal"].astype("int")
    del df["Tanggal-Bulan-Tahun"]
    del df["Bulan"]
    del df["Tahun"]
    df.set_index('Tanggal', inplace=True)
    print(df)
    
    #memakai query untuk memanggil tanggal yang diinginkan
    df2 = df.query("Tanggal == {0}".format(T))
    print("\n")
    print("Dataframe dengan tanggal yang sudah diinginkan")
    print(df2)
    
    #membagi waktu menjadi jam, menit, detik dengan kolom terpisah
    df2[["Jam","Menit","Detik"]]=df2["Waktu"].str.split(":",expand=True)
    del df2["Waktu"]
    print("\n")
    print("Dataframe dengan jam, menit, detik sudah terpisah")
    print(df2)
    
    #menggabungkan jam yang sama pada dataframe, menjadi satu
    J1 = df2["Jam"]
    J2 = J1.values.tolist()
    Jf = list(dict.fromkeys(J2))
    print("List Jam")
    print(Jf)
    
    '''YUAN'''
    
    #memilah dan merata-ratakan data sesuai dengan jam yang sama
    J3 = df2.groupby(['Jam']).mean()
    D1 = pd.DataFrame(J3)
    D2 = D1.reset_index(drop=True)
    D3 = D2.values.tolist()
    Df = [x for xs in D3 for x in xs]
    print("\n")
    print("List Curah Hujan Perjam")
    print(Df)

    #membuat tabel dataframe untuk dijadikan plot    
    tabel = pd.DataFrame({"Jam": Jf,
                          "Data Curah Hujan": Df}) 
    tabel.index = tabel["Jam"]
    del tabel["Jam"]
    print("\n")
    print("Tabel Curah Hujan {0} Maret 2022".format(T))
    print(tabel)
    
    #membuat plot atau grafik
    fig = plt.figure(figsize=(14,4), dpi=200)
    plt.plot(Jf,Df, label="Data Curah Hujan")
    
    plt.xlabel("Jam",size=12)
    plt.ylabel("Data",size=12)
    
    plt.title("Grafik Curah Hujan {0} Maret 2022".format(T),size=16)
    plt.grid(True)
    
    plt.legend()
    plt.show()

    #tanggal 27 Maret 2022, data curah hujan hanya sampai 09:08:36
