#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer to the head of the linked list.
 * @number: The number to insert.
 *
 * Return: A pointer to the new node if successful, or NULL on failure.
 */

listint_t *insert_node(listint_t **head, int number)
{
listint_t *new_node, **current;

new_node = malloc(sizeof(listint_t));
if (new_node == NULL)
return (NULL);

new_node->n = number;

current = head;
while (*current && (*current)->n < number)
current = &(*current)->next;

new_node->next = *current;
*current = new_node;

return (new_node);
}
