class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Hash Map where the values will be of type int
        # Key: Number, Value: Count in Array
        counter = defaultdict(int)

        # O(n) loop through the numbers
        for i in nums:
            # Average case O(1) lookup
            if counter[i] == 1:
                return True

            # Increment the counter of that number i
            counter[i] += 1

        # If made it through the loop, can be assured there is no duplicate
        return False
