import sqlite3


conn = sqlite3.connect('products.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
        ProductID INTEGER PRIMARY KEY,
        ProductName TEXT NOT NULL,
        Price REAL NOT NULL
    );
''')


products_data = [
    ('Apple', 2.50),
    ('Banana', 1.80),
    ('Orange', 3.20),
    ('Milk', 2.90),
    ('Bread', 1.60),
    ('Cheese', 5.75),
    ('Eggs', 2.10),
    ('Coffee', 8.50),
    ('Chocolate', 4.30),
    ('Yogurt', 1.95)
]

cursor.executemany('INSERT INTO Products (ProductName, Price) VALUES (?, ?)', products_data)

conn.commit()
conn.close()

print("Table 'Products' created successfully!")

# 1. Извличане на информация – направете таблицата с хранителни
# продукти "Products" с 10 артикула, които имат име и цена в лева. Напишете
# SQL заявка, която извлича имената и цените на всички продукти със
# стойност на цената над 50 лева.

conn = sqlite3.connect('products.db')
cursor = conn.cursor()
cursor.execute('SELECT ProductName, Price FROM Products WHERE Price > 50;')
result = cursor.fetchall()
print("\nProducts with price > 50 BGN:")
for row in result:
    print(f"{row[0]} - {row[1]} BGN")

# 2. Добавяне на нов запис - Въведете нов продукт в таблицата
# "Products" със зададено име и цена.

new_product_name = 'New Product'
new_product_price = 75
cursor.execute('INSERT INTO Products (ProductName, Price) VALUES (?, ?)', (new_product_name, new_product_price))
conn.commit()
print(f"\nNew product '{new_product_name}' added with price {new_product_price} BGN.")

# 3. Изтриване на запис: Изтрийте всички продукти от таблицата
# "Products", които са с цена под 20 лева.

cursor.execute('DELETE FROM Products WHERE Price < 20;')
conn.commit()
print("\nProducts with price < 20 BGN deleted.")

# 4. Филтриране и сортиране - извлечете имената и цените на
# продуктите от таблицата "Products", подредени в намаляващ ред
# по цената и филтрирани, така че да бъдат включени само тези
# с цена над 100 лева.

cursor.execute('SELECT ProductName, Price FROM Products WHERE Price > 100 ORDER BY Price DESC;')
result = cursor.fetchall()
print("\nProducts with price > 100 BGN (sorted by price descending):")
for row in result:
    print(f"{row[0]} - {row[1]} BGN")


conn.close()