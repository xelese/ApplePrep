class Node:
    val = None
    next = None

    def __init__(self, val=None):
        self.val = val


def mergeSortedLists(l1, l2):
    if l1 is None and l2 is None:
        return Node()

    current = Node()
    temp = current

    while l1 is not None or l2 is not None:
        if l1 is not None and l2 is not None:
            if l1.val < l2.val:
                temp.next = Node(l1.val)
                l1 = l1.next
            else:
                temp.next = Node(l2.val)
                l2 = l2.next
        else:
            if l1 is None:
                temp.next = Node(l2.val)
                l2 = l2.next

            else:
                temp.next = Node(l1.val)
                l1 = l1.next

        temp = temp.next

    return current.next


def createLinkedList(a, b, c, d):
    head = Node(a)
    temp = head

    for i in range(b, c, d):
        temp.next = Node(i)
        temp = temp.next

    return head


def printResult(l1, l2):
    result = mergeSortedLists(l1, l2)
    temp = result
    print("\n")
    print("*" * 5)
    while temp is not None:
        print(temp.val, end="->")
        temp = temp.next
    return


if __name__ == "__main__":
    l1 = createLinkedList(0, 1, 5, 1)
    l2 = createLinkedList(1, 2, 9, 1)
    printResult(l1, l2)

    l1 = None
    l2 = createLinkedList(1, 2, 9, 1)
    printResult(l1, l2)

    l1 = None
    l2 = None
    printResult(l1, l2)

    l1 = None
    l2 = Node(0)
    printResult(l1, l2)
