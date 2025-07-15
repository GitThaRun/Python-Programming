print("Simple Calculator")

print("Choose Your Operation : ")
print("1.Addition (+)")
print("2.Subtraction (-)")
print("3.Multiplication (*)")
print("4.Division (/)")

choice = int(input("Enter Your Choice : "))

num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))

if(choice == 1):
    print(f"Result : {num1} + {num2} = {num1 + num2}")
elif(choice == 2):
    print(f"Result : {num1} - {num2} = {num1 - num2}")
elif(choice == 3):
    print(f"Result : {num1} x {num2} = {num1 * num2}")
elif(choice == 4):
    if num2 != 0:
        print(f"Result : {num1} / {num2} = {num1 / num2}")
    else:
        print("Cannot Divide with zero")
else:
    print("Invalid Choice")