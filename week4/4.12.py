foods = ['canoli', 'pizza', 'falafel', 'ice cream']
friends_foods = foods[:]
foods.append('spaghetti')
friends_foods.append('calzone')
for foods in foods:
    print(f"I like {foods}")
for foods in friends_foods:
    print(f"my friend likes {foods}")