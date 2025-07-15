#  pattern format
#  *****
#  ****
#  ***
#  **
#  *

rows = int(input("Enter Rows : "))

for i in range(rows):
    for j in range(rows - i):
        print("*", end = "")
    print()