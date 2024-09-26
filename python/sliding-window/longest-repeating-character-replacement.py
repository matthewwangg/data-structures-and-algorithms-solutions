class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxcount, maxchar = 1, s[0]
        totalcount, left, answer = 0, 0, 0
        count = defaultdict(int)
        for i in range(len(s)):
            count[s[i]] += 1
            totalcount += 1
            if count[s[i]] > maxcount:
                maxchar = s[i]
                maxcount = count[s[i]]

            while totalcount - maxcount > k:
                if s[left] == maxchar:
                    maxcount -= 1
                count[s[left]] -= 1
                left += 1
                totalcount -= 1
                if count[s[left]] >= maxcount:
                    break

            answer = max(answer, i - left + 1)

        return answer