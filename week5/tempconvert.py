print("Are we using Celsius(C) for Fahrenheit(F)")
scale = input()
print(scale)
scale = scale.upper
print("How many degrees?")
degrees = input()
degrees = int(degrees)
if scale == "C":
    fahrenheit = (degrees * (9 / 5)) + 32
    print(fahrenheit)
elif scale == "F":
    Celsius = (degrees - 32) * (5 / 9)
    print(Celsius)
else:
    print("Not a valid scale")