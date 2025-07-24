def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def input_list():
    arr = []
    n = int(input("Enter the number of elements in the list: "))
    for i in range(n):
        element = int(input("Enter element (in ascending order): "))
        arr.append(element)
    return arr

# Main Program
arr = input_list()
target = int(input("Enter the element to search for: "))
result = binary_search(arr, target)

if result != -1:
    print(target, "found at index", result)
else:
    print(target, "not found in the list.")
