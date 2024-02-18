# 1. Фибоначи: Създайте рекурсивна функция, която изчислява n-
#тия елемент от редицата на Фибоначи.

print("\n'Fibonaci'\n")

def fibonaci(n):
    if n < 0:
        print("Неправилно въвеждане")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonaci(n - 1) + fibonaci(n - 2)
    

n = 10    
result = fibonaci(n)
print (f"Fibonaci from '{n}' is '{result}'")
    
    
# 2.Сума на Числа: Създайте рекурсивна функция, която намира
# сумата на всички цели числа от 1 до n.

print("\n'Sum of numbers'\n")

def sum_numbers(n):
    if n == 0:
        return 0
    else:
        return n + sum_numbers(n - 1)

n = 5
result = sum_numbers(n)
print(f"Сумата на числата от 1 до {n} е {result}")

# 3. Обръщане на Низ: Напишете рекурсивна функция, която
# обръща даден низ без да използва вградени функции.

print("\n'Revers a string'\n")

def reverse_string(x):
    if len(x) <= 1:
        return x
    else:
        return reverse_string(x[1:]) + x[0]


string = "Mincho Minchev"
reversed_string = reverse_string(string)

print(f"Reversed  '{string}' is '{reversed_string}'")

# 4. Палиндром: Напишете рекурсивна функция, която проверява
# дали даден низ е палиндром (четене отпред назад и отзад
# напред дава еднакви резултати).

print("\n'Is it palindrom or not'\n")

def is_palindrom(x):
    
    if len(x) <= 1:
        return True
    else:
        return x[0] == x[-1] and is_palindrom(x[1:-1])


string = "cannac"

if is_palindrom(string):
    print(f"'{string}' е палиндром.")
else:
    print(f"'{string}' не е палиндром.")
