#ifndef ARRAY_H
#define ARRAY_H

#include <stdio.h>
#include <unistd.h>
#include <stdbool.h>
#include <stdlib.h>

#define ARRAY_LENGTH(arr) (sizeof(arr) / sizeof(arr[0]))


// Deletion at a specific index
void deleteElement(int *arr, int index, int size);
// Traversing the array
void printArray(int arr[], int length);
// Update an element
void updateElement(int arr[], int index, int newValue);
// Access Elements:
int getElement(int arr[], int index);

#endif