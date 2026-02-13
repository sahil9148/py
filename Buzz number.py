# Program to check whether a number is a Buzz Number

# Take input from the user
num = int(input("Enter a number: "))

# Check Buzz Number condition
if num % 7 == 0 or num % 10 == 7:
    print(num, "is a Buzz Number")
else:
    print(num, "is NOT a Buzz Number")
