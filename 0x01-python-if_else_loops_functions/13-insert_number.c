#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts node at a position in sorted linked list
 * @head: pointer to head of linked list
 * @number: data of new node to insert
 * Return: new node on success, otherwise NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *less;
	listint_t *great;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		free(new_node);
		return (NULL);
	}
	new_node->n = number;

	if (*head == NULL)
	{
		new_node->next = NULL;
		*head = new_node;
		return (new_node);
	}

	less = *head;
	great = *head;

	while (less->next != NULL)
	{
		if (less->n < new_node->n && ((less->next)->n > new_node->n))
			break;
		less = less->next;
	}

	while (great->next != NULL)
	{
		if (great->n > new_node->n)
			break;
		great = great->next;
	}

	less->next = new_node;
	new_node->next = great;

	return (new_node);
}
