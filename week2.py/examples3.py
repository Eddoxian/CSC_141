#number guessing game
from random import randint
answer = randint(1, 100) #picks a number between 1 and 100

while True:
    print("Enter your guess")
    guess = input()
    guess = int(guess) #this allows guess to become an integer
    if guess == answer: #If the answer and guess are the same
        print("You win") #Then this happens
        break
    if guess > answer: #But if guess is over the answer
        print("Too high") #It will print this
    if guess < answer: #and if the guess is lower than the answer
        print("Too low") #it will print this
print("Game Over")