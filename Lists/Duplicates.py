list1 = [1,2,4,5,3,2,3,9]
unique = []

for item in list1:
    if item not in unique:
        unique.append(item)

print("List without Duplicates : ",unique)