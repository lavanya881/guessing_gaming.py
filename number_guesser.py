import random

print("🎯 Welcome to the Number Guessing Game!")

# Step 1: Get range from user
low = int(input("Enter the lower range: "))
high = int(input("Enter the higher range: "))

# Step 2: Generate random number
number = random.randint(low, high)

# Step 3: Initialize variables
guess = 0
attempts = 0

print(f"\nI have selected a number between {low} and {high}. Try to guess it!")

# Step 4: Loop until correct guess
while guess != number:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("📉 Too low! Try again.")
    elif guess > number:
        print("📈 Too high! Try again.")
    else:
        print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")

print("Thanks for playing! 😊")