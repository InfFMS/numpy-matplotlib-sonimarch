# Задача:
# Создайте шахматную доску размером 8×8, где чёрные клетки обозначены числом 1, а белые — 0.
# Укажите координаты клетки, где находится ферзь, например, [4,4].
# Определите клетки, которые атакует ферзь (в строке, столбце и диагоналях).
# Визуализация: Используйте тепловую карту (imshow), чтобы показать шахматную доску. Отметьте положение ферзя и атакуемые клетки цветами.
import matplotlib.pyplot as plt
import numpy as np


d = np.zeros((8, 8))
for i in range(8):
    for j in range(8):
        d[i][j] += (i + j) % 2

fig, ax = plt.subplots()
plt.imshow(d, cmap='Greys')

for x in range(8):
    k = (x, 4)
    ci1 = plt.Circle(k, 0.4, color='green')
    ax.add_patch(ci1)
for x in range(8):
    k = (3, x)
    ci1 = plt.Circle(k, 0.4, color='green')
    ax.add_patch(ci1)
for x in range(8):
    k = (x, x + 1)
    ci1 = plt.Circle(k, 0.4, color='green')
    ax.add_patch(ci1)
for x in range(8):
    k = (x, 7 - x)
    ci1 = plt.Circle(k, 0.4, color='green')
    ax.add_patch(ci1)

ci = plt.Circle((3, 4), 0.4, color='red')
ax.add_patch(ci)
plt.xticks(range(8), labels=[i for i in "ABCDEFGH"])
plt.yticks(range(8), labels=[i for i in range(8, 0, -1)])

plt.show()