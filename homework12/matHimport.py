# 2. Разликата между пълно и частично импортиране:
# Задача: Импортирайте модула math цялостно и след това само
# функцията sqrt от него. 
# Използвайте и двете за изчисляване на квадратен корен.

# 2.1

import math

a = 25
result = math.sqrt(a)

print(result)

# 2.2

from math import sqrt

a = 25
result = sqrt(a)

print(result)

