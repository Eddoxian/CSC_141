while True:
    first = input("\nFirst number (or q to quit): ")
    if first == 'q':
        break
    second = input("Second number: ")
    if second == 'q':
        break
    try:
        result = int(first) + int(second)
    except ValueError:
        print("Please enter valid numbers.")
    else:
        print(f"The sum is {result}")
try:
    x = int(input("First number: "))
    y = int(input("Second number: "))
except ValueError:
    pass
else:
    print(f"Sum: {x + y}")