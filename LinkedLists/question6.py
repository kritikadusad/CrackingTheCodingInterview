""" Question 2.6: Implement a function to check if a linked list
is a palindrome. 
Tests:
    >>> ll1 = Node(1, Node(2, Node(2, Node(1))))  # 1->2->2->1
    >>> ll1.isPalindrome()
    True

    >>> ll1 = Node(1, Node(2, Node(3, Node(2, Node(1)))))  # 1->2->3->2->1
    >>> ll1.isPalindrome()
    True

    >>> ll1 = Node(1, Node(2, Node(3)))  # 1->2->3
    >>> ll1.isPalindrome()
    False
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

    def list_length(self):
        """
        >>> ll = Node(1, Node(2, Node(3, Node(4, Node(5)))))
        >>> ll.list_length()
        5
        """
        length = 0
        current = self
        while current:
            length += 1
            current = current.next
        return length

    def isPalindrome(self):
        if not self:
            return True
        stack = []
        length = self.list_length()
        half = length // 2
        odd = False
        if length % 2 != 0:
            odd = True
        current = self
        count = 0
        while current:
            count += 1
            if count <= half:
                stack.append(current.data)
            else:
                if (odd and count != half + 1) or (not odd):
                    if not stack.pop() == current.data:
                        return False
            current = current.next
        return True


if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED!\n")
