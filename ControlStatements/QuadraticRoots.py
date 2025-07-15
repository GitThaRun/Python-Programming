import math
print("Quadratic Equation Solver : ax² + bx + c = 0")

a = float(input("Enter Coefficient of A : "))
b = float(input("Enter Coefficient of B : "))
c = float(input("Enter Coefficient of c : "))

Discriminant = b ** 2 - 4 * a * c

if Discriminant > 0:
    root1 = (-b + math.sqrt(Discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(Discriminant)) / (2 * a)
    print("Two Real and Distinct Roots")
    print(f"Root1 : {root1:.2f}")
    print(f"Root2 : {root2:.2f}")

elif Discriminant == 0:
    root = -b / (2 * a)
    print("Two Real And Equal Roots")
    print(f"Root : {root:.2f}")
else:
    real = -b / (2 * a)
    imaginary = math.sqrt(abs(Discriminant)) / (2 * a)
    print("Complex Roots")
    print(f"Root1 : {real:.2f} +{imaginary : .2f}i")
    print(f"Root2 : {real:.2f} -{imaginary : .2f}i")