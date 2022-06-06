#import library yang dibutuhkan
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statistics import mean

#memasukkan tanggal yang diinginkan
T = int(input("Masukkan tanggal yang diinginkan: "))
if T < 1 or T > 31:
    print("Tanggal yang dimasukkan tidak sesuai")
else:
    T_final = T - 1

    #mengubah file excel menjadi list dan array
    filename = r"C:\Users\deann\Downloads\Data Curah Hujan Kelompok 3.xls"
    df = pd.read_excel(filename)
    
    waktu1 = list(df['waktu'])
    data1 = list(df['data'])
    
    data2 = np.array(df["data"])
    
    #membagi array menjadi 31 bagian
    data3 = np.array_split(data2, 31)
    
    #membagi array menjadi 24 bagian
    data4 = data3[T_final]
    data5 = np.array_split(data4, 24)
    
    data_waktu1 = data5[0]
    data_waktu2 = data5[1]
    data_waktu3 = data5[2]
    data_waktu4 = data5[3]
    data_waktu5 = data5[4]
    data_waktu6 = data5[5]
    data_waktu7 = data5[6]
    data_waktu8 = data5[7]
    data_waktu9 = data5[8]
    data_waktu10 = data5[9]
    data_waktu11 = data5[10]
    data_waktu12 = data5[11]
    data_waktu13 = data3[12]
    data_waktu14 = data3[13]
    data_waktu15 = data3[14]
    data_waktu16 = data3[15]
    data_waktu17 = data3[16]
    data_waktu18 = data3[17]
    data_waktu19 = data3[18]
    data_waktu20 = data3[19]
    data_waktu21 = data3[20]
    data_waktu22 = data3[21]
    data_waktu23 = data3[22]
    data_waktu24 = data3[23]
    
    #mencari rata-rata setiap jam-nya
    def Average(data_waktu1):
        return mean(data_waktu1)
    average1 = Average(data_waktu1)
    def Average(data_waktu2):
        return mean(data_waktu2)
    average2 = Average(data_waktu2)
    def Average(data_waktu3):
        return mean(data_waktu3)
    average3 = Average(data_waktu3)
    def Average(data_waktu4):
        return mean(data_waktu4)
    average4 = Average(data_waktu4)
    def Average(data_waktu5):
        return mean(data_waktu5)
    average5 = Average(data_waktu5)
    def Average(data_waktu6):
        return mean(data_waktu6)
    average6 = Average(data_waktu6)
    def Average(data_waktu7):
        return mean(data_waktu7)
    average7 = Average(data_waktu7)
    def Average(data_waktu8):
        return mean(data_waktu8)
    average8 = Average(data_waktu8)
    def Average(data_waktu9):
        return mean(data_waktu9)
    average9 = Average(data_waktu9)
    def Average(data_waktu10):
        return mean(data_waktu10)
    average10 = Average(data_waktu10)
    def Average(data_waktu11):
        return mean(data_waktu11)
    average11 = Average(data_waktu11)
    def Average(data_waktu12):
        return mean(data_waktu12)
    average12 = Average(data_waktu12)
    def Average(data_waktu13):
        return mean(data_waktu13)
    average13 = Average(data_waktu13)
    def Average(data_waktu14):
        return mean(data_waktu14)
    average14 = Average(data_waktu14)
    def Average(data_waktu15):
        return mean(data_waktu15)
    average15 = Average(data_waktu15)
    def Average(data_waktu16):
        return mean(data_waktu16)
    average16 = Average(data_waktu16)
    def Average(data_waktu17):
        return mean(data_waktu17)
    average17 = Average(data_waktu17)
    def Average(data_waktu18):
        return mean(data_waktu18)
    average18 = Average(data_waktu18)
    def Average(data_waktu19):
        return mean(data_waktu19)
    average19 = Average(data_waktu19)
    def Average(data_waktu20):
        return mean(data_waktu20)
    average20 = Average(data_waktu20)
    def Average(data_waktu21):
        return mean(data_waktu21)
    average21 = Average(data_waktu21)
    def Average(data_waktu22):
        return mean(data_waktu22)
    average22 = Average(data_waktu22)
    def Average(data_waktu23):
        return mean(data_waktu23)
    average23 = Average(data_waktu23)
    def Average(data_waktu24):
        return mean(data_waktu24)
    average24 = Average(data_waktu24)
    
    #menggabungkan list rata-rata
    average1to12 = [average1,average2,average3,average4,average5,average6,average7,average8,average9,average10,average11,average12]
    average13to24 = [average13,average14,average15,average16,average17,average18,average19,average20,average21,average22,average23,average24]
    
    average1to24 = average1to12 + average13to24
    
    print("Data Curah Hujan {0} Maret 2022".format(T))
    print(average1to24)
    
    #membuat list waktu
    waktu_final = ["00:00","01:00","02:00","03:00","04:00","05:00","06:00","07:00","08:00","09:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00","20:00","21:00","22:00","23:00"]
    
    #membuat plot atau grafik
    fig = plt.figure(figsize=(16,5), dpi=200)
    plt.plot(waktu_final,average1to24)
    
    plt.xlabel("Waktu")
    plt.ylabel("Data")
    
    plt.title("Grafik Curah Hujan {0} Maret 2022".format(T))
    plt.grid(True)
    
    plt.show()
