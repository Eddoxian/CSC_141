#number guessing game
from random import randint
answer = randint(1, 100)
guess = -1
while guess != answer:
    print("Enter your guess from 1 through a hundred")
    guess = input()
    guess = int(guess)
    if guess > answer:
        print("Too high")
    elif guess < answer:
        print("Too low")
print("Game Over")