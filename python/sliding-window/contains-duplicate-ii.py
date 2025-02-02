class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        count = defaultdict(lambda: 0)
        for i in range(len(nums)):
            if count[nums[i]] > 0:
                return True

            if i - k > -1:
                count[nums[i - k]] -= 1

            count[nums[i]] += 1

        return False

