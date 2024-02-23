import sqlite3
import hashlib
import secrets

def hash_password(password):
    salt = secrets.token_hex(8)
    hash = hashlib.sha256(bytes(password + salt, "UTF-8")).hexdigest()
    for _ in range(1000000):
      hash = hashlib.sha256(bytes(hash, "UTF-8")).hexdigest()
    return (hash, salt)

# connect to database and create table
conn = sqlite3.connect("my_app_db.sqlite")
conn.execute(
"""
CREATE TABLE IF NOT EXISTS user(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  email TEXT NOT NULL,
  password_hash TEXT NOT NULL,
  salt TEXT NOT NULL
)
"""
)

# prompt user for their password
email = input("Type in your email: ")
password = input("Type in your password: ")

#hash the password
hash, salt = hash_password(password)

#store user in db
cursor = conn.cursor()
cursor.execute(
    "INSERT INTO user(email, password_hash, salt) VALUES (?,?,?)",
    (email, hash, salt)
)
conn.commit()

print("ACCOUNT CREATED!")

