# Common Pointer Usages


## **1. Dynamic Memory Allocation:**

- Pointers are often used to manage dynamic memory allocation, allowing you to create and manipulate data structures of variable size at runtime.
- Example in C:
```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int n = 5;
    int *dynamicArr = (int *)malloc(n * sizeof(int)); // Allocate memory for an integer array

    if (dynamicArr == NULL) {
        printf("Memory allocation failed.\n");
        return 1;
    }

    for (int i = 0; i < n; i++) {
        dynamicArr[i] = i * 2; // Initialize the array
    }

    for (int i = 0; i < n; i++) {
        printf("%d ", dynamicArr[i]); // Print array elements
    }

    free(dynamicArr); // Deallocate the allocated memory
    return 0;
}
```

## **2. Passing by Reference:**

- Pointers can be used to pass variables by reference to functions, allowing functions to modify the original values.
- Example in C:
```c
#include <stdio.h>

void modifyValue(int *x) {
    *x = *x * 2; // Modify the value pointed to by x
}

int main() {
    int num = 5;
    modifyValue(&num); // Pass num by reference
    printf("Modified value: %d\n", num); // Output: Modified value: 10
    return 0;
}
```

![[Screen Shot 2023-10-11 at 2.14.31 PM.png]]

## **3. Array Manipulation:**

- Pointers can be used to iterate through arrays efficiently.
- Examples in C:
```c
#include <stdio.h>

int main() {
    int arr[5] = {1, 2, 3, 4, 5};
    int *ptr = arr; // Pointer to the first element of the array

    for (int i = 0; i < 5; i++) {
        printf("%d ", *ptr); // Print array element using pointer
        ptr++; // Move the pointer to the next element
    }

    return 0;
}
```

## **4. Data Structures (Linked Lists):**

- Pointers are essential in implementing data structures like linked lists.
```c
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *next;
};

int main() {
    struct Node *head = NULL;
    head = (struct Node *)malloc(sizeof(struct Node));
    head->data = 1;
    head->next = NULL;

    // Perform linked list operations...

    free(head); // Deallocate memory when done
    return 0;
}
```

## **5. Callback Functions:**

- Function pointers are used for implementing callback functions, where a function is passed as an argument to another function.
```c
#include <stdio.h>

int add(int a, int b) {
    return a + b;
}

int subtract(int a, int b) {
    return a - b;
}

int operate(int (*operation)(int, int), int x, int y) {
    return operation(x, y);
}

int main() {
    int result1 = operate(add, 5, 3);      // 5 + 3 = 8
    int result2 = operate(subtract, 10, 4); // 10 - 4 = 6

    printf("Result 1: %d\n", result1);
    printf("Result 2: %d\n", result2);
    return 0;
}
```

## **6. Pointers to Functions:**

- Pointers can be used to create arrays of function pointers, which can be helpful for dynamic function dispatch.
```c
#include <stdio.h>

int add(int a, int b) {
    return a + b;
}

int subtract(int a, int b) {
    return a - b;
}

int main() {
    int (*operation[2])(int, int); // Array of function pointers
    operation[0] = add;
    operation[1] = subtract;

    int result1 = operation[0](5, 3);      // 5 + 3 = 8
    int result2 = operation[1](10, 4);     // 10 - 4 = 6

    printf("Result 1: %d\n", result1);
    printf("Result 2: %d\n", result2);
    return 0;
}
```

## **7. File Handling (File Pointers):**

- Pointers are used for file handling in C, where file pointers are used to read from and write to files.
```c
#include <stdio.h>

int main() {
    FILE *filePtr;
    filePtr = fopen("example.txt", "w"); // Open a file for writing

    if (filePtr == NULL) {
        printf("Failed to open the file.\n");
        return 1;
    }

    fprintf(filePtr, "Hello, World!\n"); // Write to the file
    fclose(filePtr); // Close the file

    return 0;
}
```

## **8. Pointer to Structures:**

- Pointers are often used with structures to manage and manipulate structured data efficiently.

```c
#include <stdio.h>

struct Point {
    int x;
    int y;
};

int main() {
    struct Point p1 = {2, 3};
    struct Point *ptr = &p1; // Pointer to a structure

    printf("Coordinates: (%d, %d)\n", ptr->x, ptr->y); // Access structure members using pointer

    return 0;
}
```

## **9. Pointer Arithmetic Errors:**

- While pointer arithmetic is powerful, it can lead to errors like accessing out-of-bounds memory.
```c
#include <stdio.h>

int main() {
    int arr[5] = {1, 2, 3, 4, 5};
    int *ptr = arr; // Pointer to the first element of the array

    for (int i = 0; i < 7; i++) {
        printf("%d ", *ptr); // Accessing beyond the array boundary
        ptr++; // Moving the pointer
    }

    return 0;
}
```

## **10. String Manipulation:**

- Pointers are widely used for string manipulation in C, as strings are represented as character arrays.
```c
#include <stdio.h>

int main() {
    char str[] = "Hello, World!";
    char *ptr = str; // Pointer to the first character of the string

    while (*ptr != '\0') {
        putchar(*ptr); // Print characters using pointer
        ptr++;
    }

    return 0;
}
```