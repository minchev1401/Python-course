# Input koito vavejda int , proverqvate dali e bool (ako e kazva Tova e bool ili ne e bool), dadenoto chislo da se proveri 
# da ne se deli na 3 ILI na 5.

input_int = int(input("Enter a number: "))

if type(input_int) == bool:
    print(f"{input_int} is a boolean!")
else:
    print(f"{input_int} is not a boolean!")
    
if input_int % 3 != 0 or input_int % 5 != 0:
    print(f"{input_int} can't be devide on 3 or 5")
else:
    print(f"{input_int} can be devide on 3 or 5")