import random
score = 0
keep_playing = True
number1 = random.randint(0, 100)
number2 = random.randint(0, 100)

print(f"What is {number1} + {number2}?")
user_answer = input()
user_answer = int(user_answer)
right_answer = number1 + number2
if user_answer == right_answer:
    print("Correct!")
    score += 1
else:
    print(f"Wrong!")
    score -= 1
print(f"Your score, {score}")