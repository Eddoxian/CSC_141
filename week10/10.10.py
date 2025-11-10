filename = 'Gutenberg.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print("File not found.")
else:
    words = contents.lower().split()
    count = words.count('the')
    print(f"'the' appears {count} times.")