""" Question 2.4: Write code to partition a linked list around a value x,
such that all nodes less than x come before all nodes greater than or
equal to x. If x is contained within the list, the values of x only need
to be after the elements less than x(see test). The partition element x
can appear anywhere in the "right partition"; it does not need to appear between
the left and right partitions. 
Test:
    >>> ll = Node(3, Node(5, Node(8, Node(5, Node(10, Node(2, Node(1)))))))  # 3->5->8->5->10->2->1
    >>> ll.partition(5).as_string()
    '3->2->1->5->8->5->10'

    >>> ll = Node(None) # None 
    >>> ll.partition(5)

    >>> ll = Node(3, Node(5, Node(8, Node(5, Node(10, Node(2, Node(1)))))))  # 3->5->8->5->10->2->1
    >>> ll.partition(6).as_string()
    '3->5->5->2->1->8->10'
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

    def partition(self, value):
        left = Node(None)
        left_dummy = left
        right = Node(None)
        right_dummy = right
        current = self
        if current.data is None:
            return None
        while current:
            if current.data < value:
                left.next = current
                left = left.next
            else:
                right.next = current
                right = right.next
            current = current.next
        right.next = None
        left.next = right_dummy.next
        return left_dummy.next


if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. EXCELLENT!\n")
