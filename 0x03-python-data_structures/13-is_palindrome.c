#include <stdlib.h>
#include <stdio.h>
#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of linked list
 * Return: 1 if list is a palindrome, else 0
 */
int is_palindrome(listint_t **head)
{
	int total_nodes, half_total, mid_pos;
	listint_t *temp, *new;

	/* empty list is a palindrome */
	if (*head == NULL)
		return (1);
	temp = *head;

	total_nodes = num_of_nodes(head);
	if (total_nodes % 2 == 0)
		half_total = total_nodes / 2;
	else
		half_total = (total_nodes + 1) / 2;

	/* set temp to middle of linked list; saves first half to head */
	for (mid_pos = 0; mid_pos < half_total; mid_pos++)
		temp = temp->next;
	/* reverse the midpoint set above and set to new list */
	new = reverse_list(&(temp));

	while (new && *head)
	{
		if ((*head)->n != new->n)
			return (0);
		new = new->next;
		*head = (*head)->next;
	}
	return (1);
}
/**
 * num_of_nodes - Gets number of nodes in a singly linked list
 * @head: head node of singly linked list
 * Return: number of nodes
 */
int num_of_nodes(listint_t **head)
{
	listint_t *temp;
	int num;

	temp = *head;

	num = 0;
	while (temp != NULL)
	{
		num++;
		temp = temp->next;
	}
	return (num);
}
/**
 * reverse_list - reverses a singly linked list
 * @head: head node of singly linked list
 * Return: new start node of singly linked list
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *prev, *curr;

	if (*head == NULL)
		return (NULL);

	prev = NULL;
	curr = NULL;
	while (*head != NULL)
	{
		curr = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = curr;
	}
	*head = prev;
	return (prev);
}
