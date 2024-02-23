import hashlib
import sqlite3

def compare(password, db_hash, salt):
    hash = hashlib.sha256(bytes(password + salt, "UTF-8")).hexdigest()
    return db_hash == hash

# Connect to database
conn = sqlite3.connect("my_app_db.sqlite")

# prompt user for email and password
email = input("Type in your email: ")
password = input("Type in your password: ")

#find the user by their email
cursor = conn.cursor()
cursor.execute("SELECT * FROM user WHERE email=?", (email,))
user = cursor.fetchone()

#print result
if not user:
    print("User not found")
elif not compare(password, user[2], user[3]):
    print("Password does not match")
else:
    print("Logged in!")
