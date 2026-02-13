# Program to check whether a number is Even or Odd

# Step 1: Take input from the user
number = int(input("Enter a number: "))

# Step 2: Check even or odd using modulus operator
# If remainder is 0 when divided by 2, the number is even
if number % 2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")
