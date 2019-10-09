""" Question 2.7: Given two (singly) linked lists, determine if the two
lists intersect. Return the intersecting node. Note that the intersection
is defined based on reference, not value. That is, if the kth node
of the first linked list is the exact same node (by reference) as the jth 
node of the second linked list, then they are intersecting. 

Tests:
    >>> ll1 = Node(1, Node(2, Node(3)))  # 1->2->2
    >>> ll2 = Node(4, Node(5, Node(6)))  # 4->5->6
    >>> intersecting_node(ll1, ll2)
    
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

    def length(self):
        """
        >>> ll = Node(1, Node(2, Node(3, Node(4, Node(5)))))
        >>> ll.length()
        5
        """
        length = 0
        current = self
        while current:
            length += 1
            current = current.next
        return length


def intersecting_node(list1, list2):
    length1 = list1.length()
    length2 = list2.length()
    diff = abs(length1 - length2)
    if length1 >= length2:
        longer = list1
        shorter = list2

    else:
        longer = list2
        shorter = list1
    count = 0
    if diff:
        while longer:
            count += 1
            if count == diff:
                longer = longer.next
                break
            longer = longer.next

    while longer and shorter:
        if longer == shorter:
            return longer
        longer = longer.next
        shorter = shorter.next

    return None


if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED!\n")
