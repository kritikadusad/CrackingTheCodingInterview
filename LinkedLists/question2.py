""" Question 2.2: Implement an algorithm to find the kth 
to last element of a singly linked list.
Test:
    >>> ll = Node(1, Node(2, Node(3, Node(5, Node(5)))))  # 1->2->3->4->5
    >>> kth_to_last(ll, 1).data
    5
    >>> ll = Node(None)# None 
    >>> kth_to_last(ll, 5)

    >>> ll = Node(1, Node(2, Node(3, Node(5, Node(5)))))  # 1->2->3->4->5
    >>> kth_to_last(ll, 6)

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


def kth_to_last(ll, k):
    if ll is None:
        return ll
    current = ll
    runner = ll
    count = 0
    for i in range(k):
        if not runner:
            return None
        runner = runner.next

    while runner:
        runner = runner.next
        current = current.next

    return current


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. EXCELLENT!\n")
