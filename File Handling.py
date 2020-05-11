# f = open("abc.txt",'w')
# f.write("Durga\n")
# f.write("Durga Soft\n")
# f.write("Durga Soft Operations\n")
# print("Data Stored Successfully\n")
# f.close()

# f = open("abc.txt",'a')
# f.write("Durga\n")
# f.write("Durga Soft\n")
# f.write("Durga Soft Operations\n")
# print("Data Stored Successfully\n")
# f.close()

# f = open("abc.txt",'w')
# lst = ["S\n","R\n","E\n","E\n","K\n","A\n","N\n","T\n","H"]
# f.writelines(lst)

f = open('abc.txt')
# print(f.read(3))
# print(f.readline())
# print(f.readline())
lines = f.readlines()
for line in lines:
    print(line,end = "")
#########################--------------------------------------------------------------################################

# with open("Testfile.txt","w") as f:
#     f.write("SREEKANTH\n")
#     f.write("IS A\n")
#     f.write("PYTHONIC\n")
#     print("Data Loaded Successfully")
#
# with open("Testfile.txt", "w") as f:
#     lst = ["SREEKANTH\n","DATA\n","ANALYST\n"]
#     for data in lst:
#         f.writelines(data)
#     print("Data Loaded Successfully")

########### --------------------------------------------------------------------------------------------##############

# with open("Testfile.txt","r") as f:
#     # print(f.read())
#     # print(f.read(12))
#     # print(f.readline())
#     # print(f.readline())
#     # print(f.readline())
#     lines = f.readlines()
#     for line in lines:
#         print(line,end = '')

########### --------------------------------------------------------------------------------------------##############
#
# with open("Testfile.txt") as f1:
#     with open("Outfile.txt","w") as f2:
#         f2.write(f1.read())













