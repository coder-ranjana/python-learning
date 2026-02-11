# WAP to check a number entred by the user is odd or even

num = int(input("enter number: "))

rem = num % 2

if (rem == 0):
    print("EVEN")
else:
    print("ODD")