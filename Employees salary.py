n = int(input("Enter number of employees: "))
employees = {}

for i in range(n):
    name = input("Enter employee name: ")
    salary = float(input("Enter salary: "))
    employees[name] = salary

print("Employee Dictionary:")
print(employees)
