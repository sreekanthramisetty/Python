# s = 10
# def f():
#    print(s)
#
# print(s)
# f()
# print(s)

# # # # # # # # #  # # # # #  # # # # # #  #

# s = 20
# def f():
#    s = 30
#    print(s)

# print(s)
# f()
# print(s)

# # # # # # # # #  # # # # #  # # # # # #  #
# We cannot print global variable directly inside the functions if we are assigning a value after the print ,without declaring again like above.

# s = 20
# def f():
#    print(s)
#    s = 30 #Due to this we caanot
#    print(s)
#
# print(s)
# f()
# print(s)

#
# s = 20
# def f():
#    global s
#    print("Inside Function Global",s)
#    s = 30
#    s = s + 10
#    print("Last",s)
#
# print("Out Of Function Global",s)
# f()
# print("Final",s)
#
#
# def add():
#     x = 15
#
#     def change():
#         global x
#         x = 20
#         print("Function: ", x)
#     print("Before making change: ", x)
#     print("Making change")
#     change()
#     print("After making change: ", x)
# add()
# print("Value of x", x)

# a = 10
# print(id(a))
# def f():
#     a = 9
#     x = globals()['a']
#     print(id(x))
#     print(a)
#     globals() ['a'] = 15
# f()
# print(id(a))
# print(a)
#
# a = 10
# def f():
#     print(a)
#     s = a + 10
#     print(s)
# f()