rows = int(input("Enter Rows : "))

for i in range(rows,0,-1):
    print(" " * (rows - i) + "*" * (2 * i - 1))