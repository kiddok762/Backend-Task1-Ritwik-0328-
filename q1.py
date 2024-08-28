s1 = input("Enter the first string : ")
s2 = input("Enter the second string : ")

checklist = []

for i in range(0,len(s1)-1):
    for j in range(0,len(s2)-1):
        if (s2[j] == s1[i]):
            checklist.append("Y")
        else:
            checklist.append("N")


if (checklist[0] == "Y"):
    print("The strings are not complementary.")
else:
    print("The string are complementary.")