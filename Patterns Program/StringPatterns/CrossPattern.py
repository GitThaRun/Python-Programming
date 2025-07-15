# A   A
#  B B 
#   C  
#  B B 
# A   A

rows = int(input("Enter rows : "))

for i in range(rows):
    for j in range(rows):
        if i == j or i + j == rows - 1:
            print(chr(65 + i),end = "")
        else:
            print(" ",end = "")
    print()