class Dog():
    """A simple attempt to model a dog."""

    def __init__(self,name,age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in a response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in a response to a command."""
        print(self.name.title() + " rolled over!")

    def jump(self):
        """Simulate jumpig over a response to a command."""
        print(self.name.title() + " jumped!")
