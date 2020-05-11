# def person(name,**kwargs):
#     print(name)
#     for i,j in kwargs.items():
#         print(i,j)
#
#
# person(name="Sreekanth",age = 28,gender="Male")
#
#
# def add(a,b):
#     c = a + b
#     return c
# print(add(a = 8,b = 9))
#
# def add(a,**b):
#     c = a
#     print ("a %s" %a)
#     for i,j in b.items():
#         print(i,j)
#
# add(a = 8,b = 9,c = 10)

# def f(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# f(2,4,5,a=7,b=9,c=90)


def f(b,*args):
    print(args)
    print(b)

f(2,4,5,7)