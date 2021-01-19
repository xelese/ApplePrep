class LinkedList:
    val = None
    minVal = None
    next = None

    def __init__(self, val):
        self.val = val
        return


class MinStack:
    def __init__(self):
        self.head = None

    def push(self, val):
        if self.head is None:
            self.head = LinkedList(val)
            self.head.next = None
            self.head.minVal = val
        else:
            node = LinkedList(val)
            node.minVal = min(val, self.head.minVal)
            node.next = self.head
            self.head = node
        return

    def pop(self):
        if self.head is not None:
            self.head = self.head.next
        return

    def getMin(self):
        print(self.head.minVal)
        return

    def top(self):
        print(self.head.val)
        return


if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    minStack.getMin()
    minStack.pop()
    minStack.top()
    minStack.getMin()
