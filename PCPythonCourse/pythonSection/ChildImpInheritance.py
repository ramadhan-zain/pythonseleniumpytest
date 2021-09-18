# from OOPPython import Calculator
#
# class ChildImpl(Calculator):
#     num2 = 200
#
#     def get_complete_data(self):
#         return self.num2 + self.num + self.summation()
#
#
# obj = ChildImpl(5, 5)
# print(obj.get_complete_data())

from OOPPython import Calculator

class ChildImpl(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 3)

    def get_complete_data(self):
        return self.num2 + self.num + self.summation()


obj = ChildImpl()
print(obj.get_complete_data())
