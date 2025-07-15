text = input("Enter a String : ")

freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print("\nCharacter Frequencies : ")
for key in freq:
    print(f"{key} : {freq[key]}")