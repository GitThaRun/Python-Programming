text = input("Enter String : ")

count = {}

for ch in text:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1

found = False
for ch in text:
    if count[ch] == 1:
        print(f"First Non-Repeating Character : {ch}")
        found = True
        break
if not found:
    print("No Repeating Characters")