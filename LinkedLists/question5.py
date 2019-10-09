""" Question 2.5: You have two numbers represented by a linked list, where
each node contains a single digit. The digits are stored in reverse order, 
such that the 1s digit is at the head of the list. Write a function that 
adds the two numbers and returns the sum as a linked list. 
Tests:
    >>> ll1 = Node(7, Node(1, Node(6)))  # 7->1->6
    >>> ll2 = Node(5, Node(9, Node(2, Node(1))))  # 5->9->2->1
    >>> sum_lists(ll1, ll2).as_string()
    '2->1->9->1'

    >>> ll1 = None # None
    >>> ll2 = Node(5, Node(9, Node(2, Node(1))))  # 5->9->2->1
    >>> sum_lists(ll1, ll2).as_string()
    '5->9->2->1'

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

def sum_lists(list1, list2):
    sum_list = Node(None)
    head = sum_list
    carryover = 0
    while list1 and list2:
        sum_val = list1.data + list2.data + carryover
        if sum_val > 9:
            carryover, add_val = divmod(sum_val, 10)
            sum_list.next = Node(add_val)
        else:
            sum_list.next = Node(sum_val)
            carryover = 0
        list1 = list1.next
        list2 = list2.next
        sum_list = sum_list.next
    
    if list1:
        sum_list.next = list1
    if list2:
        sum_list.next = list2

    return head.next 

if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED!\n")
