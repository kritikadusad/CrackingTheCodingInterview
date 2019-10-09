""" Question 2.8: 
Given a circular linked list, implement an algorithm that returns the node 
at the beginning of the loop.
Tests:
    >>> ll1 = Node(1, Node(2, Node(3)))  # 1->2->2
    >>> ll1.has_cycle()

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
        if current is None:
            return None
        while current:
            ll_elements.append(str(current.data))
            current = current.next

        return "->".join(ll_elements)


    def has_cycle(self):
        if not self:
            return None
        nodes = set()
        current = self
        while current:
            if current not in nodes:
                nodes.add(current)
            else:
                return current
            current = current.next
        return None


if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED!\n")
