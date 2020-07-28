import hashlib

print(hashlib.algorithms_guaranteed)

print(hashlib.algorithms_available)

plaintext= "Hello World!!"
hashed_string = hashlib.shake_256(plaintext.encode('utf-8'))
print(hashed_string.block_size)
print(hashed_string.hexdigest(10))

