while True:
    topping = input("Choose a topping (or 'quit' to stop):  ")
    if topping.lower() == 'quit':
        break
    print(f"You have added {topping}")