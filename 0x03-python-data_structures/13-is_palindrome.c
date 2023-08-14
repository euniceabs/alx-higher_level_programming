#include "lists.h"

/**
 * reverse_linked_list - reverses the order of nodes
 * in a linked list.
 * @head: the pointer to the first node in the list
 *
 * Returns: a pointer to the first node of
 * the reversed list.
 */
void reverse_linked_list(listint_t **head)
{
listint_t *current = *head;
listint_t *next_node = NULL;
listint_t *last = NULL;
while (current != NULL)
{
next_node = current->next;
current->next = last;
last = current;
current = next_node;
}

*head = last;
}

/**
 * is_palindrome - determines if a linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
listint_t *slow_ptr = *head, *fast_ptr = *head,
*temp_ptr = *head, *second_half = NULL;
if (!*head || !(*head)->next)
return (1);
while (1)
{
fast_ptr = fast_ptr->next->next;
if (!fast_ptr)
{
second_half = slow_ptr->next;
break;
}
if (!fast_ptr->next)
{
second_half = slow_ptr->next->next;
break;
}
slow_ptr = slow_ptr->next;
}
reverse_linked_list(&second_half);
while (second_half != NULL && temp_ptr != NULL)
{
if (temp_ptr->n == second_half->n)
{
second_half = second_half->next;
temp_ptr = temp_ptr->next;
}
else
{
return (0);
}
}
if (second_half == NULL)
return (1);
return (0);
}

