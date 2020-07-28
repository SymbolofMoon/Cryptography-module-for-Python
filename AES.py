# key must be in 16,24 and 32 bytes long
# text should be in multiplication of 16 bytes

from Crypto.Cipher import AES
key = "Sixteen byte key"
plain = "Secrets 16 bytes"
Cipher = AES.new(key)
ciphertext = Cipher.encrypt(plain)
print (ciphertext.hex())

plaintext= Cipher.decrypt(ciphertext)
print(plaintext.decode('utf-8'))