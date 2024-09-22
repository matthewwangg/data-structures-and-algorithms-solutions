class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash Map to keep count of the elements seen so far and their indexes
        # Key: Number, Value: Index of Number
        count = {}

        # O(n) loop over the nums array
        for i in range(len(nums)):
            # If the number to add to nums[i] to reach target has been found already
            if target - nums[i] in count:
                return [count[target - nums[i]], i]

            # Otherwise, note the index associated with the number
            count[nums[i]] = i

        # No need for return here, since we are guaranteed a solution
