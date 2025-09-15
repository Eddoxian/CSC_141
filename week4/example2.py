evens = [n if n % 2 == 0 else 0 for n in range(2, 21)]
print(evens)
evens = [n for n in range(2,21) if n % 2 == 0]
print(evens)
evens_doubled = [n * 2 for n in range(2,21) if n % 2 == 0]
print(evens_doubled)