filename = 'programming_poll.txt'

while True:
    reason = input("Why do you like programming? (q to quit): ")
    if reason == 'q':
        break
    with open(filename, 'a') as file:
        file.write(reason + "\n")
