s1 = input("Enter First String : ").replace(" ","").lower()
s2 = input("Enter Second String : ").replace(" ","").lower()

if sorted(s1) == sorted(s2):
    print("The Strings Are Anagrams")
else:
    print("Not Anagrams")