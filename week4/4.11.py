pizzas = ['cheese', 'pepperoni', 'sausage', 'mushroom']
friends_pizza = pizzas[:]
pizzas.append('new york style')
friends_pizza.append('supreme')
for pizzas in pizzas:
    print(f"I like {pizzas} pizzas")
for pizzas in friends_pizza:
    print(f"my friend likes {pizzas}")