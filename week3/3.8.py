location = ["cyprus", "france", "egypt", "japan", "china"]
original = location[:]
print(location)
alphabetical = sorted(location)
print(alphabetical)
print(original)
location.reverse()
print(location)
location.reverse()
print(location)
sorted_location = sorted(location, reverse=True)
print(sorted_location)