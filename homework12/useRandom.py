# 6. Използване на библиотеката random
# за генериране на случайни числа:
# Задача: Използвайте random за генериране на
# 5 случайни числа между 1 и 10 и ги отпечатайте.

import random 

for i in range(5):
    
    a = random.randint(1, 10)
    print(a)