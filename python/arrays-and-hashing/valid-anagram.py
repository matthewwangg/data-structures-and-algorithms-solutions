class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Hash Map to keep count of the difference in count of variables between s and t
        count = defaultdict(int)

        # O(n) loop through s and increment the counter for each character of s
        for i in s:
            count[i] += 1

        # O(n) loop through t and decrement the counter for each character of t
        for i in t:
            count[i] -= 1

        # O(n) loop through letters to check if any characters had different counts between s and t
        for i in count.keys():
            # If a counter didn't equal 0, this means s and t are not anagrams
            if count[i] != 0:
                return False

        # If every counter was 0, then they were anagrams
        return True
