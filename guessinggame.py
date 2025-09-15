import random
words = ["pears", "man", "tree", "bear"]
word = "PYTHON"
secret = secret = ["_" for letter in word]
print("".join(secret))

while "".join(secret) != word:
    print("Guess a letter")
    guess = input()
    guess = guess.upper()
    if guess in word:
        letter_index = word.index(guess)
        secret[letter_index] = guess
    else:
        print("Not in word")
    print("".join(secret))
print("Game Over")