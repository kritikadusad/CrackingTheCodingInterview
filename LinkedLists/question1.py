""" Question 2.1: Write code to remove duplicates from an unsorted linked list.
Test:
    >>> ll = Node(1, Node(2, Node(3, Node(5, Node(5)))))  # 1->2->3->5->5
    >>> remove_duplicates(ll)
    >>> ll.as_string()
    '1->2->3->5'
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


def remove_duplicates(ll):
    current = ll
    previous = ll
    new_linked_list = set()
    while current:
        if current.data not in new_linked_list:
            new_linked_list.add(current.data)
            previous = current
        else:
            previous.next = current.next
        current = current.next


if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. EXCELLENT!\n")
