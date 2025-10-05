places = {
    'mel': ['paris', 'athens', 'dubai'],
    'frank': ['france', 'puerto rico'],
    'bob': ['rome']
}

for name, places in places.items():
    print(F"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"{places}")