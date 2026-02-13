# Program to calculate Area and Volume of a Cube

# Step 1: Take input from the user
# Side length of the cube
side = float(input("Enter the side length of the cube: "))

# Step 2: Calculate the total surface area of the cube
# Formula: Total Surface Area = 6 * side * side
surface_area = 6 * side * side

# Step 3: Calculate the volume of the cube
# Formula: Volume = side * side * side
volume = side * side * side

# Step 4: Display the results
print("Total Surface Area of the cube is:", surface_area)
print("Volume of the cube is:", volume)
