class ListNode:
    def __init__(self, key=-1):
        self.key = key
        self.next = None


class MyHashSet:

    def __init__(self):
        self.map = [ListNode() for _ in range(1000)]

    def hash(self, key):
        return key % 1000

    def add(self, key: int) -> None:
        index = self.hash(key)
        curr = self.map[index]

        while curr.next:
            if curr.next.key == key:
                return
            curr = curr.next

        curr.next = ListNode(key)

    def remove(self, key: int) -> None:
        index = self.hash(key)
        curr = self.map[index]

        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                break
            curr = curr.next

    def contains(self, key: int) -> bool:
        index = self.hash(key)
        curr = self.map[index]

        while curr.next:
            if curr.next.key == key:
                return True
            curr = curr.next

        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)