class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Hash Map to store the groups of anagram strings
        # Key: Sorted Tuple of String, Value: List of each string that is an anagram of the key
        groups = defaultdict(list)

        # O(n) loop over the input array
        for i in strs:
            # Sorting i is O(1) because the length of each string is guaranteeed to be 3
            # Append each string i to its appropriate group
            groups[tuple(sorted(i))].append(i)

        # Create the list for the finalanswer
        finalanswer = []
        # O(n) loop over the keys of the groups
        for i in groups.keys():
            # Append each group to the finalanswer array
            finalanswer.append(groups[i])
        return finalanswer