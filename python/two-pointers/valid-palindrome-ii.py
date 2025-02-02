class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        valid, left, right = self.palindrome(s, left, right)

        if valid:
            return True

        valid, _, _ = self.palindrome(s, left + 1, right)
        if valid:
            return True

        valid, _, _ = self.palindrome(s, left, right - 1)
        if valid:
            return True

        return False

    def palindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False, left, right
            left += 1
            right -= 1

        return True, 0, len(s) - 1