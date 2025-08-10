import random
import string

chars = " " + string.ascii_letters + string.digits + string.punctuation
chars = list(chars)

keys = chars.copy()
random.shuffle(keys)

# Encrypt
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += keys[index]

print(cipher_text)

# decrypt
cipher_text = input("Enter a message to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = keys.index(letter)
    plain_text += chars[index]

print(plain_text)