n = int(input("Enter number of elements: "))

numbers = []

for i in range(n):
    numbers.append(int(input("Enter number: ")))

largest = numbers[0]
second_largest = numbers[0]

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num < largest and num > second_largest:
        second_largest = num

print("Second Largest Element:", second_largest)
