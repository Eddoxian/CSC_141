cities = {
    'new york': {
        'country': 'usa',
        'population': 8_400_000,
        'fact': 'Known for having the first american pizzaria'
    },
    'Dubai': {
        'country': 'India',
        'population': 4_000_387,
        'fact': 'Dubai is notable for gold trade.'
    },
    'paris': {
        'country': 'france',
        'population': 2_100_000,
        'fact': 'Paris is famous for the Eiffel Tower.'
    }
}

for city, info in cities.items():
    print(f"\n{city.title()}:")
    print(f"  Country: {info['country'].title()}")
    print(f"  Population: {info['population']}")
    print(f"  Fact: {info['fact']}")