#include "stack_array.h"

/*
	Description : C program to find and display the prime factors of a number
	in descending order.
*/

void prime_fact(int num)
{
	int i = 2;
	while (num != 1)
	{
		while (num % i == 0)
		{
			push(i);
			num = num / i;
		}
		i++;
	}
	while (top != -1)
	{
		printf("%d ", pop());
	}
}

int main()
{
	int num;

	printf("Please enter a postivie number: ");
	scanf("%d", &num);
	prime_fact(num);
}