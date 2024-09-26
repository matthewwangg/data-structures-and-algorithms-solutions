class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = defaultdict(int)
        for i in s1:
            target[i] += 1

        current = defaultdict(int)
        left = 0
        for i in range(len(s2)):
            if s2[i] not in target:
                while left < i:
                    if s2[left] not in target:
                        left += 1
                        continue
                    else:
                        current[s2[left]] -= 1
                        left += 1
            else:
                current[s2[i]] += 1
                while current[s2[i]] > target[s2[i]]:
                    if s2[left] not in target:
                        left += 1
                        continue
                    else:
                        current[s2[left]] -= 1
                        left += 1
            if current == target:
                return True

        return False

