class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        reversed = digits[::-1]
        carry = 1
        index = 0
        while carry > 0:
            if index == len(reversed):
                reversed.append(carry)
                break
            reversed[index], carry = (reversed[index] + carry) % 10, (reversed[index] + carry) // 10
            index += 1

        return reversed[::-1]


