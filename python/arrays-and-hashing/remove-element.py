class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        safe, last = 0, len(nums) - 1
        for i in range(len(nums)):
            if nums[i] != val:
                safe += 1
                continue

            while nums[last] == val:
                last -= 1

                if last <= i:
                    return safe

            nums[i], nums[last] = nums[last], nums[i]
            safe += 1

        return len(nums)