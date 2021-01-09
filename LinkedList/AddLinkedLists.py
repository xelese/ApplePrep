class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        if l1.val is None and l2.val is None:
            return l1

        c = 0

        current = ListNode()
        newval = current

        while l1 is not None or l2 is not None:
            if l1 is None:
                val1 = 0
            else:
                val1 = l1.val
                l1 = l1.next

            if l2 is None:
                val2 = 0
            else:
                val2 = l2.val
                l2 = l2.next

            sum = val1 + val2 + c
            newval.next = ListNode(sum % 10)
            newval = newval.next

            c = sum // 10

        if c > 0:
            lastNode = ListNode(c)
            newval.next = lastNode

        current = current.next

        return current
