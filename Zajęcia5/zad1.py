import sqlite3

conn = sqlite3.connect("sales.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM sales WHERE product = ?", ("Laptop",))
laptops = cursor.fetchall()
print("Sprzedaż Laptopów:")
for row in laptops:
    print(row)
print("\n")

cursor.execute("SELECT * FROM sales WHERE date IN (?, ?)", ("2025-05-07", "2025-05-08"))
dates = cursor.fetchall()
print("Dane z 2025-05-07 i 2025-05-08:")
for row in dates:
    print(row)
print("\n")

cursor.execute("SELECT * FROM sales WHERE price > ?", (200,))
expensive_sales = cursor.fetchall()
print("Transakcje z ceną jednostkową > 200 zł:")
for row in expensive_sales:
    print(row)
print("\n")

cursor.execute("""
    SELECT product, SUM(quantity * price) AS total_sales
    FROM sales
    GROUP BY product
""")
total_sales = cursor.fetchall()
print("Łączna wartość sprzedaży dla każdego produktu:")
for row in total_sales:
    print(f"{row[0]}: {row[1]:.2f} zł")
print("\n")

cursor.execute("""
    SELECT date, SUM(quantity) AS total_quantity
    FROM sales
    GROUP BY date
    ORDER BY total_quantity DESC
    LIMIT 1
""")
best_day = cursor.fetchone()
print(f"Dzień z największą liczbą sprzedanych sztuk: {best_day[0]} ({best_day[1]} sztuk)")

conn.close()
