class Restaurant():
    """Initializes a class on a restaurant"""

    def __init__(self,restaurant_name,cuisine):
        """Initializes a default method with the arguments"""
        self.restaurant_name = restaurant_name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print(self.restaurant_name.title() +  " restaurant serves " + self.cuisine.title())

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open")

restaurant = Restaurant("armenia","beef")
restaurant2 = Restaurant("times", "chicken")
restaurant3 = Restaurant("maka", "smoked pork")
print(restaurant.restaurant_name.title() + " is a good restaurant")
print("It serves " + restaurant.cuisine.title() + " cuisine")
restaurant.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
restaurant.open_restaurant()
