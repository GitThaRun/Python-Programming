# Move All Zeros to the End Without Changing Order of Others

list1 = [0,2,1,9,3,0,0,5,4]
result = []

for item in list1:
    if item != 0:
        result.append(item)

count = 0
for item in list1:
    if item == 0:
        count += 1
    
for i in range(count):
    result.append(0)

print("Required List : ",result)