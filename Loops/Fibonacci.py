sequence = int(input("Enter Upto Sequence : "))

a = 0
b = 1
count = 0

print("Fibonacci Sequence : ")

while(count < sequence):
    print(a,end = " ")
    next = a + b
    a = b
    b = next
    count += 1