class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1, c2 = None, None
        count1, count2 = 0, 0
        for num in nums:
            if num == c1:
                count1 += 1
            elif num == c2:
                count2 += 1
            elif count1 == 0:
                count1 = 1
                c1 = num
            elif count2 == 0:
                count2 = 1
                c2 = num
            else:
                count2 -= 1
                count1 -= 1

        answer = []
        if nums.count(c1) > len(nums) // 3:
            answer.append(c1)
        if nums.count(c2) > len(nums) // 3:
            answer.append(c2)
        return answer


