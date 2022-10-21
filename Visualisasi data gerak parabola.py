#Membuat model grafik parabola sejak titik awal hingga titik terjauh
#(sumbu Y awal dan akhir adalah 0 m ) dengan selisi waktunya sejak titik awal
# hingga akhir adalah 0,1 s. dengan kecepatan awal benda  1,4×10^−3  m/s.
#(untuk variabel lain dibebaskan). kemudian kodingan di unggah pada github

#Grafik gerak parabola
import numpy as np
import matplotlib.pyplot as plt
#Menentukan parameter gerak yang diketahui
alpha = np.radians(45)
y0 = 0.0  #ketinggian awal, m
v0 = 1.4*10**-3       #kecepatan awal benda
v0x = v0*np.cos(alpha)
y = 0.0   #ketinggian akhir, m
t = np.arange(0.0,0.01) #Selisih waktu sejak titik awal hingga akhir
x = v0x*t


fig, ax = plt.subplots()
ax.plot(x, y)
ax.set(xlabel='x (m)', ylabel= 'y (m)', title='Grafik Gerak Parabola')
ax.grid()
plt.show()
