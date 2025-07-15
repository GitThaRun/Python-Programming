list1 = [1,2,4,6,7,50]
Max_Num = list1[0]
Min_Num = list1[0]

for num in list1:
    if num > Max_Num:
        Max_Num = num
    if num < Min_Num:
        Min_Num = num
print(f"MaxiMum Number in List : {Max_Num}")
print(f"Minimum Number : {Min_Num}")