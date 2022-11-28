#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if there is a cycle
 * @list: list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *temp;
	listint_t *prev;

	temp = list;
	prev = list;
	while (list && temp && temp->next)
	{
		list = list->next;
		temp = temp->next->next;

		if (list == temp)
		{
			list = prev;
			prev =  temp;
			while (1)
			{
				temp = prev;
				while (temp->next != list && temp->next != prev)
				{
					temp = temp->next;
				}
				if (temp->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
