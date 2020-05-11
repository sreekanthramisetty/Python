# class MyClass:
#     x = 5
# print(MyClass)
# # Object Creation
# p1 = MyClass()
# print(p1.x)
#
# int

class Computer:
    school = "Telusko"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def config(self):
        print("This is my computer:")

    @staticmethod
    def name():
        return "A"
    @classmethod
    def Drive(cls):
        print("Shared Drive")
        return cls.school
    def avg(self):
        return (self.m1 + self.m2+self.m3)/3


c = Computer(40,50,67)
c.config()
print(c.avg())
print(Computer.name())
print(c.Drive())
