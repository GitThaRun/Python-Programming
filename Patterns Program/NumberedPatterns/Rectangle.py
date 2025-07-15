# 1 2 3 4 5
# 2 3 4 5 1
# 3 4 5 1 2
# 4 5 1 2 3
# 5 1 2 3 4

Rows = int(input("Enter Rows : "))

for i in range(Rows):
    for j in range(1,Rows + 1):
        num = (i + j) % Rows
        if num == 0:
            num = Rows
        print(num, end = "")
    print()