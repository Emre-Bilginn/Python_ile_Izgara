from csv import excel
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x_coordinates = np.random.randint(0,1000,1000)
y_coordinates = np.random.randint(0,1000,1000)

df = pd.DataFrame({'x':x_coordinates,'y':y_coordinates})
excel_path = 'Kordinatlar.xlsx'
df.to_excel(excel_path,index=False)

df = pd.read_excel(excel_path)

fig, ax = plt.subplots(figsize=(10,10))
grid_size = 100

colors = []

for x, y in zip(df['x'], df['y']):
    if x <100 or y < 100:
        colors.append('red')
    elif 100 <= x <200 or 100 <= y < 200:
        colors.append('blue')
    elif 200 <= x <300 or 200 <= y < 300:
        colors.append('green')
    elif 300 <= x <400 or 300 <= y < 400:
        colors.append('purple')
    elif 400 <= x <500 or 400 <= y < 500:
        colors.append('yellow')
    elif 500 <= x <600 or 500 <= y < 600:
        colors.append('pink')
    elif 600 <= x <700 or 600 <= y < 700:
        colors.append('brown')
    elif 700 <= x <800 or 700 <= y < 800:
        colors.append('orange')
    elif 800 <= x <900 or 800 <= y < 900:
        colors.append('gray')
    else :
        colors.append('black')

scatter = ax.scatter(df['x'], df['y'], c=colors, alpha=0.8, edgecolors='w', linewidth=0.5)

ax.set_xticks(np.arange(0, 1001, grid_size))
ax.set_yticks(np.arange(0, 1001, grid_size))
ax.grid(True, which='both', color='gray', linestyle='--', linewidth=0.5)

ax.set_title('Rastgele Koordinatlar ve Renkli Izgara')
ax.set_xlabel('X Koordinatları')
ax.set_ylabel('Y Koordinatları')

plt.show()