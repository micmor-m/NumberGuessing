from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between1 and 100.")

number = random.randint(1, 100)
difficulty = input("Choose a difficulty. type 'easy' or 'hard': ")

attempts = 10
run = True

if difficulty != 'easy':
    attempts = 4

while attempts > 0 and run:
    print(f"You have {attempts} remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > number:
        print("Too high.\nGuess again.")
    elif guess < number:
        print("Too low.\nGuess again.")
    else:
        run = False
    attempts -= 1

if not run:
    print(f"You got it! The answer was {number}")
else:
    print("You have run out of guesses, you lose.")
