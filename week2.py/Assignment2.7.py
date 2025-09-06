name = " Frank " #the space between the quotes are called whitespace.

name = name.lstrip() #closes left whitespace
name = name.rstrip()#closes right whitespace
name = name.strip() #closes both sides
print(name.strip())

name = " Frank\n\nMel " #\n is new line

print(name.strip())

name = " Frank\tMel " #\t is tab

print(name.strip())

