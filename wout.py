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

with open("Testfile.txt") as f1:
    with open("Outfile.txt","w") as f2:
        f2.write(f1.read())













