sandwich_orders = ['tuna', 'pastrami', 'ham', 'pastrami', 'turkey', 'pastrami']
print("Sorry, we have run out of pastrami!\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"Your {sandwich} sandwich is ready.")
    finished_sandwiches.append(sandwich)