class A:
    def show(self):
        print("PARENT CLASS")

class B(A):
    def show(self):
        super(B, self).show()
        print("CHILD CLASS")
    # pass
a = A()
b = B()
b.show()
