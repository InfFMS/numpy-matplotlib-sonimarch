# Задача:
# Создайте массив из 365 случайных чисел, представляющих дневную температуру (например, от −10 до 35).
# Найдите:
# Среднюю температуру за год.
# Количество дней с температурой выше 25.
# Самую длинную последовательность дней, когда температура была ниже 0.
# Визуализируйте:
# Линейный график температуры по дням.
# Гистограмму распределения температуры.
# Подсветку "холодных" и "жарких" дней на линейном графике.
from random import randint
import matplotlib.pyplot as plt


s = [randint(-10, 35) for i in range(365)]
print(f'Среднегодовая температура {round(sum(s) / len(s), 1)}')
print(f'Количество дней с температурой выше 25 - {sum(1 if i > 25 else 0 for i in s)}')
cnt = 0
d = []
for i in s:
    if i < 0:
        cnt += 1
    else:
        d.append(cnt)
        cnt = 0
print(f'Самая длинная последовательность дней, когда температура была ниже 0 - {max(d)}')


fig = plt.figure(figsize = (8, 8))
ax = plt.subplot(2,1,1)
x = [i for i in range(1, 366)]
plt.plot(x, s)
r = plt.Rectangle((5, 5), 10, 3, color='red')
ax.add_patch(r)


plt.subplot(2,1,2)
a = [i for i in range(-10, 36)]
b = [s.count(i) for i in a]
plt.bar(a, b)
plt.show()

