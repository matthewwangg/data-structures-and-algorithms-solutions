class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        minimum, maximum = max(nums), sum(nums)
        answer = maximum
        while minimum <= maximum:
            mid = (minimum+maximum) // 2
            splits = 1
            curr = 0
            for num in nums:
                curr += num
                if curr > mid:
                    splits += 1
                    curr = num

            if splits > k:
                minimum = mid + 1
            else:
                answer = min(mid, answer)
                maximum = mid - 1

        return answer
