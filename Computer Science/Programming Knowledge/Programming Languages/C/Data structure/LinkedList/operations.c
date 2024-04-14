#include "stack_operations.h"

t_node	*create_node(int data)
{
	t_node	*new_node;

	new_node = (t_node *)malloc(sizeof(t_node));
	if (new_node == NULL)
	{
		ft_putstr_fd("Memory allocation failed", 2);
		exit(1);
	}
	new_node->data = data;
	new_node->next = NULL;
	return (new_node);
}

void	insert_at_beginning(t_node **head, int data)
{
	t_node	*ptr;

	ptr = create_node(data);
	ptr->next = *head;
	*head = ptr;
}

void	insert_at_end(t_node **head, int data)
{
	t_node	*current;
	t_node	*new_node;

	current = *head;
	new_node = create_node(data);
	while (current->next != NULL)
	{
		current = current->next;
	}
	current->next = new_node;
}

void	del_first_node(t_node **head)
{
	t_node	*temp;

	temp = *head;
	if (temp == NULL)
		ft_printf("List is already empty");
	else
	{
		*head = (*head)->next;
		free(temp);
	}
}

void	del_last_node(t_node *head)
{
	t_node	*temp;

	temp = head;
	if (temp == NULL)
		ft_printf("List is already empty!");
	else if (temp->next == NULL)
	{
		free (temp);
		temp = NULL;
	}
	else
	{
		while (temp->next->next != NULL)
		{
			temp = temp->next;
		}
		free (temp->next);
		temp->next = NULL;
	}
}

void	insert_at_position(t_node **head, int data, int pos)
{
	t_node	*ptr;
	t_node	*new_node;

	ptr = *head;
	new_node = create_node(data);
	pos--;
	while (pos != 1)
	{
		ptr = ptr->next;
		pos--;
	}
	new_node->next = ptr->next;
	ptr->next = new_node;
}

void	display_list(t_node *head)
{
	t_node	*temp;

	temp = head;
	if (temp == NULL)
		ft_printf("LinkedList is empty");
	while (temp != NULL)
	{
		ft_printf("%d -> ", temp->data);
		temp = temp->next;
	}
	ft_printf("Null\n");
}

void	count_of_nodes(t_node *head)
{
	int		count;
	t_node	*ptr;

	count = 0;
	ptr = head;
	if (ptr == NULL)
		ft_printf("LinkedList is empty");
	while (ptr != NULL)
	{
		count++;
		ptr = ptr->next;
	}
	ft_printf("%d", count);
}

void	free_list(t_node *head)
{
	t_node	*temp;

	while (head != NULL)
	{
		temp = head;
		head = head->next;
		free (temp);
	}
}
