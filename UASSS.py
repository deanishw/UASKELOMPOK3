#import library yang dibutuhkan
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statistics import mean

#mengubah file excel menjadi list dan array
filename = r"C:\Users\deann\Downloads\Data Curah Hujan Kelompok 3.xls"
df = pd.read_excel(filename)

waktu1 = list(df['waktu'])
data1 = list(df['data'])

data2 = np.array(df["data"])

#membagi array menjadi 31 bagian
data3 = np.array_split(data2, 31)

data_tanggal1 = data3[0]
data_tanggal2 = data3[1]
data_tanggal3 = data3[2]
data_tanggal4 = data3[3]
data_tanggal5 = data3[4]
data_tanggal6 = data3[5]
data_tanggal7 = data3[6]
data_tanggal8 = data3[7]
data_tanggal9 = data3[8]
data_tanggal10 = data3[9]
data_tanggal11 = data3[10]
data_tanggal12 = data3[11]
data_tanggal13 = data3[12]
data_tanggal14 = data3[13]
data_tanggal15 = data3[14]
data_tanggal16 = data3[15]
data_tanggal17 = data3[16]
data_tanggal18 = data3[17]
data_tanggal19 = data3[18]
data_tanggal20 = data3[19]
data_tanggal21 = data3[20]
data_tanggal22 = data3[21]
data_tanggal23 = data3[22]
data_tanggal24 = data3[23]
data_tanggal25 = data3[24]
data_tanggal26 = data3[25]
data_tanggal27 = data3[26]
data_tanggal28 = data3[27]
data_tanggal29 = data3[28]
data_tanggal30 = data3[29]
data_tanggal31 = data3[30]


#mencari rata-rata setiap tanggalnya
def Average(data_tanggal1):
    return mean(data_tanggal1)
average1 = Average(data_tanggal1)
def Average(data_tanggal2):
    return mean(data_tanggal2)
average2 = Average(data_tanggal2)
def Average(data_tanggal3):
    return mean(data_tanggal3)
average3 = Average(data_tanggal3)
def Average(data_tanggal4):
    return mean(data_tanggal4)
average4 = Average(data_tanggal4)
def Average(data_tanggal5):
    return mean(data_tanggal5)
average5 = Average(data_tanggal5)
def Average(data_tanggal6):
    return mean(data_tanggal6)
average6 = Average(data_tanggal6)
def Average(data_tanggal7):
    return mean(data_tanggal7)
average7 = Average(data_tanggal7)
def Average(data_tanggal8):
    return mean(data_tanggal8)
average8 = Average(data_tanggal8)
def Average(data_tanggal9):
    return mean(data_tanggal9)
average9 = Average(data_tanggal9)
def Average(data_tanggal10):
    return mean(data_tanggal10)
average10 = Average(data_tanggal10)
def Average(data_tanggal11):
    return mean(data_tanggal11)
average11 = Average(data_tanggal11)
def Average(data_tanggal12):
    return mean(data_tanggal12)
average12 = Average(data_tanggal12)
def Average(data_tanggal13):
    return mean(data_tanggal13)
average13 = Average(data_tanggal13)
def Average(data_tanggal14):
    return mean(data_tanggal14)
average14 = Average(data_tanggal14)
def Average(data_tanggal15):
    return mean(data_tanggal15)
average15 = Average(data_tanggal15)
def Average(data_tanggal16):
    return mean(data_tanggal16)
average16 = Average(data_tanggal16)
def Average(data_tanggal17):
    return mean(data_tanggal17)
average17 = Average(data_tanggal17)
def Average(data_tanggal18):
    return mean(data_tanggal18)
average18 = Average(data_tanggal18)
def Average(data_tanggal19):
    return mean(data_tanggal19)
average19 = Average(data_tanggal19)
def Average(data_tanggal20):
    return mean(data_tanggal20)
average20 = Average(data_tanggal20)
def Average(data_tanggal21):
    return mean(data_tanggal21)
average21 = Average(data_tanggal21)
def Average(data_tanggal22):
    return mean(data_tanggal22)
average22 = Average(data_tanggal22)
def Average(data_tanggal23):
    return mean(data_tanggal23)
average23 = Average(data_tanggal23)
def Average(data_tanggal24):
    return mean(data_tanggal24)
average24 = Average(data_tanggal24)
def Average(data_tanggal25):
    return mean(data_tanggal25)
average25 = Average(data_tanggal25)
def Average(data_tanggal26):
    return mean(data_tanggal26)
average26 = Average(data_tanggal26)
def Average(data_tanggal27):
    return mean(data_tanggal27)
average27 = Average(data_tanggal27)
def Average(data_tanggal28):
    return mean(data_tanggal28)
average28 = Average(data_tanggal28)
def Average(data_tanggal29):
    return mean(data_tanggal29)
average29 = Average(data_tanggal29)
def Average(data_tanggal30):
    return mean(data_tanggal30)
average30 = Average(data_tanggal30)
def Average(data_tanggal31):
    return mean(data_tanggal31)
average31 = Average(data_tanggal31)

#menggabungkan list rata-rata
average1to10 = [average1,average2,average3,average4,average5,average6,average7,average8,average9,average10]
average11to20 = [average11,average12,average13,average14,average15,average16,average17,average18,average19,average20]
average21to31 = [average21,average22,average23,average24,average25,average26,average27,average28,average29,average30,average31]

average1to31 = average1to10 + average11to20 + average21to31

print("Data Curah Hujan Bulan Maret 2022")
print(average1to31)

#membuat list tanggal
tanggal_final = ["1/3/22","2/3/22","3/3/22","4/3/22","5/3/22","6/3/22","7/3/22","8/3/22","9/3/22","10/3/22","11/3/22","12/3/22","13/3/22","14/3/22","15/3/22","16/3/22","17/3/22","18/3/22","19/3/22","20/3/22","21/3/22","22/3/22","23/3/22","24/3/22","25/3/22","26/3/22","27/3/22","28/3/22","29/3/22","30/3/22","31/3/22"]

#membuat plot atau grafik
fig = plt.figure(figsize=(26,5), dpi=200)
plt.plot(tanggal_final,average1to31)

plt.xlabel("Tanggal/Bulan/Tahun")
plt.ylabel("Data")

plt.title("Grafik Curah Hujan Bulan Maret 2022")
plt.grid(True)

plt.show()
