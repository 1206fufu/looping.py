import matplotlib.pyplot as plt

# parameter gerak jatuh bebas
g = 9.8 # percepataan gravitasi dalam m/s**
wakatu_total = 120 # waktu total dalam detik (2 menit)

# variabel untuk menyimpan data waktu dan posisi
waktu =[]
posisi =[]

# loop untuk menghitung posisi setiap detik 
for t in range (wakatu_total + 1):
    y = 0.5 * g * t**2 # posisi ada waktu t
    waktu.append(t)
    posisi.append(y)

 # plot gerafik posisi terhadap waktu 
plt.plot(waktu, posisi, marker='o', color='b',linestyle='-')
plt.title('gerafik gerak jatuh bebas')
plt.xlabel('waktu(detik)')
plt.ylabel('posisi(meter)')
plt.grid(True)
plt.show()
