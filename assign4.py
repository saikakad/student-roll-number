def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return True
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return False

def fibonacci_search(arr, key):
    n = len(arr)
    
    # Initialize fibonacci numbers
    fib2 = 0   # (m-2)th Fibonacci
    fib1 = 1   # (m-1)th Fibonacci
    fib = fib1 + fib2  # mth Fibonacci

    # fib stores the smallest Fibonacci number >= n
    while fib < n:
        fib2 = fib1
        fib1 = fib
        fib = fib1 + fib2

    offset = -1

    while fib > 1:
        i = min(offset + fib2, n - 1)
        if arr[i] < key:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
        elif arr[i] > key:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        else:
            return True

    # Check last element
    if fib1 and offset + 1 < n and arr[offset + 1] == key:
        return True
    return False

# Input roll numbers
n = int(input("Enter number of students: "))
roll_numbers = []
for i in range(n):
    roll = int(input(f"Enter roll number of student {i+1}: "))
    roll_numbers.append(roll)

# Ensure sorted order
roll_numbers.sort()
print("\nSorted Roll Numbers:", roll_numbers)

# Search for a roll number
key = int(input("\nEnter roll number to search: "))

# Binary Search
found_binary = binary_search(roll_numbers, key)
print("Binary Search:", "Attended" if found_binary else "Did not attend")

# Fibonacci Search
found_fib = fibonacci_search(roll_numbers, key)
print("Fibonacci Search:", "Attended" if found_fib else "Did not attend")
