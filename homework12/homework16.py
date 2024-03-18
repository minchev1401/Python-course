import sqlite3


conn = sqlite3.connect('cars.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Cars (
        CarID INTEGER PRIMARY KEY,
        Brand TEXT NOT NULL,
        Price REAL NOT NULL
    );
''')

cars_data = [
    ('Toyota', 60000),
    ('BMW', 80000),
    ('Mercedes', 75000),
    ('Ford', 35000),
    ('Audi', 90000),
    ('Volkswagen', 45000),
    ('Honda', 55000),
    ('Lexus', 95000),
    ('Tesla', 120000),
    ('Porsche', 150000)
]

cursor.executemany('INSERT INTO Cars (Brand, Price) VALUES (?, ?)', cars_data)

conn.commit()
conn.close()

print("Таблицата 'Cars' е създадена успешно!")

# 1: Извличане на марките и цените на автомобилите с цена над 50 000 лева
conn = sqlite3.connect('cars.db')
cursor = conn.cursor()
cursor.execute('SELECT Brand, Price FROM Cars WHERE Price > 50000;')
result = cursor.fetchall()
print("\nАвтомобили с цена над 50 000 лева:")
for row in result:
    print(f"{row[0]} - {row[1]} лева")

# 2. Изтриване на автомобили с цена под 30 000 лева
cursor.execute('DELETE FROM Cars WHERE Price < 30000;')
conn.commit()
print("\nАвтомобили с цена под 30 000 лева са изтрити.")

# 3. Вмъкване на нов автомобил
new_car_brand = 'Nissan'
new_car_price = 70000
cursor.execute('INSERT INTO Cars (Brand, Price) VALUES (?, ?)', (new_car_brand, new_car_price))
conn.commit()
print(f"\nДобавен е нов автомобил '{new_car_brand}' с цена {new_car_price} лева.")

# 4. Извличане на марките и цените на автомобилите с цена над 100 000 лева (подредени по цена намаляващо)
cursor.execute('SELECT Brand, Price FROM Cars WHERE Price > 100000 ORDER BY Price DESC;')
result = cursor.fetchall()
print("\nАвтомобили с цена над 100 000 лева (подредени по цена намаляващо):")
for row in result:
    print(f"{row[0]} - {row[1]} лева")


conn.close()