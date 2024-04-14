#include "stack_array.h"

int stack_arr[MAX];
int top = -1;

int isFull()
{
	if (top == MAX - 1)
		return 1;
	return 0;
}

int isEmpty()
{
	if (top == -1)
		return 1;
	return 0;
}

int peek()
{
	if (isEmpty())
	{
		printf("Stack underflow\n");
		exit(1);
	}
	return stack_arr[top];
}

void push(int data)
{
	if (isFull())
	{
		printf("Stack overflow\n");
		return;
	}
	top = top + 1;
	stack_arr[top] = data;
}

int pop(void)
{
	int value;
	if (isEmpty())
	{
		printf("Stack underflow");
		exit(1);
	}
	value = stack_arr[top];
	top = top - 1;
	return value;
}

void print(void)
{
	int i;
	if (isEmpty())
	{
		printf("Stack underflow");
		return;
	}
	for (i = top; i >= 0; i--)
		printf("%d ", stack_arr[i]);
}
