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
	listint_t *equal;
	listint_t *negative;

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

	if (*head)
	{
		if (*head->n > new_node->n)
		{
			new_node->next = *head;
			*head = new_node;

			return (new_node);
		}
		
		if (*head->n < new_node->n)
		{
			less = *head;
			great = *head;

			while (less != NULL)
			{
				if (less->n < new_node->n && ((less->next)->n > new_node->n))
					break;
				less = less->next;
			}

			while (great != NULL)
			{
				if (great->n > new_node->n)
					break;
				great = great->next;
			}
	
			equal = *head;

			while (equal->next != NULL)
			{
				if (equal->n == new_node->n && (equal->next)->n > new_node->n)
				{
					new_node->next = equal->next;
					equal = new_node;
					return (new_node);
				}
				equal = equal->next;
			}



			less->next = new_node;
			new_node->next = great;
		}
	}

	return (new_node);
}
