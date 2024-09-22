class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Arrays for left direction product and right direction product
        left = [1 for _ in range(len(nums) + 1)]
        right = [1 for _ in range(len(nums) + 1)]

        # 2 separate O(n) loops to populate the arrays in each direction
        for i in range(len(nums)):
            left[i + 1] = left[i] * nums[i]
        for i in range(len(nums) - 1, -1, -1):
            right[i] = right[i + 1] * nums[i]

        # Final return array
        final = [1 for _ in range(len(nums))]

        # Populate the final array based on the multiplication of left and right arrays
        for i in range(len(nums)):
            final[i] = left[i] * right[i + 1]

        return final


