filename = 'learning_python.txt'

with open(filename) as file:
    lines = file.readlines()

for line in lines:
    print(line.replace('Python', 'C').strip())