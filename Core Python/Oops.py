# There are two types of variable
# 1) Class variable and 2) Instant variable

# Class variable are constant no matter how many object are
# you created

# Whereas instant variable are difference for each and every
# object

# Constructor name should be __init__

# self keyword is mandatory for calling variable names into method

class Calculator:
    num = 100               # This one is class variable

    # Default constructor
    def __init__(self, a, b):
        self.firstNum = a
        self.secondNum = b
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now executing method in class")

    def summation(self):
        return self.firstNum + self.secondNum

obj = Calculator(2, 10)          # Syntax to create objects in python
obj.getData()
print(obj.summation())

obj2 = Calculator(5, 8)
obj2.getData()
print(obj2.summation())