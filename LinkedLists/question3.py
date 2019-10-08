""" Question 2.3: Implement an algorithm to delete a node in the middle
(i.e., any node but the first and last node, not necessarily the exact middle) 
of a singly linked list, given only access to that node.
Test:
    >>> ll = Node("a", Node("b", Node("c", Node("d", Node("e", Node("f"))))))  # a->b->c->d->e->f
    >>> modified_ll = ll.delete_node(ll.return_node("c"))
    >>> modified_ll.as_string()
    'a->b->d->e->f'
    >>> ll = Node(None) # None 
    >>> ll.delete_node(ll.return_node("c"))

    >>> ll = Node(1, Node(2, Node(3, Node(5))))  # 1->2->3->4->5
    >>> ll.delete_node(ll.return_node("6"))

"""


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def as_string(self):
        """
        >>> ll = Node(1, Node(2, Node(3, Node(4, Node(5)))))
        >>> ll.as_string()
        '1->2->3->4->5'
        """

        ll_elements = []
        current = self
        while current:
            ll_elements.append(str(current.data))
            current = current.next

        return "->".join(ll_elements)

    def return_node(self, value):
        """
        Returns node with given value:
        >>> ll = Node(1, Node(2, Node(3, Node(4, Node(5)))))
        >>> ll.return_node(2).data
        2
        """
        current = self
        if not current:
            return None
        while current:
            if current.data == value:
                return current
            current = current.next
        return None

    def delete_node(self, node):
        if not node or not node.next:
            return None
        node.data = node.next.data
        node.next = node.next.next
        return self


if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. EXCELLENT!\n")
