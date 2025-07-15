# Formula : 1 + (n - 1) % 9

num = int(input("Enter a Number : "))
if(num == 0):
    print("Digital Root : 0")
else:
    print("Digital Root : ",1 + ((num - 1) % 9))
