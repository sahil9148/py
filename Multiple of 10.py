start = int(input("Enter starting range: "))
end = int(input("Enter ending range: "))

for i in range(start, end + 1):
    if i % 10 == 0:
        print(i)
