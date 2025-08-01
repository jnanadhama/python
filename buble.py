# Program to sort the elements of a list using Bubble Sort

def bubble_sort(arr):
    n = len(arr)
    
    # Outer loop - number of passes
    # i goes from 0 to n-2 (total n-1 passes)
    for i in range(n - 1):

        # Inner loop - compare adjacent elements
        # j goes from 0 to n - i - 2
        for j in range(0, n - i - 1):

            # Swap if elements are in the wrong order
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def input_list():
    arr = []
    n = int(input("Enter the number of elements in the list: "))
    for i in range(n):
        element = int(input(f"Enter element {i+1}: "))
        arr.append(element)
    return arr

# Main program
arr = input_list()
print("Original list:", arr)

bubble_sort(arr)

print("Sorted list:", arr)
