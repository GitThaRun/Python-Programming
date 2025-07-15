original = {'a' : 0,'b' : 1,'c' : 2}
swapped = {}

for key in original:
    val = original[key]
    swapped[val] = key
print("Swapped Dictionary : ",swapped)