# A
# B C
# D E F
# G H I J
# K L M N O

rows = int(input("Enter Rows : "))
char = ord('A')

for i in range(rows):
    for j in range(i + 1):
        print(chr(char),end = "")
        char += 1
    print()