# ---------------- SELECTION SORT ----------------
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


# ---------------- MERGE SORT ----------------
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


# ---------------- SORT 01 (2 POINTER) ----------------
def sort01(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] == 0:
            left += 1
        elif arr[right] == 1:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1


# ---------------- DNF SORT 012 (3 POINTER) ----------------
def sort012(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1


# ---------------- MAIN MENU ----------------
while True:
    print("\n----- MENU -----")
    print("1. Binary Search")
    print("2. Bubble Sort")
    print("3. Selection Sort")
    print("4. Merge Sort")
    print("5. SORT 01 (0s and 1s)")
    print("6. DNF SORT 012 (0s, 1s, 2s)")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 7:
        print("Exiting program.")
        break

    n = int(input("Enter number of elements: "))
    arr = list(map(int, input("Enter elements: ").split()))

    if choice == 1:
        key = int(input("Enter element to search: "))
        result = binary_search(arr, key)
        if result != -1:
            print("Element found at position", result + 1)
        else:
            print("Element not found")

    elif choice == 2:
        bubble_sort(arr)
        print("Sorted array:", arr)

    elif choice == 3:
        selection_sort(arr)
        print("Sorted array:", arr)

    elif choice == 4:
        merge_sort(arr)
        print("Sorted array:", arr)

    elif choice == 5:
        sort01(arr)
        print("Sorted array:", arr)

    elif choice == 6:
        sort012(arr)
        print("Sorted array:", arr)

    else:
        print("Invalid choice!")
