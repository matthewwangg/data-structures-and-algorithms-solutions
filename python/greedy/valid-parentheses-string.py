class Solution:
    def checkValidString(self, s: str) -> bool:
        opened = 0
        right, left, star = 0, 0, 0
        for i in s:
            if i == "(":
                left += 1
                opened += 1
            elif i == ")":
                right += 1
                opened -= 1
            else:
                star += 1
                opened -= 1

            opened = max(opened, 0)

            if right > left + star:
                return False

        return opened == 0
