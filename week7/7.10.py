responses = {}

polling_active = True

while polling_active:
    name = input("What is your name")
    vacation = input("Where do you want to go?")

    responses[name] = vacation

    repeat = input(f"Would you like someone else to respond? (Yes / No)").strip().lower()
    if repeat.lower() == 'No':
        polling_active = False

    print("\nPoll Results Are In")
    for name, place in responses.items():
        print(f"{name.title()} would like to visit {place.title()}")