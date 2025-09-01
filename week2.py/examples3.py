#number guessing game
from random import randint
answer = randint(1, 100) #picks a number between 1 and 100

while True:
    print("Enter your guess")
    guess = input()
    guess = int(guess) #this allows guess to become an integer
    if guess == answer: #If the answer and guess 
        print("You win")
        break
    if guess > answer:
        print("Too high")
    if guess < answer:
        print("Too low")
print("Game Over")