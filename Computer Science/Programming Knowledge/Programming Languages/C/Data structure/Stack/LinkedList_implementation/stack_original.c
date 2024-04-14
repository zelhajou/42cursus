#include <stdio.h>
#include <stdlib.h>

struct node
{
	int data;
	struct node *link;
};

int isEmpty(struct node *top)
{
	if (top == NULL)
		return 1;
	else
		return 0;
}

void push(int data, struct node **top)
{
	struct node *newNode;
	newNode = malloc(sizeof(newNode));

	if (newNode == NULL)
	{
		printf("Stack Overflow.");
		exit(1);
	}
	newNode->data = data;
	newNode->link = NULL;

	newNode->link = *top;
	*top = newNode;
}

int pop(struct node **top)
{
	struct node *temp;
	int val;
	temp = *top;
	val = temp->data;
	*top = (*top)->link;
	free(temp);
	temp = NULL;
	return val;
}

void print(struct node *top)
{
	struct node *temp;
	temp = top;
	if (isEmpty(top))
	{
		printf("Stack underflow\n");
		return;
	}
	printf("The stack elements are: ");
	while (temp)
	{
		printf("%d ", temp->data);
		temp = temp->link;
	}
	printf("\n");
}

void reverse_stack(struct node **top)
{
	struct node *top1 = NULL;
	struct node *top2 = NULL;

	// Pushing onto temp stack 1
	while (*top != NULL)
	{
		push(pop(top), &top1);
	}
	// Pushing onto temp stack 2
	while (top1 != NULL)
	{
		push(pop(&top1), &top2);
	}
	// Pushing onto original stack
	while (top2 != NULL)
	{
		push(pop(&top2), top);
	}
}
int main()
{
	int data;
	struct node *top = NULL;
	int choice;

	while (1)
	{
		printf("1. Push\n");
		printf("2. Print\n");
		printf("3. Reverse the stack\n");
		printf("4. quit\n");
		printf("Enter your choice:\n");
		scanf("%d", &choice);
		switch (choice)
		{
		case 1:
			printf("Enter the element to be pushed: ");
			scanf("%d", &data);
			push(data, &top);
			break;
		case 2:
			print(top);
			break;
		case 3:
			reverse_stack(&top);
			printf("Stack is reversed.\n");
			break;
		case 4:
			exit(1);
		default:
			printf("wrong choice");
			break;
		}
	}

	reverse_stack(&top);
	print(top);

	return 0;
}