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
	
	/* if list is empty */
	if (*head == NULL)
	{
		new_node->next = NULL;
		*head = new_node;
		return (new_node);
	}
	
	/* if list is not empty */
	if (*head)
	{
		/**
		 * if data in first node is greater than data in new node
		 * then in a sorted list, int in new node will be the lowest,
		 * it is added at the beginning of the list
		 */
		if ((*head)->n > new_node->n)
		{
			new_node->next = *head;
			*head = new_node;
			return (new_node);
		}
		/**
		 * if data in first node is lesser than data in new node
		 */
		if ((*head)->n < new_node->n)
		{
			less = *head;
			great = *head;

			while (less->next != NULL)
			{
				/* get node with lower data value than data in new node */
				if (less->n < new_node->n && ((less->next)->n > new_node->n))
					break;

				/* add node which has value equal to a node in the list */
				if (less->n == new_node->n && ((less->next)->n > new_node->n))
				{
					new_node->next = less->next;
					less->next = new_node;
					return (new_node);
				}
				/**
				 * add node at the end; data in new node is greater
				 * than all values in the list
				 */
				else if (less->n < new_node->n && less->next == NULL)
				{
				 	new_node->next = NULL;
					less->next = new_node;
					return (new_node);
				}
				less = less->next;
			}
			
			/* get node with greater data value than data in new node */
			while (great != NULL)
			{
				if (great->n > new_node->n)
					break;
				great = great->next;
			}
	
			/* set node->next pointers and add in between the list */
			less->next = new_node;
			new_node->next = great;
		}
	}

	return (new_node);
}
