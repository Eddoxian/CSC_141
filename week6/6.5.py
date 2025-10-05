rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'atbarah': 'ethiopia'
}


for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")


print("\nRivers:")
for river in rivers.keys():
    print(river.title())


print("\nCountries:")
for country in rivers.values():
    print(country.title())