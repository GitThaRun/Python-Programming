print("Student Grade Calculator : ")

sub1 = int(input("Enter Subject1 Marks : "))
sub2 = int(input("Enter Subject2 Marks : "))
sub3 = int(input("Enter Subject3 Marks : "))
sub4 = int(input("Enter Subject4 Marks : "))
sub5 = int(input("Enter Subject5 Marks : "))

total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = total / 5

print(f"Marks Obtained : {total} ")
print(f"Percentage : {percentage:.2f}")

if(percentage >= 90):
    grade = 'A+'
elif(percentage >= 80):
    grade = 'A'
elif(percentage >= 70):
    grade = 'B'
elif(percentage >= 60):
    grade = 'C'
elif(percentage >= 50):
    grade = 'D'
else:
    grade = "Fail"

print(f"Grade : {grade}")
