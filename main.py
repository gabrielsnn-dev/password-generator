import random

print("Welcome to the password generator")

symbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@#!*&'

number = int(input('Amount of passwords to generate: '))
length = int(input('Your password length: '))

print('\nYour passwords:')

for pswd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(symbols)
    print(passwords)