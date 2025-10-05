person1 = {"First_Name" : "Mike",
           "Last_Name" : "Richardson",
           "City" : "New York",
           "Age": "43"}
person2 = {"First_Name" : "Nor",
           "Last_Name" : "Bull",
           "City" : "Bangalor",
           "Age": "27"}
person3 = {"First_Name" : "Mary",
           "Last_Name" : "Jane",
           "City" : "Dubai",
           "Age": "64"}
people = [person1, person2, person3]

for person in people:
    print (f"\n{person['First_Name']} {person['Last_Name']}")
    print(f"Age: {person['Age']}")
    print(F"City: {person['City']}")