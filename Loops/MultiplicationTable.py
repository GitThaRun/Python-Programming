num = int(input("Enter which Table to Print : "))

print("Multiplication Table of {num} is :")

for i in range(1,21):
    result = num * i
    print(f"{num} x {i} = {result}")