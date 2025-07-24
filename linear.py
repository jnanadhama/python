# Linear Search Function
def linear_search(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            return index  # Return index if found
    return -1  # Return -1 if not found

# Function to input a list from the user
def input_list():
    arr = []
    n = int(input("Enter the number of elements in the list: "))
    for i in range(n):
        element = int(input("Enter element: "))
        arr.append(element)
    return arr

# Main Program
arr = input_list()
target = int(input("Enter the element to search for: "))

result = linear_search(arr, target)

if result != -1:
    print(target, "element found at index", result)
else:
    print(target, "element not found in the list.")
