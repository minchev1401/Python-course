# 1. Напишете програма, която чете две цели числа, въведени от потребителя и отпечатва
# по-голямото от двете.
# ● Прочетете две цели числа от конзолата
# ● Сравнете дали първото число е по-голямо от второто. 

print("\nОтпечатване на по-голямото число\n")

a = int(input("Въведете първото число: "))
b = int(input("Въведете второто число: "))

print(f"\nЧислото {a} е по-голямо от {b}!") if a > b else print(f"Числото {b} е по-голямо от {a}!\n")

# 2. Напишете конзолна програма, която чете от
# потребителя: 
# • Възраст и пол на човек
# • Принтира обръщение, според възрастта на дадения
# човек:
# - “Mr.” – мъж (пол “m”) на 16 или повече години
# - “Master” – момче (пол “m”) под 16 години
# - “Ms.” – жена (пол 'f‘) на 16 или повече години
# - “Miss.” – момиче (пол 'f‘) под 16 години
# Направете проверка за пола, след което и проверка за
# годините.
# В тялото на проверките за възраст принтирайте желаното
# обръщение

print("Обръщение по пол и възраст!")
 
gender = input("Въведете пол ('m' за мъж, 'f' за жена): ")
age = int(input("Въведете възраст: "))

if gender == "m":
    print("Mr.") if age >= 16 else print("Master.")
elif gender == "f":
    print("Ms.") if age >= 16 else print("Miss.")
else:
    print("Невалиден пол или години!\n")
    
# 3. Напишете програма, която чете цяло число, въведено от потребителя и печата дали то е
# четно или нечетно.
# ● Ако е четно отпечатайте “even”, ако е нечетно - “odd”.
# ● подсказка -> използвайте модулно деление %

print("\nЧетно или нечетно е числото?\n")

num = int(input("Enter an number: "))

print(f"The number {num} is even!") if num % 2 == 0  else  print(f"The number {num} is odd!\n")

# 4.Напишете конзолна програма, която чете ден от седмицата (str) – въведен от потребителя и
# принтира на конзолата цената на билет за кино според деня от седмицата.

print("Price of a ticket!")

price_tickets = {
     "Monday": "12 lv",
     "Tuesday": "12 lv",
     "Wednesday": "14 lv",
     "Tursday": "14 lv",
     "Friday": "12 lv",
     "Saturday": "16 lv",
    "Sunday": "16 lv"
}

input_day = (input("Enter a day of the week: "))

if input_day in price_tickets:
    print(f"The ticket prise for {input_day.capitalize()} is {price_tickets[input_day]}.")
else:
    print("Invalid day of week!\n")
    
# 5*. Напишете програма, която чете N дни от седмицата като текст
# ● където N e число прочетено от конзолата
# ● прави проверка дали въведения текст е правилен ден от седмицата
# ● ако не е принтира подходящо съобщение и приключва изпъление
# ● ако е верен сумира колко пъти е въведен съотвения ден
# ● след като се въведат N дни, програмата принтира кой ден колко пъти е въведен и приключва.

print("Collect and count a days of the week.")

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
number_of_days = int(input("Enter the number of days: "))
day_count = [0] * 7

for _ in range(number_of_days):
    input_days = input("Enter a day of the week: ")
    input_days = input_days.capitalize()  

    if input_days in days_of_week:
       day_index = days_of_week.index(input_days)
       day_count[day_index] += 1
    else:
        print(f"Invalid day: {input_days}")

for i, day in enumerate(days_of_week):
 print(f"{day}: {day_count[i]} times")

    






    

 