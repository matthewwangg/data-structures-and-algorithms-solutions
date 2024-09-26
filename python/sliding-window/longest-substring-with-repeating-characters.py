class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characters = defaultdict(int)
        left = 0
        answer = 0
        for i in range(len(s)):
            if characters[s[i]] > 0:
                while characters[s[i]] > 0:
                    characters[s[left]] -= 1
                    left += 1

            characters[s[i]] = 1

            answer = max(answer, i - left + 1)

        return answer
