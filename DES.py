from Crypto.Cipher import DES
key = "hello123"
plain = "Secrets 16 bytes"

def pad(text):
    while len(text)%8!=0:
        text+=' '
    return text  

des = DES.new(key, DES.MODE_ECB)
padded_text = pad(plain)

ciphertext = des.encrypt(padded_text)
print (ciphertext.hex())

