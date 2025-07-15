# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *

rows = int(input("Enter Rows : "))

for i in range(1,rows):
    print("*" * i + " " * 2 * (rows - i) + "*" * i)

for i in range(rows,0,-1):
    print("*" * i + " " * 2 * (rows - i) + "*" * i)