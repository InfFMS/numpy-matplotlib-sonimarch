# Задача:
# Смоделируйте 1000 бросков игрального кубика.
# Найдите:
# Сколько раз выпадало каждое значение (от 1 до 6).
# Вероятность выпадения каждого значения.
# Максимальное количество подряд выпавших одинаковых значений.
# Визуализируйте результаты в виде гистограммы.

import matplotlib.pyplot as plt
from random import randint



s_cnt = []
p = 0
cnt = 0
s = []
for i in range(1000):
    s.append(randint(1, 6))
    if s[i] == p:
        cnt += 1
    else:
        s_cnt.append(cnt)
        cnt = 0
    p = s[i]


for i in range(1, 7):
    print(f'{i} выпало {s.count(i)} раз, вероятность - {s.count(i) / 10}%')

print(f'Максимальное количество пдорят выпавших одинаковых значений {max(s_cnt)}')


cat = [str(i) for i in range(1, 7)]
val = [s.count(i) for i in range(1, 7)]
plt.bar(cat, val, color='orange')
plt.show()