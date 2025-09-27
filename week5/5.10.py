old_usernames = ['Admin', 'charles', 'erika', 'emma', 'matt']
new_usernames = ['Mike', 'john', 'lucille', 'jules', 'rob']

current_usernames_lower = [user.lower() for user in old_usernames]

for new_user in new_usernames:
    if new_user.lower() in current_usernames_lower:
     print(f"Sorrry the username '{new_user} is already taken.")
    else:
       print(f"The username '{new_user} is available.")
