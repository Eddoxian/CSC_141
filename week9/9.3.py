class User:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}, {self.age}, from {self.location}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.")


user1 = User("Alice", "May", 28, "Seattle")
user2 = User("John", "Philip", 31, "New York")

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()