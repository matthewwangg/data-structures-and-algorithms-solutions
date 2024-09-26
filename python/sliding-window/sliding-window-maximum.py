import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = []
        heap = []
        count = defaultdict(int)
        for i in range(k):
            if nums[i] not in count:
                heapq.heappush(heap, -nums[i])
            count[nums[i]] += 1

        for i in range(k, len(nums)):
            count[nums[i]] += 1
            current = heapq.heappop(heap)
            answer.append(-current)
            count[nums[i - k]] -= 1

            if nums[i - k] == -current:
                while len(heap) > 0:
                    if count[-current] > 0:
                        break
                    current = heapq.heappop(heap)
            if count[-current] > 0:
                heapq.heappush(heap, current)
            heapq.heappush(heap, -nums[i])

        answer.append(-heapq.heappop(heap))

        return answer





