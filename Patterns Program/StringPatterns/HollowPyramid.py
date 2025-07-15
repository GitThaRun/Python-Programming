#    A
#   A B
#  A   C
# A B C D

rows = int(input("Enter Rows : "))

for i in range(rows):
    print(" " * (rows - i - 1),end = "")

    for j in range(i + 1):
        if j == 0 or j == i or i == rows - 1:
            print(chr(65 + j),end = " ")
        else:
            print(" ",end = " ")
    print()