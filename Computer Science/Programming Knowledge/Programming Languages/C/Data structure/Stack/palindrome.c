#include <stdio.h>
#include <stdlib.h>

struct node
{
	int data;
	struct node *next;
} *top = NULL;

int isEmpty()
{
	if (top == NULL)
		return 1;
	else
		return 0;
}

void push(int data)
{
	struct node *newNode;
	newNode = malloc(sizeof(newNode));
	// Checking if memory cant be allocated for so;e reason
	if (newNode == NULL)
	{
		printf("stack Overflow");
		exit(1);
	}
	newNode->data = data;
	newNode->next = NULL;

	newNode->next = top;
	top = newNode;
}

int pop()
{
	struct node *temp;
	int val;
	if (isEmpty())
	{
		printf("Stack Underflow.");
		exit(1);
	}
	temp = top;
	val = temp->data;
	top = top->next;
	free(top);
	temp = NULL;
	return val;
}

int peek()
{
	if (isEmpty())
	{
		printf("Stack Underflow.");
		exit(1);
	}
	return top->data;
}

void palindrome_check(char *s)
{
	int i = 0;
	while (s[i] != 'X')
	{
		push(s[i]);
		i++;
	}
	i++;
	while (s[i])
	{
		if (isEmpty() || s[i] != pop())
		{
			printf("Not a palindrome");
			exit(1);
		}
		i++;
	}
	if (isEmpty())
		printf("Palindrome");
	else
		printf("Not a Palindrome");
}

int main()
{
	char s[100];
	printf("Please enter the string: ");
	scanf("%s", s);

	palindrome_check(s);
	return 0;
}