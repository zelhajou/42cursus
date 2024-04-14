#include "array.h"

void deleteElement(int *arr, int index, int size)
{
	if (index > size || index < 0)
		printf("index Error");
	else if (size == index)
		arr[index] = 0;
	else
	{
		while (index <= size - 1)
		{
			if (index + 1 > size - 1)
				arr[index] = 0;
			else
				arr[index] = arr[index + 1];
			index++;
		}	
	}
}
