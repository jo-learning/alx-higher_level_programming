#include "lists.h"
#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>
/**
 * insert_node - singly linked list
 * @head: linked list
 * @number: number that will be added
 *
 * Return: the address of the new node, or NULL if it failed
 * for alx project
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new = malloc(sizeof(listint_t));

	if(!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (!current || new->n < current->n)
	{
		new->next = current;
		return (*head = new);
	}

	while (current)
	{
		if (!current->next || new->n < current->next->n)
		{
			new->next = current->next;
			current->next = new;
			return (current);
		}
		current = current->next;
	}
	return (NULL);
}
