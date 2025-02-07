import random
import string

chars = " "+ string.digits + string.ascii_letters + string.punctuation
chars = list(chars)

keys =chars.copy()

random.shuffle(keys)

# print(f"chars : {chars}")
# print(f"keys : {keys}")

#Encrypt

plain_text = input("Enter a text to encrypt")
cypher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cypher_text += keys[index]

print(f"Original text : {plain_text}")
print(f"Encrypted Message : {cypher_text}")

#Decrypt
cypher_text = input("Enter a text to encrypt")
plain_text = ""

for letter in cypher_text:
    index = keys.index(letter)
    plain_text += chars[index]

print(f"Encrypted Message: {cypher_text}")
print(f"Original Message : {plain_text}")
