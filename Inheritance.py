#SINGLE INHERITANCE
#MULTI LEVEL INHERITANCE
#MULTIPLE INHERITANCE

# class A:
#     def feature1(self):
#         print("Feature 1 working")
#
#     def feature2(self):
#         print("Feature 2 working")
# #---------------------------------------------SINGLE LEVEL INHERITANCE------------------------------------A <- B
# class B(A):
#     def feature3(self):
#         print("Feature 3 working")
#
#     def feature4(self):
#         print("Feature 4 working")
#---------------------------------------------MULTI LEVEL INHERITANCE------------------------------------ A <- B <- C
# class C(B):
#     def feature5(self):
#         print("Feature 5 Working")
#
# a = A()
# a.feature2()
# a.feature1()
#
# b = B()
# b.feature1()
# b.feature2()
# b.feature3()
# b.feature4()
#
# c = C()
# c.feature1()
# c.feature2()
# c.feature3()
# c.feature4()
# c.feature5()

# --------------------------------------------------- MULTIPLE INHERITANCE --------------------------------------------
#
# class A:
#     def feature1(self):
#         print("Feature 1 working")
#
#     def feature2(self):
#         print("Feature 2 working")
#
# class B:
#     def feature3(self):
#         print("Feature 3 working")
#
#     def feature4(self):
#         print("Feature 4 working")
#
# class C(B,A):
#     def feature5(self):
#         print("Feature 5 Working")
#
# a = A()
# a.feature2()
# a.feature1()
#
# b = B()
# b.feature3()
# b.feature4()
#
# c = C()
# c.feature1()
# c.feature2()
# c.feature3()
# c.feature4()
# c.feature5()

