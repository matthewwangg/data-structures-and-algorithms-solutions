class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            distance, current = 0, s[i:i + 1]
            while current == current[::-1]:
                if i - distance < 0 or i + distance == len(s):
                    break
                distance += 1
                current = s[i - distance:i + distance + 1]
                count += 1

        for i in range(len(s) - 1):
            distance, current = 0, s[i:i + 2]
            while current == current[::-1]:
                if i - distance < 0 or i + 1 + distance >= len(s):
                    break
                distance += 1
                current = s[i - distance:i + distance + 2]
                count += 1

        return count