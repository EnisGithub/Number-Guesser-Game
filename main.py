import random
n = random.randrange(1,10)
guess = int(input("Enter any number: "))
while n!= guess:
    if guess < n:
        print("Too low")
        guess = int(input("Enter number again: "))
    if guess > n:
        print("Too high!")
        guess = int(input("Enter number again: "))
    if guys = n:
print("you guessed it right!!")
