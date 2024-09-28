class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.table = {}
        self.size = capacity
        self.leftnode = Node(0, 0)
        self.rightnode = Node(0, 0)
        self.leftnode.next = self.rightnode
        self.rightnode.prev = self.leftnode

    def get(self, key: int) -> int:
        if key in self.table and self.table[key]:
            current = self.table[key]
            current.prev.next = current.next
            current.next.prev = current.prev
            self.rightnode.prev.next = current
            current.prev = self.rightnode.prev
            self.rightnode.prev = current
            current.next = self.rightnode
            self.table[key] = current
            return self.table[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.table and self.table[key]:
            current = self.table[key]
            current.value = value
            current.prev.next = current.next
            current.next.prev = current.prev
        else:
            current = Node(key, value)
            self.size -= 1

        self.rightnode.prev.next = current
        current.prev = self.rightnode.prev
        self.rightnode.prev = current
        current.next = self.rightnode
        self.table[key] = current

        if self.size == -1:
            self.table[self.leftnode.next.key] = None
            self.leftnode.next = self.leftnode.next.next
            self.leftnode.next.prev = self.leftnode
            self.size += 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)