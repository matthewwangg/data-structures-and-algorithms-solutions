class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        two, zero = len(nums) - 1, 0
        for i in range(len(nums)):
            if i > two:
                return

            while nums[i] == 2:
                nums[i], nums[two] = nums[two], nums[i]
                two -= 1

                if i > two:
                    return

            while nums[i] == 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1

                if zero > i:
                    break





