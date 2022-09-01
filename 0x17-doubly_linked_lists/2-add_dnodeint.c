#include "lists.h"
/**
 * dlistint_t - adds a node at the beginning of a doubly-linked list
 * @head: double pointer to head of the list
 * @n: variable to be added to the list
 *
 * Return: Address of the new element of NULL
 */
dlistint_t *add_dnodeint(dlistint_t **head, const int n) {
	dlistint_t *temp;

	if (head == NULL) {
		return (NULL);
	}
	temp = malloc(sizeof(dlistint_t));
	if (temp == NULL) {
		return (NULL);
	}
	temp->n = n;
	temp->prev = NULL;
	temp->next = *head;
	*head = temp;
	if (temp->next != NULL) {
		(temp->next)->prev = temp;

	}
	return (temp);
}
