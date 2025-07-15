a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))

gcd = 1
for i in range(1,min(a,b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

lcm = max(a,b)
while True:
    if lcm % a == 0 and lcm % b == 0:
        break
    lcm += 1

print(f"GCD of {a} and {b} is : {gcd}")
print(f"LCm of {a} and {b} is : {lcm} ")