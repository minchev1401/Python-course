# 1. Инсталиране и използване на библиотеката requests:
# Задача: Използвайте requests за изтегляне на съдържанието на уебстраница
# и отпечатване на HTML кода на конзолата.

import requests 

response = requests.get('https://itacademysz.com/')

if response.status_code == 200:
    print('Успешно получаване на данни!')
    print(response.text)
else:
    print('Възникна грешка:', response.status_code)
    




 



