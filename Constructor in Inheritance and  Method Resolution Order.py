class A:
    def __init__(self):
        print("From A Class INIT")

    def feature1(self):
        print("Feature 1 From Class A")

class B:
    def __init__(self):
        super().__init__()
        print("From B Class INIT")

    def feature2(self):
        print("Feature 2 From Class B")

class C(A,B):
    def __init__(self):
        super().__init__()  #Method Resolution Order Means C inherits A __init__ here not B
        print("From C Class INIT")

    def feature3(self):
        print("Feature 3 From Class C")
b = B()
c = C()


