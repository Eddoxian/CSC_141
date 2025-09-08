import random

spanish = ["perro", "gatto", "playa"]
english = ["dog", "cat", "beach"]

i = random.randint(0, len(spanish) -1)
print(spanish[i])
print("What is this in English?")
answer = input()
if answer == english[i]:
    print("You got it!")
else:
    print(f"No, the answer is {english[i]}")