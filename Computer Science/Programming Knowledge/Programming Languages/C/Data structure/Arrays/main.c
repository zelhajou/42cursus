#include "array.h"

int main()
{
	int arr[] = {1, 2, 3, 4, 10};
	size_t size = sizeof(arr) / sizeof(arr[0]);

	// Accessing elements
	int element = getElement(arr, 0);
	printf("First Element %d\n", element);

    // update an element
	updateElement(arr, 4, 10);

	// Deletion at a specific index
	// In C, you typically can't directly remove an element from an array.
    // You can overwrite it or use a loop to shift elements if needed.
	deleteElement(arr, 3, size);

	// Traversing the array
	printArray(arr, size);

	return (0);
}