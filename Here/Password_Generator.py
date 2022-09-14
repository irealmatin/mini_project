import random

print("Welcome:))\nthis is Password generator program...")

char_pass = 'abcdefghijklmnopqrstuvwxyzABCDEFGHILKLMNOPQRSTUVWXYZ0123456789~`!@#$%^&*()-_+=}{[]|\;:"<>,./?' # A-Z , a-z , symbol , 0-9 for make password

print("******\nAnswer the question below for make your password ...")

number = int(input("1 - How many password do you want :  "))
lenght = int(input("2 - input your password lenght :  "))

print("\nYour strong passwords are ready........")

for c in range(number):
    password = ''
    for n in range(lenght):
        password +=random.choice(char_pass)

    print(password)
