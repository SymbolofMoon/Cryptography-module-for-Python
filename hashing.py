import hashlib
md5 = hashlib.md5()
plaintext='Python'
md5.update(plaintext.encode('utf-8'))
#MD5 Hashing
print(md5.hexdigest())

sha = hashlib.sha1(plaintext.encode('utf-8')).hexdigest()

print(sha)