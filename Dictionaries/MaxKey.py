dict = {'A' : 10,'B' : 35,'C' : 100}
max_key = None
max_val = float('-inf')

for key in dict:
    if dict[key] > max_val:
        max_val = dict[key]
        max_key = key
print("Key with Max Value : ",max_key)