#active variable ver
while True:
    age_input = input("Enter your age (or 'quit' to stop):  ")
    
    if age_input.lower() == 'quit':
        activate = False
    else:
        age = int(age_input)
    if age < 3:
        print("Your ticket is free")
    elif age <= 12:
        print("Your ticket is 10$")
    else:
        print("Your ticket costs 15$")

#break ver
while True:
    age_input = input("Enter your age (or 'quit' to stop):  ")
    
    if age_input.lower() == 'quit':
        break
    
    age = int(age_input)
    if age < 3:
        print("Your ticket is free")
    elif age <= 12:
        print("Your ticket is 10$")
    else:
        print("Your ticket costs 15$")

#conditional test ver
age_input = ""
while age_input.lower() != "quit":
    age_input = input("Enter your age (or 'quit' to stop):  ")
    
    if age_input.lower() != 'quit':
        age = int(age_input)
    
    age = int(age_input)
    if age < 3:
        print("Your ticket is free")
    elif age <= 12:
        print("Your ticket is 10$")
    else:
        print("Your ticket costs 15$")