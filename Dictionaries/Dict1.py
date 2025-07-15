# Create a Dictionary from Two Lists (Keys + Values)

keys = ['a','b','c']
values = [0,1,2]

d = {}

for i in range(len(keys)):
    d[keys[i]] = values[i]
print("Created Dictionary : ",d)