class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 0, 0
        first = True
        while slow != fast or first:
            slow = nums[slow]
            fast = nums[nums[fast]]
            first = False

        fast = 0
        first = True
        while fast != slow or first:
            slow = nums[slow]
            fast = nums[fast]
            first = False

        return slow

