def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        swapped = False
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no two elements were swapped by inner loop, then array is sorted
        if not swapped:
            break
    return arr

# Driver code to test above
if __name__ == "__main__":
    sample_array_1 = [64, 34, 25, 12, 22, 11, 90]
    print("Python Example 1:")
    print("Original array:", sample_array_1)
    bubble_sort(sample_array_1) # Sorts in place
    print("Sorted array:", sample_array_1)
    print("-" * 20)

    sample_array_2 = [5, 1, 4, 2, 8, 3, 7, 6]
    print("Python Example 2:")
    print("Original array:", sample_array_2)
    bubble_sort(sample_array_2) # Sorts in place
    print("Sorted array:", sample_array_2)
    print("-" * 20)

    empty_array = []
    print("Python Example (Empty Array):")
    print("Original array:", empty_array)
    bubble_sort(empty_array)
    print("Sorted array:", empty_array)
    print("-" * 20)

    single_element_array = [42]
    print("Python Example (Single Element Array):")
    print("Original array:", single_element_array)
    bubble_sort(single_element_array)
    print("Sorted array:", single_element_array)