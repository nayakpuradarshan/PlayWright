# Learn about CLASS
from selenium.webdriver.common.print_page_options import PrintOptions


# classes are user defined blueprint or prototype
# sum, multiplication, addition, constant
# methods, class variable, instance variable, constructor etc...
# method and function both are same thing, when one use function inside the class is called method

# What is constructor in class?
    # constructor is one method, which is automatically called when you create object for any class.
    # In simple word constructor is one method.

# There are two types of variable in python
    # class variable
    # instance variable

# self keyword is mandatory for calling variable names into method
# instance and class variable have whole different purpose
# constructor name should be __init__


class Calculator:
    num = 100           # class variable

    # default constructor
    def __init__(self, a, b):
        self.firstNumber = a        # instance variable
        self.secondNumber = b       # instance variable
        print("I'm called automatically when object is created")

    def getData(self):
        print("i'm now executing as method in class")

    def summation(self):
        return self.firstNumber + self.secondNumber + self.num

obj = Calculator(2, 3)          # syntax to create objects in python
obj.getData()
print(obj.summation())


obj1 = Calculator(4, 5)          # syntax to create objects in python
print(obj1.summation())



print("******** inheritance *********")

# Learn about inheritance

# What is inheritance
    # Inheritance allows us to define a class that inherits all the methods and properties from parent class.

class ChildImpl(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 3, 3)

    def getCompletData(self):
        return self.num2 + self.num

obj3 = ChildImpl()
print(obj3.getCompletData())