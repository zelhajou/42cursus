
# Pointer Pitfalls

## **1. Null Pointer Dereferencing:**

- Dereferencing a null pointer, which doesn't point to any valid memory location, can lead to program crashes or unexpected behavior.
- Example in C:
```c
int *ptr = NULL;
int value = *ptr; // Dereferencing a null pointer (undefined behavior)
```

## **2. Dangling Pointers:**

- Dangling pointers are pointers that point to memory that has been deallocated or freed. Accessing such memory can lead to undefined behavior.
- Example in C:
```c
int *ptr = (int *)malloc(sizeof(int));
free(ptr);       // Deallocate the memory
int value = *ptr; // Accessing a dangling pointer (undefined behavior)
```

## **3. Memory Leaks:**

- Memory leaks occur when dynamically allocated memory is not properly deallocated, leading to a gradual consumption of memory.
- Example in C:
```c
void someFunction() {
    int *ptr = (int *)malloc(sizeof(int));
    // Memory allocated but not freed, causing a memory leak
}
```

## **4. Uninitialized Pointers:**

- Using uninitialized pointers, which don't point to any specific memory location, can lead to unpredictable results or crashes.
- Example in C:
```c
int *ptr;
int value = *ptr; // Using an uninitialized pointer (undefined behavior)
```


## **5. Pointer Arithmetic Errors:**

- Incorrect use of pointer arithmetic can lead to accessing memory locations outside the bounds of an array or invalid memory.

```c
int arr[5] = {1, 2, 3, 4, 5};
int *ptr = &arr[0];
int value = *(ptr + 10); // Accessing memory outside the array bounds (undefined behavior)
```