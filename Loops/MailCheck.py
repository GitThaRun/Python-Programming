import re

mail = input("Enter Mail Id : ")

pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.%-]+\.[a-zA-Z]{2,}$'

if re.match(pattern,mail):
    print("Valid E-Mail Address")
else:
    print("Invalid Mail ID! Please check Again")