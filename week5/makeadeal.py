from random import randint
win_count = 0
trials = 1000
for trial in range(trials):
    doors = [0, 1, 2]
    prize_door = randint(0, 2)
    guess_door = randint(0, 2)
    print(f"prize door: {prize_door}")
    print(f"original guess door: {guess_door}")

    takeaway_door = randint(0, 2)
    while takeaway_door == prize_door or takeaway_door == guess_door:
        takeaway_door = randint(0, 2)
    print(f"takeaway door: {takeaway_door}")
    del doors[takeaway_door]
    index = 0
    for door in doors:
        if door == guess_door:
            del doors[index]
            break
        index += 1

    guess_door = doors[0]
    if guess_door == prize_door:
        print("You found the prize")
        win_count += 1
    else:
        print("wrong")
print(f"Winning percentage: {win_count / trials}")