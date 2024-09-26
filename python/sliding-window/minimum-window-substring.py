class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = defaultdict(int)
        chaser = defaultdict(int)
        answer = ""
        for i in t:
            target[i] += 1

        left = 0
        for i in range(len(s)):
            chaser[s[i]] += 1
            if i >= len(t) - 1:
                valid = True
                while valid:
                    for j in target.keys():
                        if target[j] > chaser[j]:
                            valid = False
                            break
                    if not valid:
                        break
                    if answer == "" or len(answer) > i - left + 1:
                        answer = s[left:i + 1]
                    chaser[s[left]] -= 1
                    left += 1

        return answer
