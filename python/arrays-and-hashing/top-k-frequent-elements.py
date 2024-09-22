import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create finalanswer array
        finalanswer = []
        # Hash Map to keep count of the number of elements equal to the key
        # Key: Numbers, Value: Count of Numbe
        count = defaultdict(int)

        # O(n) loop to keep track of the count of each number
        for i in nums:
            count[i] += 1

        # Heap to arrange K most frequent
        heap = []

        # O(n) loop to populate the heap based on count, with the highest count being at the top of the heap
        for i in count.keys():
            heapq.heappush(heap, (-count[i], i))

        # Popping the K most frequent elements from the heap and appending them to the final array
        for i in range(k):
            finalanswer.append(heapq.heappop(heap)[1])

        return finalanswer



