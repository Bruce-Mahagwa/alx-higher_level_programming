#include "lists.h"
/**
 * get_dnodeint_at_index - gets a node at given index
 * @head: pointer to head of a linked list
 * @index: index to look for the node
 *
 * Return: The node
 */
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index) {
	unsigned int j;

	if (head == NULL) {
		return (NULL);
	}
	if (index == 0) {
		return (head);
	}
	for (j = 0; j < index; j++) {
		if (head->next == NULL)
		{
			return (NULL);
		}
		head = head->next;
	}
	return (head);
}
