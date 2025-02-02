class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.sort(nums)

    def sort(self, nums):
        middle = len(nums) // 2

        if len(nums) > 1:
            left = self.sort(nums[middle:])
            right = self.sort(nums[:middle])

            return self.merge(left, right)

        return nums

    def merge(self, left, right):
        merged = []
        l, r = 0, 0
        while l < len(left) and r < len(right):
            if left[l] > right[r]:
                merged.append(right[r])
                r += 1
            else:
                merged.append(left[l])
                l += 1

        while l < len(left):
            merged.append(left[l])
            l += 1

        while r < len(right):
            merged.append(right[r])
            r += 1

        return merged



