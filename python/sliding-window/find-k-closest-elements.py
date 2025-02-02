class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k >= len(arr):
            return arr

        # Binary search to find closest element to x
        left, right = 0, len(arr) - 1
        closest = None
        while left <= right:
            middle = (left + right) // 2
            if arr[middle] == x:
                closest = middle
                break

            if closest is None or (abs(arr[middle] - x) < abs(arr[closest] - x) or (
                    abs(arr[middle] - x) == abs(arr[closest] - x) and middle < closest)):
                closest = middle

            if arr[middle] > x:
                right = middle - 1
            else:
                left = middle + 1

        leftBorder, rightBorder = closest, closest + 1
        while rightBorder - leftBorder - 1 < k:
            if leftBorder == -1:
                rightBorder += 1
            elif rightBorder == len(arr):
                leftBorder -= 1
            else:
                if abs(x - arr[leftBorder]) <= abs(x - arr[rightBorder]):
                    leftBorder -= 1
                else:
                    rightBorder += 1

        return arr[leftBorder + 1:rightBorder]



