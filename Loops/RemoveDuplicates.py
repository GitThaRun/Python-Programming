text = input("Enter A String : ")

result = ""

seen = {}

for ch in text:
    if ch not in seen:
        result += ch
        seen[ch] = True
print(f"String After Removing Duplicates : {result}")