# # Assigning Functions to Variables
#
# def plus_one(number):
#     return number + 1
# add_one = plus_one
# print(add_one(5))

# Defining Functions Inside other Functions

# def plus_One(num):
#     def add(num):
#         return num + 1
#     result = add(num)
#     return result
#
# print(plus_One(5))

# Passing Functions as Arguments to other Functions

# def plus_one(num):
#     return  num + 1
#
# def function_Call(function):
#     number = 4
#     return function(number)
#
# print(function_Call(plus_one))

#Functions Returning other Functions

# def plus():
#     def add():
#         return "Say Hi"
#     return add
#
# all = plus()
# all()

# Nested Functions have access to the Enclosing Function's Variable Scope

# def print_message(message):
#     "Enclosong Function"
#     def message_sender():
#         "Nested Function"
#         print(message)
#
#     message_sender()
# print_message("Some random message")
# #
# # def f1(a,b):
# #     c = a/b
# #     print(c)
# #
# # def f(func):
# #     def calc(a,b):
# #         if a < b:
# #             a,b = b,a
# #         return func(a,b)
# #     return calc
# #
# # Result = f(f1)
# #
# # Result()
#
# #
# # def hello_function():
# #     a = 5
# #     def say_hi():
# #         c = a
# #         return "Hi"
# #     return say_hi
# # hello = hello_function()
# # hello()
#
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper
@uppercase_decorator
def say_hi():
    return 'hello there'

decorate = uppercase_decorator(say_hi)
print(decorate())
#
# def decorator_with_arguments(function):
#     def wrapper_accepting_arguments(arg1, arg2):
#         print("My arguments are: {0}, {1}".format(arg1,arg2))
#         function(arg1, arg2)
#     return wrapper_accepting_arguments
#
# @decorator_with_arguments
# def cities(city_one, city_two):
#     print("Cities I love are {0} and {1}".format(city_one, city_two))
#
# cities("Nairobi", "Accra")