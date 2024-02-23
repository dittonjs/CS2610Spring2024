import sqlite3

app_db = sqlite3.connect("my_app_db.sqlite")
rainbow_db = sqlite3.connect("rainbow_table.sqlite")

cursor = app_db.execute("SELECT * FROM user;")
users = cursor.fetchall()

for user in users:
    user_hash = user[2]
    rainbow_cursor = rainbow_db.execute("SELECT * FROM password_map WHERE hash = ?", (user_hash,))
    rainbow_hash = rainbow_cursor.fetchone()
    if rainbow_hash:
        print(f"Password for user {user[1]} is {rainbow_hash[1]}")
    else:
        print(f"No password found for user with email {user[1]}")

