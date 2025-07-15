    #     *
    #    ***
    #   *****
    #  *******
    # *********
    #  *******
    #   *****
    #    ***
    #     *
rows = int(input("Enter Rows : "))

for i in range(1,rows):
    print(" " * (rows - i) + "*" * (2 * i - 1))
for i in range(rows,0,-1):
    print(" " * (rows - i) + "*" * (2 * i - 1))