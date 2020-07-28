import hashlib, binascii

hash = hashlib.pbkdf2_hmac('sha512', b'SupersecretPassword',b'saltthepassword',100000)
print(binascii.hexlify(hash).decode('utf-8'))