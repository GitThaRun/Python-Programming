#         1
#       1 2 1
#     1 2 3 2 1
#   1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1

rows = int(input("Enter Rows : "))

for i in range(1,rows + 1):
    print("  " * (rows - i), end = "")

    for j in range(1,i + 1):
        print(j, end = " ")

    for j in range(i - 1,0,-1):
        print(j, end = " ")
    
    print()
    