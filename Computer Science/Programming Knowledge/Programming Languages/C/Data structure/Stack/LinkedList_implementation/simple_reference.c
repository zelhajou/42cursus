#include <stdio.h>

void change_val(int **ptr)
{
	int val2 = 46;
	// *ptr = val2;
	**ptr = val2;
}

int main()
{
	int val = 35;
	int *ptr;
	ptr = &val;
	printf("%d\n", *ptr);

	change_val(&ptr);
	printf("%d", *ptr);
	return 0;
}