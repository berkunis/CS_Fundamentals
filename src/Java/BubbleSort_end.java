import java.util.Arrays;

public class BubbleSort_end { // Class name matches the filename (if you keep it as BubbleSort_end.java)

    void bubbleSort(int arr[]) {
        int n = arr.length;
        boolean swapped;
        for (int i = 0; i < n - 1; i++) {
            swapped = false;
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    // swap arr[j+1] and arr[j]
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true;
                }
            }
            // IF no two elements were swapped by inner loop, then break
            if (!swapped)
                break;
        }
    }

    // Method to print the array
    void printArray(int arr[]) {
        System.out.println(Arrays.toString(arr));
    }

    // Driver method to test above
    public static void main(String args[]) {
        // THIS IS THE LINE THAT NEEDS TO CHANGE:
        BubbleSort_end ob = new BubbleSort_end(); // Create an object of the CURRENT class
        
        int arr1[] = {64, 34, 25, 12, 22, 11, 90};
        System.out.println("Java Example 1:");
        System.out.print("Original array: ");
        ob.printArray(arr1);
        ob.bubbleSort(arr1);
        System.out.print("Sorted array: ");
        ob.printArray(arr1);
        System.out.println("--------------------");

        int arr2[] = {5, 1, 4, 2, 8, 3, 7, 6};
        System.out.println("Java Example 2:");
        System.out.print("Original array: ");
        ob.printArray(arr2);
        ob.bubbleSort(arr2);
        System.out.print("Sorted array: ");
        ob.printArray(arr2);
        System.out.println("--------------------");

        int emptyArr[] = {};
        System.out.println("Java Example (Empty Array):");
        System.out.print("Original array: ");
        ob.printArray(emptyArr);
        ob.bubbleSort(emptyArr);
        System.out.print("Sorted array: ");
        ob.printArray(emptyArr);
        System.out.println("--------------------");

        int singleElementArr[] = {42};
        System.out.println("Java Example (Single Element Array):");
        System.out.print("Original array: ");
        ob.printArray(singleElementArr);
        ob.bubbleSort(singleElementArr);
        System.out.print("Sorted array: ");
        ob.printArray(singleElementArr);
    }
}