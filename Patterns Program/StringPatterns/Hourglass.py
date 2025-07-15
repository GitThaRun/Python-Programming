# ABCDEDCBA
#  ABCDBA
#   ABCBA
#    ABA
#     A

rows = int(input("Enter Rows : "))

for i in range(rows):
    print(" " * i, end = "")
    
    for j in range(rows - i):
        print(chr(65 + j),end = "")
    
    for j in range(rows - i - 2,-1,-1):
        print(chr(65 + j),end = "")
    
    print()