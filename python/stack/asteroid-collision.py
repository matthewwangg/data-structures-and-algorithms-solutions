class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:
                broken = False
                while stack and (stack[-1] > 0 and asteroid < 0):
                    right = stack.pop()
                    if right >= abs(asteroid):
                        if right > abs(asteroid):
                            stack.append(right)
                        broken = True
                        break

                if not broken:
                    stack.append(asteroid)

        return stack


