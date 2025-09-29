from random import choice

capitals = {"US" : "Washington",
            "Canada" : "Ottowa",
            "Japan" : "Tokyo",
            "France" : "Paris"}
country = (choice(list(capitals.keys())))

print(F"What is the capital of {country}?")
answer = ()
if answer == capitals[country]:
    print("You got it")
else:
    print(f"Nope, the answer it {capitals[country]}")