class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        validone = []
        for i in triplets:
            if i[0] <= target[0]:
                validone.append(i)
        validtwo = []
        for i in validone:
            if i[1] <= target[1]:
                validtwo.append(i)
        validthree = []
        for i in validtwo:
            if i[2] <= target[2]:
                validthree.append(i)

        seenone, seentwo, seenthree = False, False, False
        for i in validthree:
            if i[0] == target[0]:
                seenone = True
            if i[1] == target[1]:
                seentwo = True
            if i[2] == target[2]:
                seenthree = True

        return seenone and seentwo and seenthree
