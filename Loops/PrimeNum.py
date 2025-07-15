import math
num = int(input("Enter a Number : "))

isPrime = True

if(num <= 1):
    isPrime = False
else:
    for i in range(2,int(math.sqrt(num) + 1)):
        if(num % 2 == 0):
            isPrime = False
            break
if(isPrime):
    print(f"{num} is a Prime Number")
else:
    print(f"Not a Prime Number")