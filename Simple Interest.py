# Simple Interest Calculator in Python

# Step 1: Take input from the user
# Principal amount (P)
principal = float(input("Enter the Principal amount: "))

# Rate of interest per year (R)
rate = float(input("Enter the Rate of Interest (per annum): "))

# Time period in years (T)
time = float(input("Enter the Time (in years): "))

# Step 2: Calculate Simple Interest using the formula
# Simple Interest = (P * R * T) / 100
simple_interest = (principal * rate * time) / 100

# Step 3: Display the result
print("Simple Interest is:", simple_interest)
