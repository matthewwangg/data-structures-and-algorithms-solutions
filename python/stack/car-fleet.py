class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = [(position[i], speed[i]) for i in range(len(position))]
        combined.sort()
        combined = combined[::-1]
        stack = [-1]
        for i in combined:
            time = (target - i[0]) / i[1]
            if time <= stack[-1]:
                continue
            else:
                stack.append(time)

        return len(stack) - 1
