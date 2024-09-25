class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        k = (len(nums1) + len(nums2))
        odd = False
        if k % 2 == 1:
            k = k // 2
            k += 1
            odd = True
        else:
            k = k // 2

        while k > 1:
            if len(nums1) == 0 or len(nums2) == 0:
                break
            if k % 2 == 0:
                current = k // 2 - 1
                if current > len(nums1) - 1 or current > len(nums2) - 1:
                    current = min(len(nums1) - 1, len(nums2) - 1)
                num1 = nums1[current]
                num2 = nums2[current]
                if num1 > num2:
                    nums2 = nums2[current + 1:]
                else:
                    nums1 = nums1[current + 1:]
                k -= current + 1
            else:
                tempk = k - 1
                current = tempk // 2 - 1
                if current > len(nums1) - 1 or current > len(nums2) - 1:
                    current = min(len(nums1) - 1, len(nums2) - 1)
                num1 = nums1[current]
                num2 = nums2[current]
                if num1 > num2:
                    nums2 = nums2[current + 1:]
                else:
                    nums1 = nums1[current + 1:]
                k -= current + 1

        if len(nums1) == 0:
            if odd:
                return nums2[k - 1]
            else:
                return (nums2[k - 1] + nums2[k]) / 2
        if len(nums2) == 0:
            if odd:
                return nums1[k - 1]
            else:
                return (nums1[k - 1] + nums1[k]) / 2

        if odd:
            return min(nums1[0], nums2[0])
        else:
            one = nums1[0]
            two = nums2[0]
            if len(nums2) > 1 and nums2[1] < one:
                return (nums2[0] + nums2[1]) / 2
            elif len(nums1) > 1 and nums1[1] < two:
                return (nums1[0] + nums1[1]) / 2
            return (nums1[0] + nums2[0]) / 2

