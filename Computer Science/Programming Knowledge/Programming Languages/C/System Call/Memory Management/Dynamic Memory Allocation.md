- **`malloc` and `free`:** The standard C library provides functions like `malloc` for dynamic memory allocation and `free` for deallocating memory. Memory allocated on the heap persists until explicitly freed.

1. **[malloc] (Memory Allocation):**
	- `malloc` is used to allocate a specified number of bytes of memory on the heap (dynamically allocated memory).
	- It returns a pointer to the first byte of the allocated memory block.
	- If memory allocation fails, it returns a null pointer (`NULL`).

- **Example (Dynamic Memory Allocation):**
```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *ptr;
    ptr = (int *)malloc(5 * sizeof(int)); // Allocate memory for 5 integers
    if (ptr == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }
    // Use the allocated memory
    ptr[0] = 10;
    ptr[1] = 20;

    // Deallocate the memory when done
    free(ptr);
    return 0;
}
```

2. [calloc] **for Initializing Memory:**

- **`calloc`:** The `calloc` function is used to allocate memory for an array of elements and initialize all bytes to zero. It takes two arguments: the number of elements and the size of each element.
```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *ptr;
    int size = 5;

    ptr = (int *)calloc(size, sizeof(int)); // Allocate memory for an array of 5 integers (initialized to 0)

    if (ptr == NULL) {
        printf("Memory allocation failed!\n");
        return 1;
    }

    // Use the allocated memory
    for (int i = 0; i < size; i++) {
        printf("ptr[%d] = %d\n", i, ptr[i]); // All values should be 0
    }

    free(ptr); // Deallocate the allocated memory

    return 0;
}
```

Using `calloc` is advantageous when you need to ensure that the allocated memory is initialized to a known state (zero in this case).

3. [realloc] **for Resizing Memory:**

- **`realloc`:** The `realloc` function is used to resize a previously allocated block of memory. It takes a pointer to the previously allocated memory block and the new size.
```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *ptr;
    int size = 5;

    ptr = (int *)malloc(size * sizeof(int)); // Allocate memory for an array of 5 integers

    if (ptr == NULL) {
        printf("Memory allocation failed!\n");
        return 1;
    }

    // Use the allocated memory
    for (int i = 0; i < size; i++) {
        ptr[i] = i * 2;
        printf("ptr[%d] = %d\n", i, ptr[i]);
    }

    // Reallocate memory for 10 integers
    ptr = (int *)realloc(ptr, 10 * sizeof(int));

    if (ptr == NULL) {
        printf("Memory reallocation failed!\n");
        return 1;
    }

    // Use the reallocated memory
    for (int i = 5; i < 10; i++) {
        ptr[i] = i * 2;
        printf("ptr[%d] = %d\n", i, ptr[i]);
    }

    free(ptr); // Deallocate the allocated memory

    return 0;
}
```

When using `realloc`, it's essential to assign the result back to the original pointer because the memory address may change.


## **Memory Leaks:**

**Leak Detection:** Memory leaks occur when allocated memory is not properly deallocated. Tools like `valgrind` can help detect memory leaks in C programs.