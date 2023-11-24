# 1. Пресметнете лице на правоъгълник:
# Да се напише конзолна програма, която въвежда две цели числа (страните на
# правоъгълника a и b), пресмята лицето на правоъгълник с тези страни и принтира резултата от променлива "area".

print("Пресметнете лицето на правоъгълник:")
a = int(input("въведете \"a\": "))
b = int(input("enter \"b\": "))
area = a * b

print("Лицето е: " + str(area))

# 2. Поздрав по име:
# Да се напише конзолна програма, която чете от конзолата име на човек и отпечатва
# “Hello <name>!”, където <name> е въведеното име от конзолата.
# Насоки:
# ● Създайте променлива name и запазете в нея името, което ще прочете от
# конзолата, използвайки функцията input().
# ● Изведете изхода на конзолата, чрез конкатенация (долепяне на текстовете).
# ● Принтирайте получения резултат.

print("Поздрав по име:")

name = input("Въведете име: ")

print("Hello " + name + "!")

# 3. Конкатенация на текст и числа:
# Напишете програма, която прочита от конзолата име, фамилия, възраст и град и
# печата следното съобщение:
# “You are <first_name> <last_name>, a <age> - years old person from <town>.”
# ● Въведете входните данни и ги запишете в променливи с подходящ тип данни.
# ● Изведете форматирания изход:

print("Конкатенация на текст и числа:")

first_name = str(input("Enter first name: "))
last_name = str(input("enter last name: "))
age = int(input("enter your age: "))
town = str(input("eneter your town: "))

print(f"You are {first_name} {last_name}, a {age}- years old person from {town}.")

# 4. Добавяне на 1 година към дата:
# Напишете програма, която прочита от конзолата дата, добавя 1 година към нея и
# печата новата дата.

print("Добавяне на 1 година към дата:")

from datetime import datetime

date_str = input("Enter date(format DD/MM/YYYY): ")
date_format = datetime.strptime(date_str, '%d/%m/%Y')
new_date = date_format.replace(year = date_format.year + 1)
date_to_print = new_date.strftime("%d/%m/%Y")

print(date_to_print)

# 5.Прочитане на 3 променливи от тип цяло число, записване във списък и
# сумиране. На конзолата трябва да се принтира сумата.

print("Прочитане на 3 променливи, записване в списък.\nПринтиране на сумата им.")

num1 = int(input("Enter the first num: "))
num2 = int(input("Enter the second num: "))
num3 = int(input("Enter the third num: "))

my_list = [num1, num2, num3]
sum_my_list = sum(my_list)

print(f"The sum is: {sum_my_list}")

# 6*.Прочитане на неизвестен/различен брой числa, записване във списък и
# сумиране. На конзолата трябва да се принтира сумата.

print("Прочитане на неизвестен брой числa, записване в списък и\nпринтиране на сумата им.")
numbers = []
while True:
    try:
        user_input = input("Enter a number (or \"Q\" to finish): ")
        if user_input.upper() == "Q":
            break
        numbers.append(int(user_input))
    except ValueError:
        print("Invalid input. Please enter a valid integer or 'Q'.")

total_sum = sum(numbers)
print(f"Sum of the numbers: {total_sum}")







