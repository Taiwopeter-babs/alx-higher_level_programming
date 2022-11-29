#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks for occurence of cycle in linked list
 * @list: pointer to head of singly linked list
 * Return: 0 if no cycle, otherwise 1
 */
int check_cycle(listint_t *list)
{
	listint_t *once;
	listint_t *twice;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}
	once = list;
	twice = list;

	while (once != NULL && twice != NULL)
	{
		once = once->next;
		twice = (twice->next)->next;

		if (twice == once)
			return (1);
	}

	return (0);
}
