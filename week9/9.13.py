import random
class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return random.randint(1, self.sides)

six_sided = Die()
print("6-sided die rolls:")
for _ in range(10):
    print(six_sided.roll_die(), end=" ")
print("\n")

ten_sided = Die(10)
print("10-sided die rolls:")
for _ in range(10):
    print(ten_sided.roll_die(), end=" ")
print("\n")

twenty_sided = Die(20)
print("20-sided die rolls:")
for _ in range(10):
    print(twenty_sided.roll_die(), end=" ")