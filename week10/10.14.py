import json

def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def get_new_username():
    username = input("What is your name? ")
    with open('username.json', 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        correct = input(f"Are you {username}? (y/n): ")
        if correct.lower() == 'y':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We’ll remember you next time, {username}!")
    else:
        username = get_new_username()
        print(f"We’ll remember you next time, {username}!")

greet_user()