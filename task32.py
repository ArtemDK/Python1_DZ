# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random

new_list = [random.randint(0, 100) for _ in range(1, 10)]
print(new_list)

min_date = 10
max_date = 45
rez = list()

for i in range(len(new_list)):
    if min_date <= new_list[i] <= max_date:
        rez.append(i)
print(rez)

