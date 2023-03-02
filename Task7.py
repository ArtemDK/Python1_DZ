# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

import random
number_1 = random.randint(0, 10000000)
print(number_1)
stepen = 2
dig1 = 0
while number_1 >= stepen:
    dig = stepen*stepen
    stepen = dig
    if dig < number_1:
        print(dig)

