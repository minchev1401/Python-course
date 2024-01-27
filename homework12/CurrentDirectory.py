# 5. Използване на библиотеката os за взаимодействие с
# операционната система:
# Задача: Използвайте os за намиране на
# текущата работна директория и промяна на директорията.

print("\nChange Current Directory\n")

import os

current_directory = os.getcwd()
print("Current_directory is: ", current_directory)

new_directory = "C:/Users/35989/VSCode/homework/homework12"
os.chdir(new_directory)

