# Program to find the last digit of a number

# Step 1: Take input from the user
number = int(input("Enter a number: "))

# Step 2: Find the last digit
# Using modulus operator (% 10)
last_digit = abs(number) % 10   # abs() handles negative numbers

# Step 3: Display the result
print("The last digit of the number is:", last_digit)
