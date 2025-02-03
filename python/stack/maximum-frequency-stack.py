import heapq


class FreqStack:

    def __init__(self):
        self.heap = []
        self.count = defaultdict(lambda: 0)
        self.time = 0

    def push(self, val: int) -> None:
        self.count[val] += 1
        heapq.heappush(self.heap, (-self.count[val], self.time, val))
        self.time -= 1

    def pop(self) -> int:
        count, time, popped = heapq.heappop(self.heap)
        self.count[popped] -= 1
        return popped

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()