
import sqlite3
import random
conn = sqlite3.connect("database.sqlite")

conn.execute(
"""
CREATE TABLE IF NOT EXISTS purchase_order(
id INTEGER PRIMARY KEY AUTOINCREMENT,
amount DOUBLE NOT NULL,
product_name TEXT NOT NULL
);
"""
)

products = [
    "LARGE_BOLT",
    "SMALL_BOLT",
    "WOOD_SCREW",
    "DRYWALL_SCREW",
    "LARGE_NAIL",
    "SMALL_NAIL"
]
values = []
for _ in range(5000000):
    amount = round(random.uniform(5.5, 200.5), 2)
    product = random.choice(products)
    values.append(str((amount, product)))

values = ",".join(values)
res = conn.executescript(f"INSERT INTO 'purchase_order' ('amount', 'product_name') VALUES {values};")
