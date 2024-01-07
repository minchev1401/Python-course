# 1. Напишете функция, която получава три числа (int) и връща (return) най-малкото.
# • Принтирайте резултата на конзолата.
# • Използвайте подходящо име за функцията.

def get_lower_number(a, b, c):
    return min(a, b, c)
    

print("\nThe lower integer.\n")
while True:
    try:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        c = int(input("Enter the third number: "))
        result = get_lower_number(a, b, c)
        break
    
    except (ValueError):
        print("Numbers must be integer!Try again")
    
print(f"\nThe lower integer is {result}!")


# 2. Напишите програма, която ще получава три цели числа от тип int.
# Направете следните функции:
# • sum_numbers(), която ще връща return сборът на първите две цели числа.
# • substract(), която ще връща разликата от върнатата стойност на първите две цели
# числа и третото число.

# Обединете двете функции в една главна с име add_and_subtract(), която ще
# получава трите цели числа като параметри.
# Принтирайте резултата на функцията subtract() на конзолата.

def sum_numbers(a, b):
    return a + b
def substract(a, b, c):
    return sum_numbers(a, b) - c
def add_and_subtract(a, b, c):
    return substract(a, b, c)
    
    
print("\nAdd and subtract!\n")
    
while True:
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter first number: "))
        c = int(input("Enter first number: \n"))
        result = add_and_subtract(a, b, c)
        break
    except (ValueError):
        print("The numbers must be integers!\n")
        
print(result)

# 3. Напишите програма, която получава последователност от цели числа, разделени
# от празно място (single space).
# • Принтирайте лист само от четните числа (even numbers).
# • Използвайте filter()


print("\nEven numbers\n")

def even_numbers(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))

while True:
    try:
        user_input = input("Enter The Numbers: ").split()
        numbers = [int(x) for x in user_input]
        even_numbers_list = even_numbers(numbers)
        break
    
    except ValueError:
        print("Numbers must be enter with space!")
        
print(even_numbers_list)

# 4. Напишите програма, която получава последователност от цели числа, разделени
# от празно място (single space).
# • Принтирайте сортиран (sorted) лист от числа във възходящ ред (ascending order).
# • Използвайте sorted()

print("List of sorted numbers.")

while True:
    try:
        numbers = input("Enter the numbers: ").split()
        numbers = [int(num) for num in numbers]
        sorted_numbers = sorted(numbers)

        print(sorted_numbers)
    except ValueError:
        print("The numbers must be integer!")


# 5. Напишите програма, която получава лист от цели числа, разделени от празно
# място (single space).
# • Принтирайте минималната и максималната стойност на дадените числа, както
# и сумата на всички цели числа от листа.

# - "The minimum number is {minimum number}“
# - "The maximum number is {maximum number}“
# - "The sum number is: {sum of all numbers}“

# • Използвайте min(), max() и sum().


print("\nMinimum, Maximum and Sum!\n")

def min_max_sum(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    total = sum(numbers)
    print(f"The minimum number is {minimum}")
    print(f"The maximum number is {maximum}")
    print(f"The sum number is: {total}")

while True:
    try:
        user_input = input("Enter the integers: ").split()
        user_input = [int(x) for x in user_input]
        min_max_sum(user_input)
        break
    except ValueError:
        print("The list must be only integers!")