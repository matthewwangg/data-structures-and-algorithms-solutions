class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxleft, maxright = height[left], height[right]
        answer = 0
        while left < right:
            answer += min(maxleft, maxright)
            if height[left] < height[right]:
                answer -= height[left]
                left += 1
            else:
                answer -= height[right]
                right -= 1

            maxleft = max(maxleft, height[left])
            maxright = max(maxright, height[right])

        return answer


