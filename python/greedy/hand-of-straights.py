class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = defaultdict(int)
        for i in hand:
            count[i] += 1

        for i in sorted(count.keys()):
            while count[i] > 0:
                for j in range(groupSize):
                    count[i + j] -= 1
                    if count[i + j] < 0:
                        return False

        return True