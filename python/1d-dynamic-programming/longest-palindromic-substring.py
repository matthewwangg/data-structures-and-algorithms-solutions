class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxstring = ""
        for i in range(len(s)):
            distance, current = 0, s[i:i + 1]
            while current == current[::-1]:
                if i - distance < 0 or i + distance == len(s):
                    break
                distance += 1
                current = s[i - distance:i + distance + 1]
            distance -= 1

            if distance * 2 + 1 > len(maxstring):
                maxstring = s[i - distance:i + distance + 1]

        for i in range(len(s) - 1):
            distance, current = 0, s[i:i + 2]
            while current == current[::-1]:
                if i - distance < 0 or i + distance == len(s):
                    break
                distance += 1
                current = s[i - distance:i + distance + 2]
            distance -= 1

            if distance * 2 + 2 > len(maxstring):
                maxstring = s[i - distance:i + distance + 2]

        return maxstring

