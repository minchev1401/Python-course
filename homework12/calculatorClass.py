# 3. Работа с модули и класове:
# Задача: Дефинирайте клас Calculator с методи за
# основни математически операции и създайте
# инстанция на този клас, за да извършите изчисления.

print("\nClass Calculator\n")

class Calculator:
    def __init__(self):
        pass
    
    def sum_numbers(self, a, b):
        return a + b
    
    def minus(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def devide(self, a, b):
        return a / b
    
calculator = Calculator()

print(calculator.sum_numbers(20, 10))
print(calculator.minus(20, 10))
print(calculator.multiply(20, 10))
print(calculator.devide(20, 10))

