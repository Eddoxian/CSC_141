import random
words = ["pears", "man", "tree", "bear"]
word = "PYTHON"
secret = ["_" for letter in word]
print("".join(secret))

while "".join(secret) != word:
    print("Guess a letter")
    guess = input()
    guess = guess.upper()
    if guess in word:
        index = 0
        for letter in word:
            if letter == guess:
                secret[index] = letter
            index += 1
    else:
        print("Not in word")
    print("".join(secret))
print("Game Over")