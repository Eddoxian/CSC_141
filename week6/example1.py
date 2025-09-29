names = ["Brian", "Sarah", "Mary", "Jillian"]
salaries = [ 25, 20, 40, 50]
ages = [40, 20, 50, 30]

for i in range(len(names)):
    print(F"Name: {names[i]} Salary: {salaries[i]} Age: {ages[i]}")

print(names[0])

employees = {
    "Brian" : {"salary" : 25, "age" : 45},
    "Sarah" : {"salary" : 20, "age" : 25},
    "Mary" : {"salary" : 40, "age" : 50},
    "Jillian" : {"salary" : 50, "age" : 30},
}

#for i in range(len(names)):
    #print(F"Name: {names[i]} Salary: {salaries[i]} Age: {ages[i]}")
print(employees["Brian"])

populations = {
    "US" : 34000000,
    "Canada" : 40000000,
    "Japan" : 120000000
}

print(populations["US"])

for employee in employees:
    data = employees[employee]
    print(employee)
    print(data["salary"])
    print(data["age"])