#import library yang dibutuhkan
import pandas as pd
import matplotlib.pyplot as plt

#memasukkan tanggal yang diinginkan
T = int(input("Masukkan tanggal yang diinginkan: "))
if T < 1 or T > 31:
    print("Tanggal yang dimasukkan tidak sesuai")
else:

    #mengubah file excel menjadi dataframe
    filename = r"C:\Users\deann\Downloads\Data Curah Hujan Kelompok 3.csv"
    df = pd.read_csv(filename, sep=",", decimal=',', index_col=0)
         
    #membagi dan menghapus bagian yang tidak diperlukan pada dataframe
    df[['Tanggal-Bulan-Tahun','Waktu']]=df["waktu"].str.split(' ',expand=True)
    del df["waktu"]
    df[['Tahun','Bulan','Tanggal']]=df["Tanggal-Bulan-Tahun"].str.split('-',expand=True)
    df["Tanggal"] = df["Tanggal"].astype("int")
    del df["Tanggal-Bulan-Tahun"]
    del df["Bulan"]
    del df["Tahun"]
    df.set_index('Tanggal', inplace=True)
    
    #memakai query untuk memanggil tanggal yang diinginkan
    df3 = df.query("Tanggal == {0}".format(T))
    
    #membagi waktu menjadi jam, menit, detik dengan kolom terpisah
    df3[["Jam","Menit","Detik"]]=df3["Waktu"].str.split(":",expand=True)
    del df3["Waktu"]
    
    #menggabungkan jam yang sama pada dataframe, menjadi satu
    J1 = df3["Jam"]
    J2 = J1.values.tolist()
    Jf = list(dict.fromkeys(J2))
    
    #memilah dan merata-ratakan data sesuai dengan jam yang sama
    J3 = df3.groupby(['Jam']).mean()
    D1 = pd.DataFrame(J3)
    D2 = D1.reset_index(drop=True)
    D3 = D2.values.tolist()
    Df = [x for xs in D3 for x in xs]

    #membuat tabel dataframe untuk dijadikan plot    
    tabel = pd.DataFrame({"Jam": Jf,
                          "Data Curah Hujan": Df}) 
    tabel.index = tabel["Jam"]
    del tabel["Jam"]

    print("\n")
    print("Tabel Curah Hujan {0} Maret 2022".format(T))
    print(tabel)
    
    #membuat plot atau grafik
    fig = plt.figure(figsize=(16,5), dpi=200)
    plt.plot(Jf,Df, label="Data Curah Hujan")
    
    plt.xlabel("Jam")
    plt.ylabel("Data")
    
    plt.title("Grafik Curah Hujan {0} Maret 2022".format(T))
    plt.grid(True)
    
    plt.legend()
    plt.show()
