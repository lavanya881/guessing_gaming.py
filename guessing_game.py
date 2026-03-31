import random

number = random.randint(1, 100)
guess = None

while guess != number:
    guess = int(input("Enter your guess (1-100): "))
    
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Correct! You guessed the number.")