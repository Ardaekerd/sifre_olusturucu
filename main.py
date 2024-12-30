kullanilibilir = "+-/*!&$?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

import random


def generate_password(numofchars):
    password = ""
    for i in range(numofchars):
        password += random.choice(kullanilibilir)
    return password

num_of_letters = int(input("kaç karakterli bir şifre istiyorsun?"))
password = generate_password(num_of_letters)
print(password) 
