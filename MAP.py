from builtins import map

# Traditional Method

my_pets = ['alfred', 'tabitha', 'william', 'arla']
UpperList = []
for pet in my_pets:
    uppercase = pet.upper()
    UpperList.append(uppercase)
print(UpperList)

# Using MAP Method

UpperList_Map = list(map(str.upper,my_pets))
print(UpperList_Map)
# Assignment
circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]
length = len(circle_areas)
print(length)
result = list(map(round,circle_areas,range(1,length + 1)))
L_result = list(map(round,circle_areas,range(1,length)))
print(result,L_result)


my_string  = ['a','b','c','d','e']
my_numbers = [1,2,3,4,5]
results = list(zip(my_string,my_numbers))
print(results)

Lambda_result = list(map(lambda a,b:(a,b),my_string,my_numbers))
print(Lambda_result)

