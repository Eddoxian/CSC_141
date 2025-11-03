class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, customers):
        self.number_served += customers

restaurant = Restaurant("The Lotus", "Chinese")
restaurant.set_number_served(20)
restaurant.increment_number_served(5)
print(f"Customers served: {restaurant.number_served}")