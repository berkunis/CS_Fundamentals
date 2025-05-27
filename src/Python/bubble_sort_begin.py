def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        swapped = False
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # TODO: Compare arr[j] and arr[j + 1]
            # If arr[j] is greater than arr[j + 1], they need to be swapped
            # ---- START CODING HERE ----

            # if arr[j] > arr[j + 1]:
            #     # Swap the elements
            #     arr[j], arr[j + 1] = arr[j + 1], arr[j]
            #     swapped = True
            pass # Remove this 'pass' statement once you add your comparison and swap logic

            # ---- END CODING HERE ----
        
        # If no two elements were swapped by inner loop, then array is sorted
        if not swapped:
            break
    return arr

# Driver code to test above - no changes needed here for the exercise
if __name__ == "__main__":
    sample_array_1 = [64, 34, 25, 12, 22, 11, 90]
    print("Python Example 1 (Begin Version):")
    print("Original array:", sample_array_1)
    bubble_sort(sample_array_1)
    print("Sorted array:", sample_array_1)
    print("-" * 20)

    sample_array_2 = [5, 1, 4, 2, 8, 3, 7, 6]
    print("Python Example 2 (Begin Version):")
    print("Original array:", sample_array_2)
    bubble_sort(sample_array_2)
    print("Sorted array:", sample_array_2)
    print("-" * 20)

    empty_array = []
    print("Python Example (Empty Array - Begin Version):")
    print("Original array:", empty_array)
    bubble_sort(empty_array)
    print("Sorted array:", empty_array)
    print("-" * 20)

    single_element_array = [42]
    print("Python Example (Single Element Array - Begin Version):")
    print("Original array:", single_element_array)
    bubble_sort(single_element_array)
    print("Sorted array:", single_element_array)