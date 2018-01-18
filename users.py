class User():
    """Initialize the personal biography of users"""
    def __init__(self,first_name,last_name,gender, age,country):
        self.first_name =first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.country = country
        self.login_attempts = 0

    def increment_login_attempts(self,attempts=1):
        """Increments the number of login attempts made by the user to a system"""
        self.login_attempts += attempts

    def reset_login_attempts(self,reset=0):
        """Resets the login attempts back to the default zero(0)"""
        self.login_attempts = reset

    def describe_user(self):
        if self.gender == 'male':
            print(self.first_name.title() + " " + self.last_name.title() +"'s gender is " +
            self.gender.title() + ". His age is " + str(self.age) + " and his country of origin is " +
            self.country.title() + " and logging in our system " + str(self.login_attempts) + " times")
        else:
            print(self.first_name.title() + " " + self.last_name.title() +"'s gender is " +
            self.gender.title() + ". She age is " + str(self.age) + " and her country of origin is " +
            self.country.title() + " and logging in our system " + str(self.login_attempts) + " times")

greet_user = User('Lesley', 'Mpingo', 'male', 26, 'zimbabwe')
greet_user2 = User('small', 'abley', 'female', 28, 'bahamas')

greet_user.describe_user()
greet_user.increment_login_attempts()
greet_user.increment_login_attempts()
greet_user.increment_login_attempts()
greet_user.increment_login_attempts()
greet_user.describe_user()
greet_user.reset_login_attempts()
greet_user.describe_user()
greet_user2.describe_user()
