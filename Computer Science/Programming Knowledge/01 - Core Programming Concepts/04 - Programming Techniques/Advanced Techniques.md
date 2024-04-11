
# 1. **Recursion** : 

**Recursion**: Recursion is a technique where a function calls itself to solve a problem. It's particularly useful for solving problems that can be divided into smaller, similar sub-problems. Recursion often involves defining a base case (the stopping condition) and a recursive case (where the function calls itself with modified arguments).
```c
#include <stdio.h>

// Function to calculate the factorial of a number using recursion
unsigned long long factorial(int n) {
    // Base case: if n is 0 or 1, the factorial is 1
    if (n == 0 || n == 1) {
        return 1;
    }
    // Recursive case: multiply n by the factorial of (n-1)
    else {
        return n * factorial(n - 1);
    }
}

int main() {
    int num;
    printf("Enter a non-negative integer: ");
    scanf("%d", &num);

    if (num < 0) {
        printf("Factorial is not defined for negative numbers.\n");
    } else {
        unsigned long long result = factorial(num);
        printf("Factorial of %d = %llu\n", num, result);
    }

    return 0;
}
```


# 2. **Divide and Conquer**: 
Divide and conquer is a problem-solving technique that involves breaking down a complex problem into smaller, more manageable sub-problems, solving them independently, and then combining their solutions to solve the original problem. This technique is commonly used in algorithms like merge sort and quicksort.

```c
#include <stdio.h>

// Function to merge two sorted subarrays into a single sorted array
void merge(int arr[], int left[], int leftSize, int right[], int rightSize) {
    int i = 0, j = 0, k = 0;

    while (i < leftSize && j < rightSize) {
        if (left[i] <= right[j]) {
            arr[k++] = left[i++];
        } else {
            arr[k++] = right[j++];
        }
    }

    while (i < leftSize) {
        arr[k++] = left[i++];
    }

    while (j < rightSize) {
        arr[k++] = right[j++];
    }
}

// Function to perform Merge Sort
void mergeSort(int arr[], int size) {
    if (size <= 1) {
        return;  // Base case: Array of size 1 or less is already sorted
    }

    // Calculate the middle index of the array
    int mid = size / 2;

    // Divide the array into two halves
    int left[mid];
    int right[size - mid];

    for (int i = 0; i < mid; i++) {
        left[i] = arr[i];
    }
    for (int i = mid; i < size; i++) {
        right[i - mid] = arr[i];
    }

    // Recursively sort the two halves
    mergeSort(left, mid);
    mergeSort(right, size - mid);

    // Merge the sorted halves back into the original array
    merge(arr, left, mid, right, size - mid);
}

int main() {
    int arr[] = {12, 11, 13, 5, 6, 7};
    int size = sizeof(arr) / sizeof(arr[0]);

    printf("Original array: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }

    // Call Merge Sort to sort the array
    mergeSort(arr, size);

    printf("\nSorted array: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }

    return 0;
}
```




```
|-- Advanced Techniques
|   |-- Recursion
|   |-- Divide and Conquer
|   |-- Dynamic Programming
|   |-- Backtracking
|   |-- Greedy Algorithms
|   |-- Graph Algorithms
|   |-- Searching Algorithms
|   |-- Sorting Algorithms
```
