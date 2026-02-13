# Program to check divisibility by 5 and 35

# Step 1: Take input from the user
number = int(input("Enter a number: "))

# Step 2: Check divisibility conditions
# A number divisible by 35 must be divisible by both 5 and 7
if number % 5 == 0 and number % 35 == 0:
    print("The number is divisible by both 5 and 35.")
elif number % 5 == 0:
    print("The number is divisible by 5 but not by 35.")
elif number % 35 == 0:
    print("The number is divisible by 35.")
else:
    print("The number is not divisible by 5 or 35.")
