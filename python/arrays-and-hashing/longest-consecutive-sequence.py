class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Hash Map to track which numbers are present
        # Key: Number, Value: 1
        hashmap = {}
        for i in nums:
            hashmap[i] = 1

        # Final answer number
        finalanswer = 0

        # O(n) loop over keys of the hash map
        for i in hashmap.keys():
            # If the current key is not the start of a sequence, continue
            if hashmap.get(i - 1, 0) == 1:
                continue
            else:
                # Loop through the sequence and see how far it goes
                current = i
                while hashmap.get(current, 0) == 1:
                    # Save the answer if its higher than the current final answer
                    finalanswer = max(finalanswer, current - i + 1)
                    current += 1

        return finalanswer
