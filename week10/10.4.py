filename = 'guest_book.txt'

while True:
    name = input("Enter your name (or 'q' to quit): ")
    if name == 'q':
        break
    with open(filename, 'a') as file:
        file.write(f"{name}\n")
    print(f"Welcome, {name}!")