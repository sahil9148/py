# Program to check voting eligibility

# Step 1: Take age input from the user
age = int(input("Enter your age: "))

# Step 2: Check voting eligibility
# Legal voting age is 18 years
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
