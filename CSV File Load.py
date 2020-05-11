import csv
from datetime import datetime
path = "E:\Files\socratica.csv"
file = open(path,newline = '')
list = [line for line in open(path)]
# print(list[0].strip().split(','))
# print(list[1].strip().split(','))
# print(dir(csv))
reader = csv.reader(file)
# print(reader)
header = next(reader)
data = []
for row in reader:
    date = row[0]
    open_price = float(row[1])
    High = float(row[2])
    Low = float(row[3])
    Close = float(row[4])
    volume = int(row[5])
    Adj_Close = float(row[6])
    data.append(row)
# print(data)
# file.close()

returns_path = "E:\Files\GoogleReturns.csv"
file = open(returns_path,"w")
writer = csv.writer(file)
writer.writerow(["Date","Return"])
#
# for i in range(len(data) - 1):
#     todays_row = data[i]
#     print(todays_row[0])
#     print(todays_row[-1])
#     print(data[i+1])
