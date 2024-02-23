import hashlib

my_string = input("input a string: ")

hash = hashlib.sha256(my_string.encode()).hexdigest()

print(hash)
