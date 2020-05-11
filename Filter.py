# alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o']
#
# def VowelCheck(alphabet):
#     Vowel = ['a','e','i','o','u']
#     if alphabet in Vowel:
#         return  True
#     else:
#         return False
#
# VowelList = list(filter(VowelCheck,alphabets))
# print(VowelList)

# alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o']
# VowelLst = []
# for i in alphabets:
#     Vowel = ['a','e','i','o','u']
#     if i in Vowel:
#         VowelLst.append(i)
#         print(VowelLst)
#
#
# randomList = [1, 'a', 0, False, True, '0']
#
# filteredList = filter(None, randomList)
#
# print('The filtered elements are:')
# for element in filteredList:
#     print(element)

scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
filer_List = list(filter(lambda a : a > 75,scores))
print(filer_List)

# palindrome
dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")
palindromes = list(filter(lambda a:a==a[::-1],dromes))
print(palindromes)