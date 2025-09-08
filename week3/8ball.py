import random
answers = ['yes', 'no', 'maybe', 'plausible']
print("What do you seek")
question = input()
answer = random.choice(answers)
print(answer)