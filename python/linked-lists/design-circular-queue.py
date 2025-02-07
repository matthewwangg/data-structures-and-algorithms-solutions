class ListNode:
    def __init__(self, val=-1, nex=None):
        self.val = val
        self.next = nex


class MyCircularQueue:

    def __init__(self, k: int):
        self.init = k
        self.capacity = k
        self.head = ListNode()

    def enQueue(self, value: int) -> bool:
        if self.capacity == 0:
            return False

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(value)
        self.capacity -= 1
        return True

    def deQueue(self) -> bool:
        if not self.head.next:
            return False

        self.head.next = self.head.next.next
        self.capacity += 1
        return True

    def Front(self) -> int:
        if not self.head.next:
            return -1

        return self.head.next.val

    def Rear(self) -> int:
        if not self.head.next:
            return -1

        curr = self.head
        while curr.next:
            curr = curr.next

        return curr.val

    def isEmpty(self) -> bool:
        return self.capacity == self.init

    def isFull(self) -> bool:
        return self.capacity == 0

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()