lstElements = int(input("No .Of Elements to list: "))
Lst = []
for i in range(lstElements):
    Str = input("Enter the input: ")
    Lst.append(Str)
print(Lst)
for j in Lst:
    print(Lst.index(j))

