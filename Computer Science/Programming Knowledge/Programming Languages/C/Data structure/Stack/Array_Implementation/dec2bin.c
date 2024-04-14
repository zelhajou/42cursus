#include "stack_array.h"

void dec2bin(int n)
{
	while (n != 0)
	{
		push(n % 2);
		n = n / 2;
	}
}

void print2()
{
	if (isEmpty())
	{
		printf("Stack Underflow.");
		exit(1);
	}
	while (!isEmpty())
	{
		printf("%d", pop());
	}
}

int main()
{
	int dec;
	printf("Ebter the decinal number: ");
	scanf("%d", &dec);
	dec2bin(dec);
	print2();

	return 0;
}