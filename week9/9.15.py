import random
lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']
winning_ticket = random.sample(lottery_pool, 4)
count = 0
while True:
    count += 1
    my_ticket = random.sample(lottery_pool, 4)
    if my_ticket == winning_ticket:
        break
print(f"It took {count} tries to win the lottery!")
print(f"Winning ticket: {winning_ticket}")