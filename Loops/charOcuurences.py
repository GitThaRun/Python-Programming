s = input("Enter a String : ").lower()
ch = input("Enter Character to Find Occurence : ")

count = 0
for c in s:
    if c == ch:
        count += 1
print(f"\n Character '{ch}' occurred {count} Times")
