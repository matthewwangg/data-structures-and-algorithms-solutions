class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = defaultdict(int)
        for i in range(len(s)):
            last[s[i]] = i
        finalanswer = []
        addition = ""
        end = last[s[0]]
        for i in range(len(s)):
            if i <= end:
                end = max(end, last[s[i]])
                addition += s[i]
            else:
                finalanswer.append(len(addition))
                addition = s[i]
                end = last[s[i]]

        if addition:
            finalanswer.append(len(addition))

        return finalanswer


