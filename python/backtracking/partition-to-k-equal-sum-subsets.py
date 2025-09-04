class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False

        target = sum(nums) // k
        subsets = [0 for _ in range(k)]

        def partition(i):
            valid = True
            for subset in subsets:
                if subset != target:
                    valid = False

            if valid and i == len(nums):
                return True

            if i == len(nums):
                return False

            answer = False
            for k in range(len(subsets)):
                if target < subsets[k] + nums[i]:
                    continue
                subsets[k] += nums[i]
                answer = answer or partition(i + 1)
                if answer:
                    break
                subsets[k] -= nums[i]

                if subsets[k] == 0:
                    break

            return answer

        return partition(0)
