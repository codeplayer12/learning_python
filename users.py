class User():
    """Initialize the personal biography of users"""
    def __init__(self,first_name,last_name,gender, age,country):
        self.first_name =first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.country = country

    def describe_user(self):
        if self.gender == 'male':
            print(self.first_name.title() + " " + self.last_name.title() +"'s gender is " +
            self.gender.title() + ". His age is " + str(self.age) + " and his country of origin is " +
            self.country.title())
        else:
            print(self.first_name.title() + " " + self.last_name.title() +"'s gender is " +
            self.gender.title() + ". She age is " + str(self.age) + " and her country of origin is " +
            self.country.title())

greet_user = User('Lesley', 'Mpingo', 'male', 26, 'zimbabwe')
greet_user2 = User('small', 'abley', 'female', 28, 'bahamas')

greet_user.describe_user()
greet_user2.describe_user()
