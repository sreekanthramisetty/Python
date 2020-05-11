# class Student:
#     def __init__(self,name,rollno,ram,cpu):
#         self.name = name
#         self.rollno = rollno
#         self.lap = self.Laptop(ram,cpu)
#
#     def show(self):
#         self.lap.show()
#         print(self.name,self.rollno)
#
#     class Laptop:
#         def __init__(self,ram,cpu):
#             self.ram = ram
#             self.cpu = cpu
#
#         def show(self):
#             print(self.ram,self.cpu)
#
# s = Student("SREEKANTH","1234","4GB",'I5')
# Laptop = Student.Laptop("8GB",'I7')
# s.show()
# Laptop.show()
# # print(s.name,s.rollno)
#

class A:
    def __init__(self):
        print("A")

a = A()
