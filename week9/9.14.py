import random
lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']
winning_ticket = random.sample(lottery_pool, 4)
print("Winning ticket is:")
print(winning_ticket)