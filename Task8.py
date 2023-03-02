# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению


import random

number = int(input('введите длину списка: '))
my_list = [random.randint(0,100) for _ in range (number)]
print(my_list)
my_list.sort()
print(my_list)
finde = int(input('какое число ищем?: '))
count=0
dig = 0
for item in my_list:
    if item==finde:
        count += 1
if count>0:
    print(f' число {finde} встречается {count} раз')
else:
    for item in my_list:
    if item < finde:
        dig==finde
    print(item)

    # print(dig)

# 	else:
# print(f' число {finde} встречается {count} раз')

