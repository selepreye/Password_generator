import random
import string

length = int(input("Enter you password length: "))

chars = string.ascii_letters
chars += string.digits
chars += string.punctuation

password = ""

for i in range(length):
    password += random.choice(chars)

print("Your generated password: ", password)