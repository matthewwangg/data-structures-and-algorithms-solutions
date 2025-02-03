# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        centralindex = 0
        left, right = 1, mountainArr.length() - 2
        while left <= right:
            mid = (left + right) // 2
            l, m, r = mountainArr.get(mid - 1), mountainArr.get(mid), mountainArr.get(mid + 1)
            if m > r and m > l:
                centralindex = mid
                break
            if m > r:
                right = mid - 1
            else:
                left = mid + 1

        left, right = 0, centralindex
        while left <= right:
            mid = (left + right) // 2
            curr = mountainArr.get(mid)
            if curr == target:
                return mid

            if curr > target:
                right = mid - 1
            else:
                left = mid + 1

        left, right = centralindex, mountainArr.length() - 1
        while left <= right:
            mid = (left + right) // 2
            curr = mountainArr.get(mid)
            if curr == target:
                return mid

            if curr < target:
                right = mid - 1
            else:
                left = mid + 1

        return -1