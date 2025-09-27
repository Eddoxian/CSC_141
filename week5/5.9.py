usernames = []

for user in usernames:
    if user == 'admin':
        print("Hello admin, would you like a status update?")
    else:
        print(f"Hello {user}, Welcome back.")
else:
    print("Awaiting user")