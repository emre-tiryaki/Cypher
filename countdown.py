import string
import random

#The encryption language letters
chars: list = list(" " + string.ascii_letters + string.digits + string.punctuation)
key: list = chars.copy()

random.shuffle(key)

print(f"chars: {chars}")
print(f"key: {key}")

#Encryption

def encrypt(plain_text: str) -> str:
    tmp: str = ""
    for i in plain_text:
        tmp += key[chars.index(i)]
    return tmp

def decrypt(encrypted_text: str) -> str:
    tmp: str = ""
    for i in encrypted_text:
        tmp += chars[key.index(i)]
    return tmp

plain_text: str = input("The text you want to encrypt: ")
encrypted_text: str = encrypt(plain_text)
print(encrypted_text)

encrypted_text = input("The text you want to decypher: ")
decripted_text: str = decrypt(encrypted_text)
print(decripted_text)