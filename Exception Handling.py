import numpy
a = 4
b = 0
try:
    result = a/b
    print(result)
except ZeroDivisionError as e:
    print("Zero cannot in denominator",e)
finally:
    print("BYE!")
