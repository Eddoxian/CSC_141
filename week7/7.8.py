sandwich_orders = ['tuna', 'ham', 'turkey']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich.title())