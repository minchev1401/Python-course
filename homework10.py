# 1. Създайте клас с име Person.
# При инициализацията, той трябва да получи name и age.
# Скрийте името и възрастта като private атрибути, които не са достъпни извън класа.
# Създайте два метода на инстанцията наречени get_name и get_age, които да връщат
# стойностите на private атрибутите.

print("\nClass 'Person'\n")

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
person = Person("George", 32)
print(person.get_name())
print(person.get_age())


# 2. Създайте клас с име Mammal. 
# При инициализацията, той трябва да получи name, type и sound. 
# Създайте клас атрибут наречен kingdom, който не бива да се достъпва извън класа и
# го задайте на “animals”.
# Направете още три метода на инстанцията:
# • make_sound – връща низ във формата "{name} makes {sound}“
# • get_kingdom – връща private атрибут на царство (kingdom)
# • info() – връща низ във формата "{name} is of type {type}"

print("\nClass 'Mammal'!\n")


class Mammal:
    def __init__(self, name, type, sound):
        self.name = name
        self.type = type
        self.sound = sound
        self.__kingdom = "animals"
        
    def make_sound(self):
        return f"{self.name} makes {self.sound}"

    def get_kingdom(self):
        return self.__kingdom

    def info(self):
        return f"{self.name} is of type {self.type}"

mammal = Mammal("Dog", "Domestic", "Bark")

print(mammal.make_sound())
print(mammal.get_kingdom())
print(mammal.info())

# 3. Създайте папка project, в която направете два файла със следните имена:
# • food.py
# • fruit.py
# Във файла food.py, създайте клас наречен Food, който при инициализация ще
# получава дата на изтичане на срока (expiration_date) като низ от символи (str).
# Във файла fruit.py, създайте клас наречен Fruit, който при инициализация ще
# получава име (name) като низ от символи (str) и дата на изтичане на срока
# (expiration_date) също като низ (str). 
# Класът Fruit трябва да наследява класа Food.

print("\nProject food/fruit\n")

import os

if not os.path.exists("project"):
    os.mkdir("project")
    
with open("project/food.py", "w") as f:
    f.write("""class Food:
    def __init__(self, expiration_date):
        self.expiration_date = expiration_date""")
    
with open("project/fruit.py", "w") as f:
    f.write("""
from food import Food

class Fruit(Food):
    def __init__(self, name, expiration_date):
        super().__init__(expiration_date)
        self.name = name
""")
    
# 4. В папка наречена (project) създайте два файла със следните имена: 
# • animal.py 
# • dog.py
# Във файла animal.py, създайте клас наречен (Animal) с единствен метод eat(), който
# връща: “eating…”
# Във файла dog.py, създайте клас наречен (Dog) с единствен метод bark(), който
# връща: "barking…"
# Класът (Dog) трябва да наследява от класа (Animal).

print("\nProject animal/dog\n")

import os

if not os.path.exists("project"):
    os.mkdir("project")
    
with open("project/animal.py", "w") as f:
    f.write("""class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return 'eating...'""")
    
with open("project/dog.py", "w") as f:
    f.write("""
from animal import Animal

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def bark(self):
        return 'barking...'
""")
    
# 5. Създайте клас наречен (Vehicle). 
# При инициализация, той трябва да получава max_speed (int - по избор; по
# подразбиране 150) и mileage (number). 
# Създайте променлива на инстанцията наречена (gadgets) - празен списък по
# подразбиране.

print ("\nClass 'Vehicle'\n")

class Vehicle:
    def __init__(self, max_speed = 150, mileage = 0):
        self.max_speed = max_speed
        self.mileage = mileage
        self.gadgets = []
        
car = Vehicle(mileage = 20)

print(car.max_speed)
print(car.mileage)
print(car.gadgets)

car.gadgets.append("Hudly Wireless")

print(car.gadgets)

# 6. Създайте клас наречен (Circle). 
# При инициализация, той трябва да получава radius (number). Създайте клас атрибут
# наречен пи (pi), който трябва да бъде равен на 3.14. Създайте 3 метода на
# инстанцията:
# • set_radius (new_radius) – променя радиуса
# • get_area() – връща прощта на кръга
# • get_circumference() – връща обиколката на кръга

print("\nClass 'Circle'\n")

class Circle:
    def __init__(self, radius = 0):
        self.radius = radius
        self.pi = 3.14
        
    def set_radius(self, new_radius):
        self.radius = new_radius
        
    def get_area(self):
        return self.pi * self.radius ** 2
    
    def get_circumference(self):
        return 2 * self.pi * self.radius
    
circle = Circle(10)
circle.set_radius(12)

print(circle.get_area())
print(circle.get_circumference())

