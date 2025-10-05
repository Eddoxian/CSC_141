pet1 = {'animal_type': 'dog', 'owner': "Sal"}
pet2 = {'animal_type': 'cat', 'owner': "Mel"}
pet3 = {'animal_type': 'bird', 'owner': "Hel"}

pets = [pet1, pet2, pet3]

for pet in pets:
    print(f"\n{pet['owner']} owns a {pet['animal_type']}")