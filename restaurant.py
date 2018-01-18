class Restaurant():
    """Initializes a class on a restaurant"""

    def __init__(self,restaurant_name,cuisine):
        """Initializes a default method with the arguments"""
        self.restaurant_name = restaurant_name
        self.cuisine = cuisine
        self.number_served = 0

    def set_number_sevred(self,number_of_customer_served):
        """Sets the number of customers to be served."""
        self.number_served = number_of_customer_served

    def increment_number_served(self,served):
        """
        Increments the number of customers that have been served
        """
        self.number_served += served

    def describe_restaurant(self):
        print(self.restaurant_name.title() +  " restaurant serves " +
        self.cuisine.title() + " and number of people served are " +
        str(self.number_served))

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open")

restaurant = Restaurant("armenia","beef")


restaurant2 = Restaurant("times", "chicken")
restaurant3 = Restaurant("maka", "smoked pork")

print(restaurant.restaurant_name.title() + " is a good restaurant")
print("It serves " + restaurant.cuisine.title() + " cuisine")

restaurant.describe_restaurant()

restaurant.number_served = 5 #default setting of value using direct assignment
restaurant.describe_restaurant()

restaurant.set_number_sevred(25) #indirect assignment of values using a function
restaurant.describe_restaurant()

restaurant.increment_number_served(40) #calls function that increments the previously stored value
restaurant.describe_restaurant()

restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

restaurant.open_restaurant()
