# Here we'll inherit properties from parent to child class
# Oops file is the file where we have base class

# Make sure to import base class to child class
# Make sure to add base class name into child class
# If you have constructor which isn't default then make sure to
    # Class parent constructor in child contractor

from Oops import Calculator

class Child(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 10)

    def getCompleteData(self):
        return self.num2 + self.num + self.summation()

obj = Child()
print(obj.getCompleteData())
