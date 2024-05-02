# Example 4 - Guessing Game - Correct Solution
import random

num = random.randrange(1,101)

guess = int(input("What is the number?: "))

while guess != num:
    if guess > num:
        print("guess is too high, guess again")
    else: 
        print("guess is too low, guess again")

print("congratulations!")