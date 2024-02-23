import hashlib

hasher = hashlib.md5()
hasher.update(b"Hello, world!")
print(hasher.hexdigest())