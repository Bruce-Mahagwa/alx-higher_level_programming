#include "lists.h"
/**
 * free_dlistint - frees a doubly linked list
 * @head pointer to first element of a linked list
 *
 * Return: void
 */
void free_dlistint(dlistint_t *head) {
	dlistint_t *new;

	while (head != NULL) {
		new = head->next;
		free(head);
		head = new;
	}
}
