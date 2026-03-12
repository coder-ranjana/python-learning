#WAP to enter marks of 3 subjects form the user and store them in a dictionary. Start with an empty dictionary & add one bt one. Use subject name as kay & marks as value.

marks = {}

x = int(input("enter phy : "))
marks.update({"phy" : x})

x = int(input("enter math : "))
marks.update({"marks" : x})

x = int (input("enter chem : "))
marks.update({"chem" : x})

print(marks)




