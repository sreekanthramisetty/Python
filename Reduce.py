from functools import reduce
numbers = [3, 4, 6, 9, 34, 12]
result = reduce(lambda a,b:a+b,numbers,10)
print(result)

