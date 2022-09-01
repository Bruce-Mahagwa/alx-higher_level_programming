#include "lists.h"
/**
 * dlistint_len - finds number of elements in a linked list
 * @h: pointer to the head of a linked list
 *
 * Return: number of elements
 */
size_t dlistint_len(const dlistint_t *h) {
	size_t j;

	for (j= 0; h != NULL; j++) {
		h = h -> next;
	}
	return (j);
}
