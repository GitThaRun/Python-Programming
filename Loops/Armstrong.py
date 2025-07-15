num = int(input("Enter a Number : "))

power = len(str(num))

temp = num
result = 0

while(temp > 0):
    digit = temp % 10
    result += digit ** power
    temp //= 10

if result == num:
    print(f"{num} is an Armstrong Number")
else:
    print("Not an Armstrong Number")