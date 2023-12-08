# 1. Напишете програма, която проверява дали въведеното от потребителя число е в интервала
# [-100, 100] и е различно от 0 и извежда "Yes", ако отговаря на условията, или "No" ако е извън
# тях.


print("\nIs it in range from -100 to 100")

input_number = float(input("Enter a number: "))

if input_number >= -100 and input_number <= 100 and input_number != 0:
    print("YES")
else:
    print("NO")
    
    
# 2. Напишете програма, която чете въведена година от потребителя и проверява дали тя е
# високосна. Високосните години се делят на 4, без остатък. Ако годината обаче също се дели без
# остатък на 100, то тя НЕ е високосна. Ако годината също се дели без остатък и на 400, то тя ще
# е високосна.
# Ако годината е високосна, програмата извежда
# “Yes”, в противен случай извежда “No”.

print("\nВисокосна ли е годината?")

year = int(input("Въведете година: "))

if year % 400 == 0:
    print(f"YES! {year} е високосна година.")
elif year % 100 == 0:
    print(f"NO! {year} не е високосна година.")
elif year % 4 == 0:
    print(f"YES! {year} е високосна година.")
else:
    print(f"NO! {year} не е високосна година.")
    
# Напишете програма, която чете час от денонощието(цяло число) и ден от седмицата
# (текст) - въведени от потребителя и проверява дали офисът на фирма е отворен, като
# работното време на офисът е от 10-18 часа, от понеделник до събота включително.

print("\nWorking time!")

days_of_working = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

input_hour = int(input("Enter hour (format 24h): "))
input_day = str(input("Enter day of week: ")).title()

if input_day not in days_of_working:
    print("Invalid day of Week!")
elif input_day == days_of_working[-1]:
    print("CLOSED")
elif input_hour < 10 or input_hour >= 18:
    print("CLOSED")
else:
    print("OPEN")
    
    
# 4. Напишете програма, която по въведена температура от потребителя определя категорията на
# температурата: 
# “Студено” за температура под 0 градуса, 
# “Умерено” за температура между 0 и 25 градуса и
# “Топло” за температура над 25 градуса.

print("\nТоплор умерено или студено?")

input_temp = float(input("Въведете температура: "))

if input_temp < 0:
    print("Студено!")
elif input_temp <= 25:
    print("Умерено!")
else:
    print("Топло!")

# 5. Напишете програма, която чете въведена сума от потребителя и държава на доставка (текст). 
# Ако държавата е “България”
# , цената на доставката е 2% от сумата. Ако държавата е в
# “Европа”
# , цената на доставката е 5% от сумата. За останалите държави, цената на доставката
# е 10% от сумата.
# Програмата извежда крайната сума за плащане, включително доставката.

print("Total price with delivery!")

europe_country = ["France", "Germany", "Spain", "Italy", "Greece", 
 "Portugal", "Netherlands", "Belgium", "Austria", 
 "Switzerland", "Denmark", "Sweden", "Norway", "Finland"]

price = float(input("Enter price: "))
country = str(input("Enter country: ")).title()

if country == "Bulgaria":
    deliv_price = price * 0.02
    
elif country in europe_country:
    deliv_price = price * 0.05
    
else:
    deliv_price = price * 0.10
    
total_price = deliv_price + price

print(f"Total price is ${total_price}")



    
