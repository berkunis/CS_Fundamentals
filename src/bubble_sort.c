#include <stdio.h>
#include <stdbool.h> // For bool type

// Function to swap two elements
void swap(int *xp, int *yp) {
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}

// Function to implement bubble sort
void bubbleSort(int arr[], int n) {
    int i, j;
    bool swapped;
    for (i = 0; i < n - 1; i++) {
        swapped = false;
        for (j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(&arr[j], &arr[j + 1]);
                swapped = true;
            }
        }
        // IF no two elements were swapped by inner loop, then break
        if (swapped == false)
            break;
    }
}

// Function to print an array
void printArray(int arr[], int size) {
    int i;
    for (i = 0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

// Driver program to test above functions
int main() {
    int arr1[] = {64, 34, 25, 12, 22, 11, 90};
    int n1 = sizeof(arr1) / sizeof(arr1[0]);
    printf("C Example 1:\n");
    printf("Original array: ");
    printArray(arr1, n1);
    bubbleSort(arr1, n1);
    printf("Sorted array: ");
    printArray(arr1, n1);
    printf("--------------------\n");

    int arr2[] = {5, 1, 4, 2, 8, 3, 7, 6};
    int n2 = sizeof(arr2) / sizeof(arr2[0]);
    printf("C Example 2:\n");
    printf("Original array: ");
    printArray(arr2, n2);
    bubbleSort(arr2, n2);
    printf("Sorted array: ");
    printArray(arr2, n2);
    printf("--------------------\n");
    
    int empty_arr[] = {};
    int n_empty = 0; // Or sizeof(empty_arr)/sizeof(int) if compiler allows zero-sized array
    printf("C Example (Empty Array):\n");
    printf("Original array: ");
    printArray(empty_arr, n_empty);
    bubbleSort(empty_arr, n_empty);
    printf("Sorted array: ");
    printArray(empty_arr, n_empty);
    printf("--------------------\n");

    int single_arr[] = {42};
    int n_single = sizeof(single_arr)/sizeof(single_arr[0]);
    printf("C Example (Single Element Array):\n");
    printf("Original array: ");
    printArray(single_arr, n_single);
    bubbleSort(single_arr, n_single);
    printf("Sorted array: ");
    printArray(single_arr, n_single);

    return 0;
}