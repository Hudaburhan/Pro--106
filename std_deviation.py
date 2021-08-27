import math
import csv
import statistics

with open('data2.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)
    
data= file_data[0]
def mean(data):
    n= len(data)
    total=0
    for x in data:
        total= total+int(x)
    
    mean = total/n
    print(mean)
    return mean

squared_List=[]
for number in data:
    a= int(number)- mean(data)
    a=a**2
    squared_List.append(a)

sum=0
for i in squared_List:
    sum+=i

result = sum/len(data)-1
std_dev = math.sqrt(result)
print(std_dev)
# print("Using standard libraries", statistics.stdev(data))