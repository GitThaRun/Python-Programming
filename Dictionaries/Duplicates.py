dict = {'a':0,'b' : 1,'c' : 5,'d' : 1,'e' : 2}
seen = []
duplicates = []

for k in dict :
    val = dict[k]

    if val in seen and val not in duplicates:
        duplicates.append(val)
    else:
        seen.append(val)
print("Duplicates : ",duplicates)