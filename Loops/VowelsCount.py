text = input("Enter a String : ").lower()

vowels = "aeiou"
count = 0

for c in text:
    if c in vowels:
        count += 1
print(f"Number of Vowels in the String :{count}")