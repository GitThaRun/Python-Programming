#      1
#     1 1
#    1 2 1
#   1 3 3 1
#  1 4 6 4 1

rows = int(input("Enter Rows : "))

for i in range(rows):
    value = 1
    print(" " * (4 * (rows - i)), end = "")

    for j in range(i + 1):
        print(f"{value:4d}", end = "")
        value = value * (i - j) // (j + 1)
    print()