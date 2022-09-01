#include "lists.h"
/**
 * dlistint_t - adds a node at the end of the list
 * @head: pointer to first element of a list
 * @n: element to be added
 *
 * Return: Address of the new element of NULL
 */
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n) {
	dlistint_t *new, *temp;

	if (head == NULL) {
		return (NULL);
	}
	new = malloc(sizeof(dlistint_t));
	if (new == NULL) {
		return (NULL);
	}
	new->n = n;
	new->next = NULL;
	if (*head == NULL) {
		new->prev = NULL;
		*head = new;
		return (new);
	}
	temp = *head;
	while (temp->next != NULL) {
		temp = temp->next;
	}
	temp->next = new;
	new->prev = temp;
	return (new);
}
