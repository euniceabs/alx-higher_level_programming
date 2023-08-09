#include "lists.h"

/**
 * check_cycle - Determine whether a linked list contains a
 * cycle or not.
 * @list: Reference to the beginning node of the linked list.
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */


int check_cycle(listint_t *list)
{
listint_t *walker, *runner;
    
if (list == NULL)
return (0);

walker = list;
runner = list->next;

while (walker != NULL && runner != NULL && runner->next != NULL)
{
if (walker == runner)
return (1);
walker = walker->next;
runner = runner->next->next;
}

return (0);
}
