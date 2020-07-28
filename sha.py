import hashlib

print(hashlib.algorithms_guaranteed)

print(hashlib.algorithms_available)

plaintext= "Hello World!!"
hashed_string = hashlib.sha224(plaintext.encode('utf-8'))
print(hashed_string.hexdigest())

hashed_string = hashlib.sha512(plaintext.encode('utf-8'))
print(hashed_string.hexdigest())