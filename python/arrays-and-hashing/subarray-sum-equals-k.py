class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(lambda: 0)
        count[0] = 1
        prefix, answer = 0, 0
        for num in nums:
            prefix += num
            answer += count[prefix-k]
            count[prefix] += 1
        return answer