# stringConcat = input("Enter the String : ")
# for i in stringConcat:
#     if stringConcat.index(i)%2 == 0 and i.isalpha() == True:
#         print(i,end = '')

###########################################

# stringConcat = input("Enter the String : ")
# s = ""
# for i in stringConcat:
#     s = i + s
#     print(s)

###########################################
str = 'acab'
ran  = len(str)
seta = []
for i in range(ran):
    x = str[i]
    for j in range(i + 1,ran):
        a = 1
        y = str[j]
        if x == y:
            a += 1
            print(x,a)

            print(seta)









