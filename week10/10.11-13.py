#10.11
import json

filename = 'favorite_number.json'
number = input("What’s your favorite number? ")

with open(filename, 'w') as f:
    json.dump(number, f)
    print("We’ll remember your number!")

#10.12
import json

filename = 'favorite_number.json'

with open(filename) as f:
    number = json.load(f)
    print(f"I know your favorite number! It’s {number}.")

#10.13
import json

filename = 'favorite_number.json'

try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    number = input("What’s your favorite number? ")
    with open(filename, 'w') as f:
        json.dump(number, f)
    print("Got it, I’ll remember that.")
else:
    print(f"Your favorite number is still {number}.")