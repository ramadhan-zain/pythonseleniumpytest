#self keyword is mandatory for calling variable names into method
#instance and class variables have whole different purposes
# constructor name should be __init__
#'new' keyword is not required when you create object

#classes are user defined blueprint or prototype
class Calculator:
    num = 100  #class variables

    #default constructor
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("I am created when the object is created")

    def get_data(self):
        print("I am now executing as method in class")

    def summation(self):
        return self.a + self.b

# obj = Calculator(2, 100)
# obj.get_data()
# print(obj.num)
# print(obj.summation())