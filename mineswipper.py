# Задача:
# Создайте игровое поле для "Сапёра" размером 10×10.
# Поле должно быть представлено в виде двумерного массива.
# Разместите 15 мин случайным образом (обозначьте их числом −1).
# Для каждой клетки без мины подсчитайте количество мин в соседних клетках.
# Визуализируйте:
# Само поле (где мины выделены красным).
# Поле с числами, где указано количество мин вокруг каждой клетки (для наглядности).
#
import matplotlib.pyplot as plt
import numpy as np
from random import randint


s = set()
d1 = np.zeros((10, 10))
d2 = np.zeros((10, 10))

for i in range(10):
    for j in range(10):
        d2[i][j] += ((i + j) % 2) * 0.1


while len(s) < 15:
    s.add((randint(0, 9),randint(0, 9)))

for i in s:
    d1[i] = -1
    d2[i] = 1

fig = plt.figure(figsize = (10,5))
plt.subplot(1,2,1)
plt.imshow(d2, cmap='coolwarm')


plt.subplot(1,2,2)
cnt = 0
for i in range(10):
    for j in range(10):
        if d2[i][j] != 1:
            if i > 0:
                if d1[i - 1][j] == -1:
                    cnt += 1
                if j > 0:
                    if d1[i - 1][j - 1] == -1:
                        cnt += 1
                if j < 9:
                    if d1[i - 1][j + 1] == -1:
                        cnt += 1
            if i < 9:
                if d1[i + 1][j] == -1:
                    cnt += 1
                if j > 0:
                    if d1[i + 1][j - 1] == -1:
                        cnt += 1
                if j < 9:
                    if d1[i + 1][j + 1] == -1:
                        cnt += 1
            if j > 0:
                if d1[i][j - 1] == -1:
                    cnt += 1
            if j < 9:
                if d1[i][j + 1] == -1:
                    cnt += 1
            plt.text(j, i, cnt)

            d1[i][j] = cnt
            cnt = 0
        else:
            plt.text(j, i, 'M')




plt.imshow(d1, cmap='Reds')

plt.show()