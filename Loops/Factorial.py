num = int(input("Enter a Number : "));

fact = 1

if(num < 0):
    print("Factorial not defined for negative numbers")
else:
    for i in range(1,num + 1):
        fact *= i
    print(f"Factorial of {num} is : {fact}")
    