"""The LinkedList code from before is provided below.
The three functions added to the LinkedList are:
"append" - adds an element to the end of the list
"get_position" - returns the element at a certain position.
"insert" - add an element to a particularspot in the list.
"delete" - delete the first element with that particular value."""

class Node():
    """Model a node of a linked list"""

    def __init__(self, value, next=None):
        """Initialize attributes of a node object"""

        self.value = value
        self.next = next

class LinkedList():
    """Model of a linked list"""

    def __init__(self, head=None):
        """Initialize atttributes of the linked list"""

        self.head = head

    def append(self, new_node):
        """Function to add a node at the end of the linked list"""

        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node
