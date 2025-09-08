runs = [1, 5, 2 , 3, 4, 7, 9, 12]
print("Average Score")
print(sum(runs) / len(runs))
print("Highest Score")
print(max(runs))
print("Lowest Score")
print(min(runs))

runs = [1, 5, 2 , 3, 4, 7, 9, 12]
highest = runs[0]
for score in runs:
    print(score)
    if score > highest:
        highest = score
print("Highest score found:")
print(highest)
print(max(runs))

runs = [1, 5, 2 , 3, 4, 7, 9, 12]
lowest= runs[0]
for score in runs:
    print(score)
    if score < lowest:
        lowest = score
print("Lowest score found:")
print(lowest)
print(min(runs))

runs = [1, 5, 2 , 3, 4, 7, 9, 12]
key = 12
for score in runs:
    if score == key:
        print("Found it!")
