num = int(input("Enter a Number : "))

original = num
reverse = 0

while(num > 0):
    last = num % 10
    reverse = reverse * 10 + last
    num //= 10

if(original == reverse):
    print(f"{original} is a palindrome Number")

else:
    print("Not a Palindrome Number")