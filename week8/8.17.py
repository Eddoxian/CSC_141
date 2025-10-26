def make_pizza(size, *toppings):
    """What are you making?"""
    print(f"\nI am making a {size}-inch pizza with:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')