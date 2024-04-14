#include <stdio.h>
#include <stdlib.h>

struct node
{
	int data;
	struct node *link;
};

// Function to create a new node with the given data
struct node *createNode(int data)
{
	struct node *newNode = (struct node *)malloc(sizeof(struct node));
	if (newNode == NULL)
	{
		perror("Memory allocation failed");
		exit(1);
	}
	newNode->data = data;
	newNode->link = NULL;
	return newNode;
}

void count_of_nodes(struct node *head)
{
	int count = 0;
	if (head == NULL)
		printf("Linked List is empty");
	struct node *ptr = NULL;
	ptr = head;
	while (ptr != NULL)
	{
		count++;
		ptr = ptr->link;
	}
	printf("%d", count);
}

// Function to display the elements of the list
void displayList(struct node *head)
{
	if (head == NULL)
		printf("LinkedList is empty");
	struct node *temp = NULL;
	temp = head;
	while (temp != NULL)
	{
		printf("%d -> ", temp->data);
		temp = temp->link;
	}
	printf("NULL\n");
}

void insertAtEnd(struct node **head, int data)
{

	struct node *current, *newNode;
	current = *head;
	newNode = createNode(data);

	while (current->link != NULL)
	{
		current = current->link;
	}
	current->link = newNode;
}

// struct node *add_at_end2(struct node *ptr, int data)
// {
// 	struct node *temp = malloc(sizeof(struct node));
// 	temp->data = data;
// 	temp->link = NULL;

// 	ptr->link = temp;
// 	return temp;
// }

/*

// Function to insert a new node at the beginning of the list
void insertAtBeginning(struct Node** head, int data) {
	struct Node* newNode = createNode(data);
	newNode->next = *head;
	*head = newNode;
}

*/

// Function to insert a new node at the end of the list
void insertAtBeginning(struct node **head, int d)
{
	struct node *ptr = malloc(sizeof(struct node));
	ptr->data = d;
	ptr->link = NULL;

	ptr->link = *head;
	*head = ptr;
}

// struct node *insertAtBeginning(struct node *head, int d)
// {
// 	struct node *ptr = malloc(sizeof(struct node));
// 	ptr->data = d;
// 	ptr->link = NULL;

// 	ptr->link = head;
// 	return ptr;
// }

void add_at_pos(struct node **head, int data, int pos)
{
	struct node *ptr = *head;
	struct node *ptr2 = malloc(sizeof(struct node));
	ptr2->data = data;
	ptr2->link = NULL;

	pos--;
	while (pos != 1)
	{
		ptr = ptr->link;
		pos--;
	}

	ptr2->link = ptr->link;
	ptr->link = ptr2;
}

void del_first(struct node **head)
{
	if (*head == NULL)
		printf("List is already empty");
	else
	{
		struct node *tmp = *head;
		*head = (*head)->link;
		free(tmp);
	}
}

void del_last(struct node *head)
{
	if (head == NULL)
		printf("List is already empty!");
	else if (head->link == NULL)
	{
		free(head);
		head = NULL;
	}
	else
	{
		struct node *temp = head;
		struct node *temp2 = head;
		while (temp->link != NULL)
		{
			temp2 = temp;
			temp = temp->link;
		}
		temp2->link = NULL;
		free(temp);
		temp = NULL;
	}
}

void del_last2(struct node *head)
{
	if (head == NULL)
		printf("List is already empty!");
	else if (head->link == NULL)
	{
		free(head);
		head = NULL;
	}
	else
	{
		struct node *temp = head;
		while (temp->link->link != NULL)
		{
			temp = temp->link;
		}
		free(temp->link);
		temp->link = NULL;
	}
}

struct node *del_list(struct node *head)
{
	struct node *temp = head;

	while (temp != NULL)
	{
		temp = temp->link;
		free(head);
		head = temp;
	}
	return head;
}

// Function to free memory occupied by the list
void freeList(struct node *head)
{
	while (head != NULL)
	{
		struct node *temp = head;
		head = head->link;
		free(temp);
	}
}

void del_pos(struct node **head, int position)
{
	struct node *current = *head;
	struct node *previous = *head;
	if (*head == NULL)
		printf("List is already empty!");
	else if (position == 1)
	{
		*head = current->link;
		free(current);
		current = NULL;
	}
	else
	{
		while (position != 1)
		{
			previous = current;
			current = current->link;
			position--;
		}
		previous->link = current->link;
		free(current);
		current = NULL;
	}
}

int main()
{
	struct node *head = malloc(sizeof(struct node));
	head->data = 45;
	head->link = NULL;

	insertAtEnd(&head, 20);
	insertAtEnd(&head, 30);
	displayList(head);
	add_at_pos(&head, 67, 3);
	struct node *ptr = head;
	displayList(head);
	del_first(&head);
	del_last(head);
	displayList(head);
	del_pos(&head, 1);
	displayList(head);
}

// int main()
// {
// 	struct node *head = NULL;
// 	head = (struct node *)malloc(sizeof(struct node));
// 	head->data = 45;
// 	head->link = NULL;

// 	count_of_nodes(head);

// 	print_data(head);
// }