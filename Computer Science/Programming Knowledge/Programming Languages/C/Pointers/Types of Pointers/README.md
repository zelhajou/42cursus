
# Type of Pointers

**a. Null Pointers:**

Null pointers are pointers that do not point to any valid memory location. They are often used to represent the absence of a value or an uninitialized pointer.
- Example in C:
	```c
	int *ptr = NULL; // ptr is a null pointer
	```

**b. Void Pointers:**

Void pointers, also known as generic pointers, are pointers that do not have a specific data type associated with them. They are often used for functions that can work with different data types.
- Example in C:
	```c
	void *genericPtr;
	int num = 10;
	float pi = 3.14;
	genericPtr = &num; // Assigning an int pointer to a void pointer
	genericPtr = &pi;  // Assigning a float pointer to a void pointer
	```

**c. Function Pointers:**

Function pointers are pointers that point to functions instead of data. They are used for implementing callbacks, dynamic function dispatch, and creating extensible code.
- Example in C:
	```c
	int add(int a, int b) {
		return a + b;
	}

	int (*functionPtr)(int, int); // Function pointer declaration
	functionPtr = add;             // Pointing to the "add" function
	int result = functionPtr(5, 3); // Calling the function using the pointer
	```

**d. Array Pointers:**

Array pointers are pointers that point to the first element of an array. They are often used to manipulate arrays and iterate through their elements.
- Example in C:
	```c
	int arr[5] = {1, 2, 3, 4, 5};
	int *ptr = arr; // Pointer to the first element of the array
	// Accessing array elements using pointer arithmetic
	printf("%d\n", *ptr);   // Output: 1
	printf("%d\n", *(ptr+2)); // Output: 3
	```

**e. Pointer to Pointer (Double Pointer):**

Pointer to pointer, also known as a double pointer, is a pointer that points to another pointer. They are commonly used in dynamic memory allocation and multi-dimensional arrays.
- Example in C:
	```c
	int num = 42;
	int *ptr1 = &num;
	int **ptr2 = &ptr1; // Pointer to pointer
	printf("%d\n", **ptr2); // Output: 42
	```