from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
#from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa



private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)


public_key = private_key.public_key()

message = b"The Secret Key is here"

ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf = padding.MGF1(algorithm=hashes.SHA1()),
        algorithm=hashes.SHA1(),
        label=None
    )
)

print(ciphertext.encode('hex'))



plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf = padding.MGF1(algorithm=hashes.SHA1()),
        algorithm=hashes.SHA1(),
        label=None
    )
)

print(plaintext)